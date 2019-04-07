# -*- coding: utf-8 -*-
from subprocess import run, PIPE
from pathlib import Path
from .TypeProjet import *
from .MsbuildProjet import ProjetMsbuild
from .CmdRad import CmdRad
from .Embarcadero import Embarcadero
from .IdProjet import IdProjet
from .Options import OptionBuild

from os import remove

from shutil import rmtree

def si_gtest(test: Path):
    cde=test.name + " --help"
    r=run(cde,shell=True, stdout=PIPE, cwd=str(test.parent))
    return  r.stdout.find(b"Google Test") != -1

def SuppressionRepertoireId(id: IdProjet ):
    rep = id.Repertoire / id.Platform.value / id.Config.value
    if rep.is_dir():
      rmtree(str(rep))
      print("del :", rep)


def SuppressionFichier(ext: str, id: IdProjet):
    for fic in id.Repertoire.rglob(f"*.{ext}"):
        print("suppression :", fic)
        remove(str(fic))



class Process(object):
    def clean(self, id: IdProjet):
        CmdRad().cwd = str(id.Repertoire)
        print(f"{id.NomCompletStr} /t:Clean /p:Config={id.Config.value} /p:Platform={id.Platform.value}")
        CmdRad().MsBuild(f"{id.NomCompletStr} /t:Clean /p:Config={id.Config.value} /p:Platform={id.Platform.value}")
        SuppressionFichier("stat", id)
        SuppressionFichier("local", id)
        SuppressionFichier("identcache", id)
        SuppressionRepertoireId(id)



    def Make(self, id: IdProjet):
        if self.siOkCompile:
            CmdRad().cwd = str(id.Repertoire)
            CmdRad().MsBuild(f"{id.ProjetXml} /t:Make /p:Config={id.Config.value} /p:Platform={id.Platform.value}")

    def Build(self, id: IdProjet):
        if self.siOkCompile:
            CmdRad().cwd = str(id.Repertoire)
            CmdRad().MsBuild(f"{id.ProjetXml} /t:build  /p:Config={id.Config.value} /p:Platform={id.Platform.value}")

    def ReBuild(self, id: IdProjet):
        if self.siOkCompile:
            CmdRad().cwd = str(id.Repertoire)
            CmdRad().MsBuild(f"{id.ProjetXml}  /t:ReBuild  /p:Config={id.Config.value} /p:Platform={id.Platform.value}")

    def Install(self, id: IdProjet):
        if self.siOkdIde:
            print("enregistrePackage:", self.FinalOutput)
            rucheKnownPackage = Embarcadero().getRegistreBDS("Known Packages")
            rucheKnownPackage.set_valeur(self.FinalOutput, self.SanitizedProjectName)
            self.clearCaches(self.FinalOutputName)

    def UnInstall(self, id: IdProjet):
        if self.siOkdIde:
            print("desEnregistrePackage:", self.FinalOutput)
            rucheKnownPackage = Embarcadero().getRegistreBDS("Known Packages")
            rucheKnownPackage.effacer_valeur_si_existe(self.FinalOutput)
            self.clearCaches(self.FinalOutputName)

    def Valide(self, id: IdProjet):
        if self.siTest:
            cde=id.Repertoire / self.FinalOutput
            CmdRad().cwd = str(cde.parent)
            if si_gtest(cde):
                nom_fic=f"{cde.name}_{id.Platform.value }_{id.Config.value }"
                fic_out=self.option.Racine /  "test-reports" / nom_fic
                fic_out=fic_out.with_suffix(".xml")
                outputtest= f" --gtest_output=\"xml:{fic_out}\""
                CmdRad().Cde(cde.name + outputtest)
            else:
                #ce n'est pas un google test
                CmdRad().Cde(cde.name)

    ActionsTarget = {Target.CLEAN: clean,
                     Target.BUILD: Build,
                     Target.MAKE: Make,
                     Target.INSTALL: Install,
                     Target.UNINSTALL: UnInstall,
                     Target.TEST: Valide
                     }

    def __init__(self, id: IdProjet):
        self.Id = id
        self.Update()

    def Update(self):
        with  ProjetMsbuild(self.Id) as ms:
            self.TypeProjet = ms.typeProjet
            self.siDesignOnlyPackage = ms.siDesignOnlyPackage
            self.siDesignAndExePackage = ms.siDesignAndExePackage
            self.FinalOutputName = ms.FinalOutputName
            self.SanitizedProjectName = ms.SanitizedProjectName
            self.FinalOutput = ms.FinalOutput
            self.siTest = ms.siTest
            #ms.afficheProp()

    @property
    def siOkCompile(self):
        # pas de compilation pour les design only en Win64
        return self.Id.Platform != Plateforme.WIN64 or not self.siDesignOnlyPackage

    @property
    def siOkdIde(self):
        return self.Id.Platform == Plateforme.WIN32 and (self.siDesignAndExePackage or self.siDesignOnlyPackage)

    def clearCaches(self, nomPackage):
        ruchePackageCache = Embarcadero().getRegistreBDS("Package Cache")
        ruchePackageCache.effacer_cle(nomPackage)
        ruchePaletteCache = Embarcadero().getRegistreBDS("Palette\\Cache")
        ruchePaletteCache.effacer_cle(nomPackage)

    def actions(self, option: OptionBuild):
        self.option =option
        if self.TypeProjet in option.TypeProjets:
            for p in option.Plateformes:
                for c in option.Configs:
                    self.Id.Platform = p
                    self.Id.Config = c
                    for target in option.Targets:
                        if target in {Target.INSTALL, Target.UNINSTALL, Target.TEST}:
                            self.Update()
                        self.ActionsTarget[target](self, self.Id)
