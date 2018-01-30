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
    UNINSTALL = "uninstall"
    CLEAN = "clean"
    BUILD = "build"
    MAKE = "make"
    TEST = "valide"
    INSTALL = "install"



TousTypeProjets = list(TypeProjet)

Phase1Projets=[TypeProjet.Librairie,TypeProjet.PackageExe]
Phase2Projets=[TypeProjet.PackageIde]
Phase3Projets=[TypeProjet.Application, TypeProjet.Test]


ToutesPlateformes = list(Plateforme)
ToutesConfigs = list(Config)
TousTargets = [Target.CLEAN, Target.BUILD,Target.TEST, Target.INSTALL ]


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