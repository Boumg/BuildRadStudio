# -*- coding: utf-8 -*-

import clr
from System.Diagnostics import Process
from pathlib import Path
import time
import os
from rxbuilder.CmdRad import CmdRad

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


def checkVarEnv(varName: str, val_comp= None):
    var = os.environ.get(varName)
    if not var:
        raise Exception(f" La variable environnement {varName} n'est pas défini.")
    rep= Path(CmdRad().ResolutionEnv(var))
    if rep:
        if (not (rep.is_dir())):
            raise Exception(f"La veleur de la variable env. {varName} reference un repertoire {rep} qui n'est pas defini.")
    else:
        raise Exception(f" La variable environement {varName} n'est pas de valeur.")
    if val_comp:
        rep_comp=Path( CmdRad().ResolutionEnv(val_comp))
        if rep != rep_comp:
            raise Exception(f" La variable environement {varName} n'est pas la bonne valeur;  attendu: {val_comp}, valeur:{rep} ")

    return True