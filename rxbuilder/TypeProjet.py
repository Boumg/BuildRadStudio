#-*- coding: utf-8 -*-

from enum import Enum
from pathlib import Path


class TypeProjet(Enum):
    Librairie = "lib"
    PackageExe = "excecution"
    PackageIde = "conception"
    Application = "appli"
    Test = "test"


class Plateforme(Enum):
    WIN64 = "Win64"
    WIN32 = "Win32"



class Config(Enum):
    RELEASE = "Release"
    DEBUG = "Debug"


class Target(Enum):
    CLEAN = "clean"
    BUILD = "build"
    MAKE = "make"
    INSTALL = "install"
    UNINSTALL = "uninstall"
    TEST = "valide"


TousTypeProjets = list(TypeProjet)
ToutesPlateformes = list(Plateforme)
ToutesConfigs = list(Config)
TousTargets = [Target.CLEAN, Target.BUILD, Target.INSTALL, Target.TEST]


class RXSuffix(Enum):
    CPP = "cbproj"
    DEPLOY = "deployproj"
    DELPHIP = "dproj"
    GROUP = "groupproj"

    @classmethod
    def getEext(self, fichier):
        """
         retour le type de fichier msbuild,
         sinon une erreur si le fichier n'est pas msbuild
        """
        fic = Path(fichier.lower())
        ext = fic.suffix[1:]
        if ext[-4:] != "proj":
            raise Exception("Le fichier n'est pas de type msbuild , ", fichier)
        trouve = None
        for e in RXSuffix:
            if ext == e.value:
                trouve = e
                break
        if not trouve:
            raise Exception("Le fichier n'est pas de type Rad Studio , ", fichier)
        return trouve