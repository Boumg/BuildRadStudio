#-*- coding: utf-8 -*-

from pathlib import Path

from .CmdRad import CmdRad
from .IdProjet import IdProjet

from os import remove




#listeProjetEvalue = []


def SuppressionFichier( ext : str,  projet :IdProjet):
    for fic in projet.Repertoire.glob(f"*.{ext}"): 
        print ("suppression :",fic)
        remove(str(fic)) 
       

class MsMake(object):
    """description of class"""
    def __init__(self, cmd : CmdRad) :
        self.Cmd = cmd
    def Process(self, projet :IdProjet) :
        self.Cmd.MsBuild(projet.NomCompletStr + ' /t:Clean /p:Config=' + projet.Config + ' /p:Platform=' + projet.Platform)
        SuppressionFichier("stat",projet )
        SuppressionFichier("local",projet )
        SuppressionFichier("identcache",projet )


        #Rd %COMPOSANTS%\SpTBXLib\Test\Win32 /s /q
        #Rd %COMPOSANTS%\SpTBXLib\Test\Win64 /s /q
        #del %COMPOSANTS%\SpTBXLib\Test\*.stat /f /q
        #del %COMPOSANTS%\SpTBXLib\Test\*.local /f /q
        #REM del %COMPOSANTS%\SpTBXLib\Test\*.res /f /q
        #del %COMPOSANTS%\SpTBXLib\Test\*.identcache /f /q




   


class Process(object):
    Cmd = CmdRad()   
    def __init__(self,racine):
        self.Racine = racine

    @property
    def Racine(self):
        return self._Racine
   
    @Racine.setter
    def Racine(self, value):
        self._Racine =  Path( self.Cmd.ResolutionEnv(str(value)))
        if (not(self._Racine.is_dir() )):
            raise Exception(f" Le repertoire racine {self._Racine} n'est pas defini.")



