# -*- coding: utf-8 -*-
"""
 Gestion des builds de l'environenement  Rad Studio
  - Permet d'enregistre automatiquement les packages d'IDE
  - Gestion multi-plateformes multi-configuration
"""
 
__version__ = "0.0.1"
 
from .Options import OptionBuild
from .Process import Process


def Process(racine=None, groupes=[]):
    option= OptionBuild()     
    # Type de projets/ packages  
    selecs= lambda projet  :   projet.lower() in option.TypeProjets 
    targets= lambda target :    target.lower() in option.Targets 
    plateformes= lambda plateforme :    plateforme.lower() in option.Plateformes 
    configs= lambda config :    config.lower() in option.Configs 
    properties= lambda property : property.lower() in option.Properties
    """
    for g in groupes:
        b=BuildProjet(racine,g[0],g[1] ) 
        b.processGroup(selecs, targets, plateformes, configs, properties 
    """