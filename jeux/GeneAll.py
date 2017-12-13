# -*- coding: utf-8 -*-
import os,sys
dossier=os.path.expandvars("%COMPOSANTS%\\InstalleurRad")
sys.path.append(dossier) 

from embarcadero import *
   

listeComposants = [
    (r'xe',"TstBuild.groupproj")
	
    ]
dir_path = os.path.dirname(os.path.abspath(__file__))
Process(dir_path,listeComposants )


    