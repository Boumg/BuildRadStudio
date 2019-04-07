# -*- coding: utf-8 -*-

import os
import subprocess
from .CmdWindows import get_code_page
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


class Cmd(object):
    """ Classe de gestion des commandes pour Ide Rad studio
         Singleton class
    """

    def __init__(self, envBuild={}):
        self.EnvBuild = envBuild
        self.__cwd = None
        self.EnCours = False
        self.EnvSystem = subprocess.os.environ.copy()

        self.miseAjourEnv(self.EnvSystem)

    def __getitem__(self, key):
        return self.EnvSystem[key]

    def __setitem__(self, key, value):
        self.EnvSystem[key] = value

    def ResolutionEnv(self, chaine):
        """
        Remplace les variables par leur valeur et retourne le résultat
        """
        dico = dict(self.EnvBuild)
        k = FirstSympEnv(chaine)
        while k != None:
            K = k.upper()
            if K in self.EnvSystem:
                chaine = chaine.replace("%" + k + "%", self.EnvSystem[K])
            else:
                if K in dico:
                    chaine = chaine.replace("%" + k + "%", dico[K])
                else:
                    raise Exception("CmdRad", "set env non definie", k)
            k = FirstSympEnv(chaine)  # suivant
        return chaine

    def miseAjourEnv(self, ev):
        for k, v in self.EnvBuild:
            ev[k] = self.ResolutionEnv(v)

    @property
    def cwd(self):
        return self.__cwd

    @cwd.setter
    def cwd(self, value):
        self.__cwd = os.path.expandvars(value)

    def DebutCde(self, cde):
        if self.EnCours == True and self.build.poll() == None:
            raise Exception("Build en cours de :", cde)
        self.Projet = cde
        self.EnCours = True
        print("cde", cde, "cwd", self.cwd)
        self.build = subprocess.Popen(cde, shell=True, cwd=self.cwd, env=self.EnvSystem, stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE, encoding=get_code_page(), errors="surrogateescape")

    def DebutMsBuild(self, projet):
        self.DebutCde("msbuild " + projet)

    def AffichageCmd(self, line):
        if (line is None):
            return
        if len(line) == 0:
            return
        try:
            print(line, end='', flush=True)
        except UnicodeEncodeError as e:
            print(str(e), line.encode('UTF-8'), end='', flush=True)

    def Attente2(self):
        iterout = iter(self.build.stdout.readline, "")
        for line in iterout:
            self.AffichageCmd(line)
            if (not (self.build.poll() is None)):
                break
        self.EnCours = False
        outs, errs = self.build.communicate()
        self.AffichageCmd(errs)
        self.AffichageCmd(outs)
        print("fin")
        if (self.build.poll() != 0):
            raise Exception("Erreur de build :", self.Projet, self.build.poll())

    def Attente(self):
        while self.build.poll() is None:
            a, b = self.build.communicate()
            try:
                print(a)
                print(b)
            except UnicodeEncodeError as e:
                print(str(e))

            # print(f"info:'{a}'")
            # print(f"err:'{b}'")

        self.EnCours = False
        if (self.build.poll() != 0):
            raise Exception("Erreur de build :", self.Projet, self.build.poll())

    def MsBuild(self, projet):
        self.DebutMsBuild(projet)
        self.Attente2()

    def Cde(self, projet):
        self.DebutCde(projet)
        self.Attente()


@singleton
class CmdRad(Cmd):
    """ Classe de gestion des commandes pour Ide Rad studio
         Singleton class
    """

    def __init__(self):
        super().__init__(Embarcadero().getrsvars())


@singleton
class CmdDef(Cmd):
    """ Classe de gestion des commandes pour Ide Rad studio
         Singleton class
    """

    def __init__(self):
        super().__init__()


def CdeRad(cde: str, cwd: str = None):
    if cwd:
        CmdRad().cwd = cwd
    CmdRad().Cde(cde)


def Cde(cde: str, cwd: str = None):
    if cwd:
        CmdDef().cwd = cwd
    CmdDef().Cde(cde)
