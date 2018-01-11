# -*- coding: utf-8 -*-
"""
 Gestion des builds de l'environenement  Rad Studio
  - Permet d'enregistre automatiquement les packages d'IDE
  - Gestion multi-plateformes multi-configuration
"""
 
__version__ = "0.0.1"
 
from .Options import OptionBuild
from .Process import Process
from .IdProjet import IdProjet

def Process(racine=None, groupes=[], options=None):
    option= OptionBuild(options)
    # Type de projets/ packages  
    selecs= lambda projet  :   projet.lower() in option.TypeProjets 
    targets= lambda target :    target.lower() in option.Targets 
    plateformes= lambda plateforme :    plateforme.lower() in option.Plateformes 
    configs= lambda config :    config.lower() in option.Configs 
    properties= lambda property : property.lower() in option.Properties
    for f in option.Projets:
        id=IdProjet(racine, f)


    """
    for g in groupes:
        b=BuildProjet(racine,g[0],g[1] ) 
        b.processGroup(selecs, targets, plateformes, configs, properties 
    """
"""
def processGroup(self, PredicatSelec, _Predicattarget, Predicatplateforme, Predicatconfig, PredicatProperty ) :
    self._PredicatSelec=PredicatSelec
    self.checkPredicatProperty(PredicatProperty)
    for  p in self.Platforms :
      for c in self.Configs :
          if Predicatconfig(c) and  Predicatplateforme(p):                 
             for ssproj in self.BuildSousProjets(p,c):
                if PredicatSelec(ssproj.TypeProjet):
                        ssproj.process( _Predicattarget , PredicatProperty )
"""