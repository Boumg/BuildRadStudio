# -*- coding: utf-8 -*-
"""
 Gestion des builds de l'environenement  Rad Studio
  - Permet d'enregistre automatiquement les packages d'IDE
  - Gestion multi-plateformes multi-configuration
"""

__version__ = "0.0.1"
__all__ = ['ProcessMain']

from .Options import OptionBuild
from .CmdRad import CmdRad
from .Process import Process
from .IdProjet import IdProjet, ExtRadStudioProjet
from .MsbuildProjet import ProjetMsbuild


def Salut():
    print("Bonjour les amis")
def ProcessProjet(id: IdProjet, option: OptionBuild):
    if id.siGroup:
        with ProjetMsbuild(id) as gr:
            for e in gr.sous_projets():
                p = Process(IdProjet(id.Repertoire / e))
                p.actions(option)
    elif id.siProjetCppOrPas:
        p = Process(id)
        p.actions(option)


def ProcessMain(racine=None, groupes=[], options=None):
    option = OptionBuild(options)
    if racine:
        option.Racine = CmdRad().ResolutionEnv(racine)
    option.AddProjets(groupes)
    # Type de projets/ packages
    for f in option.Projets:
        ProcessProjet(IdProjet(option.Racine, f), option)

if __name__ == "__main__":
    ProcessMain()