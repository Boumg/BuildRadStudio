# -*- coding: utf-8 -*-
"""
 Gestion des builds de l'environenement  Rad Studio
  - Permet d'enregistre automatiquement les packages d'IDE
  - Gestion multi-plateformes multi-configuration
"""

__version__ = "0.0.1"
__all__ = ['rxbuild', "checkVarEnv", "attenteArretBds"]
from pathlib import Path
from .TypeProjet import Target,RXSuffix
from .Options import OptionBuild
from .CmdRad import CmdRad
from .Process import Process
from .IdProjet import IdProjet

from .MsbuildProjet import ProjetMsbuild
from .VerifAvantCompilation import attenteArretBds, checkVarEnv

def ListeSelctionFichiers(pattern):
    return [str(f) for f in Path().glob("*.{pattern.value}")]

def ListeProjets():
    return ListeSelctionFichiers(RXSuffix.CPP.value) + ListeSelctionFichiers(RXSuffix.DELPHIP)

def ListeGroupOuProjets():
    li=ListeSelctionFichiers(RXSuffix.GROUP)
    if  li:
        return li;
    return ListeProjets;

def rxbuildProjet(id: IdProjet, option: OptionBuild):
    if id.siGroup:
        with ProjetMsbuild(id) as gr:
            for e in gr.sous_projets():
                p = Process(IdProjet(id.Repertoire / e))
                p.actions(option)
    elif id.siProjetCppOrPas:
        p = Process(id)
        p.actions(option)


def rxbuild(racine=None, groupes=[], options=None):
    try:
        option = OptionBuild(options)
    except  Exception as e:
        print(e)
        exit(3)
    if Target.INSTALL in option.Targets or Target.UNINSTALL in option.Targets:
        # il n'est pas possible d'(de)installer avec Ide ouvert
        attenteArretBds()
    if racine:
        option.Racine = CmdRad().ResolutionEnv(racine)
    option.AddProjets(groupes)
    #Recherche des fichiers projets sous le repertoire courant
    if not option.Projets:
        option.AddProjets( ListeGroupOuProjets())

    # Type de projets/ packages
    for f in option.Projets:
        rxbuildProjet(IdProjet(option.Racine, f), option)


if __name__ == "__main__":
    rxbuild()
