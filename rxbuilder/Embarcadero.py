# -*- coding: utf-8 -*-

from .CmdWindows import Registre

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
        return [a for a in sorted(VersionRad.items()) if c._DelphiRuche.si_existe_ruche(a[0] + "\\C++")]

    @classmethod
    def getDerniereVersion(c):
        c.Versions = c.getVersions()
        if len(c.Versions) == 0:
            raise Exception("Embarcadero", "Pas de version trouvee de Rad studio")
        return c.Versions[-1]

    def __init__(self):
        self.Version = self.getDerniereVersion()
        self._RucheVersion = self._DelphiRuche.get_registre(self.Version[0])

    def getRegistreBDS(self, nomSsRuche):
        return self.getRucheBDS.get_registre(nomSsRuche)

    @property
    def RootDir(self):
        return self._RucheVersion.get_valeur("RootDir")

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
        cle = self.getRucheBDS.get_registre(subkey_name)
        valeurs = cle.lister_valeurs(value_name)
        if not (path in valeurs):
            cle.ajouter_chemin(value_name, path)
            # returnS uniquement utilise par les unittests
            return False
        return True

    def checkReg(self, subkey_name, value_name, path):
        cle = self.getRucheBDS.get_registre(subkey_name)
        valeurs = cle.lister_valeurs(value_name)
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
