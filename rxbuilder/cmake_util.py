# -*- coding: utf-8 -*-
from pathlib import Path
from shutil import which

from .CmdRad import Cde
from .VerifAvantCompilation import checkVarEnv, suppression_repertoire

def _get_cmake_dir():
    return checkVarEnv("PROGRAMFILES") / r"cmake/bin"

def _get_cmake():
    """
      recherche de l'executable cmake
        :return: cmake executable
    """
    return which("cmake", path=str(_get_cmake_dir()))

def _get_ctest():
    """
      recherche de l'executable ctest
        :return: ctest executable
    """
    return which("ctest", path=str(_get_cmake_dir()))

def is_cmake():
    return _get_cmake() != None


def get_ctest_cde():
    """
      recherche de l'executable ctest.exe
        :return: ctest executable
    """
    ctest_exe = _get_ctest()
    if ctest_exe:
        return '"' + ctest_exe + '" '
    else:
        cmake_dir=_get_cmake_dir()
        raise Exception(f" Pas de commande cmake , sous le repertoire {cmake_dir}-> installer cmake ")

def get_cmake_cde():
    """
      recherche de l'executable cmake
        :return: cmake executable
    """
    cmake_exe = _get_cmake()
    if cmake_exe:
        return '"' + cmake_exe + '" '
    else:
        cmake_dir = _get_cmake_dir()
        raise Exception(f" Pas de commande ctest , sous le repertoire {cmake_dir}-> installer cmake ")


def BuildCmakeVS(cwd_build: Path, installDir="", option="", configs=("Release",)):
    """
     genere un projet  Visual Studio 15 2017 Win64 avec cmake et l'install
     le repertoire de buile (cwd_build) est supprime avant de lancer cmake

    :param cwd_build:  repertoire de build
    :param installDir: repertoire installation
    :param option: option de generation du projet
    :param  configs : tuple des configs generer
    """

    suppression_repertoire(cwd_build)
    cwd_build.mkdir()
    str_cwd = str(cwd_build)
    if installDir:
        Cde(
            get_cmake_cde() + r' -DCMAKE_INSTALL_PREFIX=' + installDir + option + r' -G"Visual Studio 15 2017 Win64" ..',
            cwd=str_cwd)
    else:
        Cde(get_cmake_cde() + r' ' + option + r' -G"Visual Studio 15 2017 Win64" ..', cwd=str_cwd)

    for config in configs:
        if installDir:
            cde = get_cmake_cde() + f" --build  . --config {config} --target INSTALL"
        else:
            cde = get_cmake_cde() + f" --build  . --config {config} "
        Cde(cde, cwd=str_cwd)


def CtestCmakeVS(cwd_build: Path, configs=("Release",)):
    """
     test d'un projet  Visual Studio 15 2017 Win64 avec cmake et l'install

    :param cwd_build:  repertoire de build
    :param  configs : tuple des configs generer

    """

    str_cwd = str(cwd_build)

    for config in configs:
        """  "c:\Program Files\CMake\bin\ctest.exe"  -V -C debug  --no-compress-output -T Test || verify > NUL 
		Le fichier resultat est sous <build>\Testing\<Date>\Test.xml
		pattern  junit **/Testing/**/Test.xml 
		"""
        cde = get_ctest_cde() + f"  -V  -C {config} --no-compress-output -T test  || verify > NUL"
        Cde(cde, cwd=str_cwd)
