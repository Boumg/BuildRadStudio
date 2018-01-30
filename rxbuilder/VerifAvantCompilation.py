# -*- coding: utf-8 -*-

import clr
from System.Diagnostics import Process
import time
import os

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


def checkVarEnv(varName: str) -> bool:
    var = os.environ.get(varName)
    return var and os.path.exists(var)
