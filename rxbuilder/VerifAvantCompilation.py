# -*- coding: utf-8 -*-

import clr
from System.Diagnostics import Process
from pathlib import Path
from shutil import rmtree
import time
import os
from .CmdRad import CmdRad
from  .version import __version__

"""
Remplace le code dos suivant :

Set "MyProcess=bds.exe"
Title Verification de l^'execution du processus "%MyProcess%"
:Loop

Set "MyProcess=bds.exe"
Title Verification de l^'execution du processus "%MyProcess%"
:Loop
tasklist /nh /fi "imagename eq %MyProcess%" 2>nul |find /i "%MyProcess%" >nul
if not errorlevel 1 (
    Color 0C
    Echo "%MyProcess%" est en cours d^'execution
    Echo Veuillez quitter l'application, sinon la construction des Composants ne sera pas possible
    pause
    goto Loop
)
Color 0F

"""

RADSTUDIO_IDE_NOM = 'bds'


def siProcessEnCours(nom: str) -> bool:
    p = [v.ProcessName for v in Process.GetProcesses()]
    return nom in p


def siIdeBdsEnCours() -> bool:
    return siProcessEnCours(RADSTUDIO_IDE_NOM)


def attenteArretBds():
    if siIdeBdsEnCours():
        os.system("color 0C")
        print("Rad Studio (BDS)  est en cours d'exécution")
        print("Veuillez quitter l'application, sinon la construction des Composants ne sera pas possible")
        while siIdeBdsEnCours():
            time.sleep(1)
        os.system("color 0F")


def checkVarEnv(cle: str, val_comp: str=None, force: bool=True):

    def verif(rep:Path):
        if rep:
            if (not (rep.is_dir())):
                raise Exception(
                    f"La veleur de la variable env. {cle} reference un repertoire {str(rep)} qui n'est pas defini.")
        else:
            raise Exception(f" La variable environement {cle} n'est pas de valeur.")


    def resolv(rep_str:str):
        if rep_str:
            return Path(CmdRad().ResolutionEnv(rep_str))
        return None

    def getval_path():
        if not cle:
            raise Exception("checkVarEnv : il faut une cle")

        rep =None
        try:
            rep= CmdRad()[cle]
        except:
            pass
        return resolv(rep)

    def setval_path(rep:Path):
        rep_str=""
        if rep:
            rep_str= str(rep)
        CmdRad()[cle] = rep_str


    #init conditions
    rep_comp= None
    if not val_comp:
        force=False
    else:
        rep_comp=resolv(val_comp)

    rep_force=None

    rep= getval_path()
    if rep:
        if rep_comp and (rep != rep_comp):
            if force:
                rep_force=rep_comp
            else:
                raise Exception(
                    f" La variable environement {cle} n'est pas la bonne valeur;  attendu: {rep_comp}, valeur:{rep} ")
    else:
        if force:
            rep_force = rep_comp
        else:
            raise Exception(f" La variable environnement {cle} n'est pas défini.")

    if rep_force :
        verif(rep_force)
        print( f"Valeur force: La variable d'environement {cle} n'est pas la bonne valeur;  attendu: {rep_force}, valeur:{rep} ")
        rep=rep_force
        setval_path(rep)
    else:
        verif(rep)

    return rep


def versiontuple(v):
    return tuple(map(int, (v.split("."))))

def rxbuild_minimum_requis(version:str):
    t_version_requis=versiontuple(version)
    t_version_courante=versiontuple(__version__)
    if t_version_courante < t_version_requis:
        raise  Exception(f"la version rxbuilder doit être mise à jour ; requis :{version} courante:{__version__}  ")

def suppression_repertoire(rep: Path):
    if rep.is_dir():
        rmtree(str(rep))
        print("del :", rep)

