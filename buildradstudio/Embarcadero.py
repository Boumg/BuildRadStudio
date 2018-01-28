# -*- coding: utf-8 -*-

import winreg


class Registre(object):

    def __init__(self, pathreg, hklm=winreg.HKEY_CURRENT_USER):
        self._hklm = None
        self._reg = hklm
        self._keyR = None
        self._path = pathreg

    @property
    def path(self):
        return self._path

    @path.setter
    def setPath(self, value):
        if self._path != value:
            self._keyR = None
            self._path = value

    @property
    def hklm(self):
        if self._hklm == None:
            self._hklm = winreg.ConnectRegistry(None, self._reg)
        return self._hklm

    @property
    def keyR(self):
        if self._keyR == None:
            self._keyR = winreg.OpenKey(self.hklm, self.path, 0, winreg.KEY_ALL_ACCESS)
        return self._keyR

    NO_DEFAULT = type(str('NO_DEFAULT'), (object,), {})()

    def getValeur(self, name, default=NO_DEFAULT):
        try:
            value = winreg.QueryValueEx(self.keyR, name)[0]
        except WindowsError:
            if default is self.NO_DEFAULT:
                raise ValueError("No such registry key", name)
            value = default
        return value

    def setValeur(self, name, val, default=NO_DEFAULT):
        try:
            winreg.SetValueEx(self.keyR, name, 0, winreg.REG_SZ, val)
        except WindowsError:
            if default is self.NO_DEFAULT:
                raise ValueError("Writing registry key failed ! - ", name)

    def getRuche(self, value):
        return winreg.OpenKey(self.keyR, value, 0, winreg.KEY_READ)

    def getRegistre(self, value):
        reg = self._path
        if reg[-1] != "\\":
            reg += "\\"
        return Registre(reg + value, self._reg)

    def siExisteRuche(self, value=""):
        try:
            self.getRuche(value)
        except WindowsError:
            return False
        return True

    def siExisteValeur(self, name):
        try:
            self.value = winreg.QueryValueEx(self.keyR, name)[0]
        except WindowsError:
            return False
        return True

    def effacerValeur(self, name):
        try:
            winreg.DeleteValue(self.keyR, name)
        except WindowsError:
            raise ValueError("Deleting registry key failed ! - ", name)

    def effacerValeurSiExiste(self, name):
        if self.siExisteValeur(name):
            self.effacerValeur(name)

    def ListeSubKey(self, nb_subk):
        liste_subk = []
        indexSk = 0
        while indexSk < nb_subk:
            liste_subk.append(winreg.EnumKey(self.keyR, indexSk))
            indexSk += 1
        return liste_subk

    def effacerCle(self, nomCle):
        if self.siExisteRuche(nomCle):
            subKey = self.getRegistre(nomCle)
            nb_subk, nb_v, t = winreg.QueryInfoKey(subKey.keyR)
            if (nb_subk > 0):
                for subkname in subKey.ListeSubKey(nb_subk):
                    subKey.effacerCle(subkname)
            winreg.DeleteKey(self.keyR, nomCle)

    '''            
    def expand(obj):        
        # expand obj
        return obj
    '''

    def listerValeurs(self, value_name):
        valeurs = self.getValeur(value_name)
        liste = valeurs.split(';')
        return liste

    def ajouterPath(self, value_name, path):
        oldValue = self.getValeur(value_name)
        newValue = oldValue + ";" + path
        self.setValeur(value_name, newValue)


"""Dectection des versions installés de Delphi"""
DelphiRegPath = 'Software\\Embarcadero\\BDS\\'

Nom = 'RAD Studio'
VersionRad = {"12.0": "xe5", "13.0": "xe6", "14.0": "xe7", "15.0": "xe8", "16.0": "xe9", "17.0": "seattle",
              "18.0": "berlin", "19.0": "tokyo", "20.0": "xe20?", "21.0": "xe21?"}

subKeyWin32 = "C++\\Paths\\Win32"
subKeyWin64 = "C++\\Paths\\Win64"

inclPath = "IncludePath"
libPath = "LibraryPath"
inclPath_Clang32 = "IncludePath_Clang32"
libPath_Clang32 = "LibraryPath_Clang32"


def singleton(cls):
    instance = None

    def ctor(*args, **kwargs):
        nonlocal instance
        if not instance:
            instance = cls(*args, **kwargs)
        return instance

    return ctor


@singleton
class Embarcadero(object):
    """description of class
        singleton
    """
    _DelphiRuche = Registre(DelphiRegPath)


    @classmethod
    def getVersions(c):
        return [a for a in sorted(VersionRad.items()) if c._DelphiRuche.siExisteRuche(a[0] + "\\C++")]

    @classmethod
    def getDerniereVersion(c):
        c.Versions = c.getVersions()
        if len(c.Versions) == 0:
            raise Exception("Embarcadero", "Pas de version trouvee de Rad studio")
        return c.Versions[-1]

    def __init__(self):
        self.Version = self.getDerniereVersion()
        self._RucheVersion = self._DelphiRuche.getRegistre(self.Version[0])

    def getRegistreBDS(self, nomSsRuche):
        return self.getRucheBDS.getRegistre(nomSsRuche)

    @property
    def RootDir(self):
        return self._RucheVersion.getValeur("RootDir")

    @property
    def Bin(self):
        return self.RootDir + 'bin\\'

    @property
    def getRucheBDS(self):
        return self._RucheVersion

    def getrsvars(s):
        fichier = s.Bin + "rsvars.bat"
        with open(fichier, 'r') as mon_fichier:
            v = [ligne.replace("@SET", '').strip().split("=") for ligne in mon_fichier.read().splitlines() if
                 ligne != ""]
            for e in v:
                e[0] = e[0].upper()
            return v

    def addReg(self, subkey_name, value_name, path):
        cle = self.getRucheBDS.getRegistre(subkey_name)
        valeurs = cle.listerValeurs(value_name)
        if not (path in valeurs):
            cle.ajouterPath(value_name, path)
            # returnS uniquement utilise par les unittests
            return False
        return True

    def checkReg(self, subkey_name, value_name, path):
        cle = self.getRucheBDS.getRegistre(subkey_name)
        valeurs = cle.listerValeurs(value_name)
        if not (path in valeurs):
            return False
        return True

    # check Include Path in registry
    def checkIncludeRegWin32(self, path):
        return self.addReg(subKeyWin32, inclPath, path)

    def checkIncludeRegWin32CLang(self, path):
        return self.addReg(subKeyWin32, inclPath_Clang32, path)

    def checkIncludeRegWin64(self, path):
        return self.addReg(subKeyWin64, inclPath, path)

    # check Add Library Path in registry
    def checkAddLibRegWin32(self, path):
        return self.checkReg(subKeyWin32, libPath, path)

    def checkAddLibRegWin32CLang(self, path):
        return self.checkReg(subKeyWin32, libPath_Clang32, path)

    def checkAddLibRegWin64(self, path):
        return self.checkReg(subKeyWin64, libPath, path)
