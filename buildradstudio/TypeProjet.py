#-*- coding: utf-8 -*-

from enum import Enum

class TypeProjet(Enum):
    Librairie = "lib"
    PackageExe = "excecution"
    PackageIde = "conception"
    Application = "appli"
    Test = "test"


class Plateforme(Enum):
    WIN32 = "Win32"
    WIN64 = "Win64"


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

