# -*- coding: utf-8 -*-

import os
import subprocess
from .Embarcadero import Embarcadero


def singleton(cls):
    instance = None

    def ctor(*args, **kwargs):
        nonlocal instance
        if not instance:
            instance = cls(*args, **kwargs)
        return instance

    return ctor


def FirstSympEnv(chaine):
    """
    recherche le premier mot entre deux "%" est le retourne
    """
    p1 = chaine.find("%")
    p2 = chaine.find("%", p1 + 1)
    if p1 == -1 or p2 == -1:
        return None
    return chaine[p1 + 1:p2]

@singleton
class CmdRad(object):
    """ Classe de gestion des commandes pour Ide Rad studio
         Singleton class
    """
    def __init__(self):
        self.Emb = Embarcadero()
        self.paramsOsEnv = self.Emb.getrsvars()
        self.__cwd = None
        self.EnCours = False
        self.EnvRad = subprocess.os.environ.copy()
        self.miseAjourEnv(self.EnvRad)

    def __getitem__(self, key):
        return self.EnvRad[key]

    def __setitem__(self, key, value):
        self.EnvRad[key] = value

    def ResolutionEnv(self, chaine):
        """
        Remplace les variables par leur valeur et retourne le résultat
        """
        dico = dict(self.paramsOsEnv)
        k = FirstSympEnv(chaine)
        while k != None:
            K = k.upper()
            if K in self.EnvRad:
                chaine = chaine.replace("%" + k + "%", self.EnvRad[K])
            else:
                if K in dico:
                    chaine = chaine.replace("%" + k + "%", dico[K])
                else:
                    raise Exception("CmdRad", "set env non definie", k)
            k = FirstSympEnv(chaine)  # suivant
        return chaine

    def miseAjourEnv(self, ev):
        for k, v in self.paramsOsEnv:
            ev[k] = self.ResolutionEnv(v)


    @property
    def cwd(self):
        return self.__cwd

    @cwd.setter
    def cwd(self, value):
        self.__cwd = os.path.expandvars(value)

    def DebutCde(self, cde):
        if self.EnCours == True and self.build.poll() == None:
            raise Exception("Build en cours de :", self.cde)
        self.Projet = cde
        self.EnCours = True
        print("cde", cde, "cwd", self.cwd)
        self.build = subprocess.Popen(cde, shell=True, cwd=self.cwd, env=self.EnvRad, stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE, encoding="cp860")

    def DebutMsBuild(self, projet):
        self.DebutCde("msbuild " + projet)

    # todo evt message, branche des logger, analyser les traces
    def Attente(self):
        while self.build.poll() is None:
            a, b = self.build.communicate()
            print(a)
        self.EnCours = False
        if (self.build.poll() != 0):
            raise Exception("Erreur de build :", self.Projet, self.build.poll())

    def MsBuild(self, projet):
        self.DebutMsBuild(projet)
        self.Attente()

    def Cde(self, projet):
        self.DebutCde(projet)
        self.Attente()
