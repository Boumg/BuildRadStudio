# -*- coding: utf-8 -*-
"""
 Gestion des builds de l'environenement  Rad Studio
  - Permet d'enregistre automatiquement les packages d'IDE
  - Gestion multi-plateformes multi-configuration
"""

__version__ = "0.1.6"
__all__ = ['rxbuild', "checkVarEnv", "attenteArretBds", "Cde", "CdeRad", "CmdDef", "CmdRad",
           "suppression_repertoire", "get_cmake_cde","BuildCmakeVS", "CtestCmakeVS", "rxbuild_minimum_requis"
           ]
from pathlib import Path

from os import getcwd
from sys import argv

from .TypeProjet import Target, RXSuffix, Phase1Projets, Phase2Projets, Phase3Projets
from .Options import OptionBuild
from .CmdRad import CmdRad, Cde, CdeRad, CmdDef
from .Process import Process
from .IdProjet import IdProjet

from .MsbuildProjet import ProjetMsbuild
from .VerifAvantCompilation import attenteArretBds, checkVarEnv, suppression_repertoire, \
    rxbuild_minimum_requis
from .cmake_util import  get_cmake_cde, BuildCmakeVS, CtestCmakeVS


def ListeSelctionFichiers(pattern):
    c = Path.cwd()
    return [str(f) for f in c.glob(f"*.{pattern.value}")]


def ListeProjets():
    return ListeSelctionFichiers(RXSuffix.CPP) + ListeSelctionFichiers(RXSuffix.DELPHIP)


def ListeGroupOuProjets():
    li = ListeSelctionFichiers(RXSuffix.GROUP)
    if li:
        return li
    return ListeProjets()


def ParcoursGroup(groupe, idProj: IdProjet, option: OptionBuild):
    for e in groupe:
        p = Process(IdProjet(idProj.Repertoire / e))
        p.actions(option)


def rxbuildProjet(id: IdProjet, option: OptionBuild):
    if id.siGroup:
        with ProjetMsbuild(id) as gr:
            groupe = gr.sous_projets()
            typesprojets = option._TypeProjets
            # print("typesprojets",typesprojets)

            # phase 1
            option._TypeProjets = [v for v in Phase1Projets if v in typesprojets]
            # print("phase 1",option._TypeProjets)
            ParcoursGroup(groupe, id, option)

            # phase 2
            option._TypeProjets = [v for v in Phase2Projets if v in typesprojets]
            # print("phase 2",option._TypeProjets)
            ParcoursGroup(groupe, id, option)

            # phase 3
            option._TypeProjets = [v for v in Phase3Projets if v in typesprojets]
            # print("phase 3",option._TypeProjets)
            ParcoursGroup(groupe, id, option)

            option._TypeProjets = typesprojets

    elif id.siProjetCppOrPas:
        p = Process(id)
        p.actions(option)


def rxbuild(racine=None, groupes=[], options=None, lignecde=True):
    argligne= ""
    option = None
    if lignecde:
        argligne = argv[1:]
    try:
        option = OptionBuild(options, argligne)
    except Exception as e:
        print(e)
        exit(3)

    if racine:
        option.Racine = CmdRad().ResolutionEnv(racine)
    else:
        option.Racine = getcwd()

    if Target.INSTALL in option.Targets or Target.UNINSTALL in option.Targets:
        # il n'est pas possible d'(de)installer avec Ide ouvert
        attenteArretBds()

    option.AddProjets(groupes)
    # Recherche des fichiers projets sous le repertoire courant
    if not option.Projets:
        li = ListeGroupOuProjets()
        option.AddProjetsListe(li)

    # Type de projets/ packages
    for f in option.Projets:
        rxbuildProjet(IdProjet(option.Racine, f), option)


if __name__ == "__main__":
    rxbuild()
