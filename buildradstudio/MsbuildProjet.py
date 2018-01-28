# -*- coding: utf-8 -*-
import os

import clr
from Microsoft.Build.Evaluation import Project, ProjectCollection
from .TypeProjet import *
from .IdProjet import IdProjet

"""
 Mise a jour avec l'env. Rad Studio
"""
from .CmdRad import CmdRad

CmdRad().miseAjourEnv(os.environ)


class ProjetMsbuild(object):
    """description of class"""
    _ProjectCollection = ProjectCollection()

    def afficheProp(self):
        print("*******************************")
        print("projets :", self.Id.NomCompletStr)
        print("*******************************")
        for k, v in self.PropXml.items():
            print(f"{k:<35} =", v)

    def RevalueProjectMsBuild(self):
        if self.Id.siProjetCppOrPas:
            self._MsProjet.SetGlobalProperty("Platform", self.Id.Platform.value)
            self._MsProjet.SetGlobalProperty("Config", self.Id.Config.value)
        self._MsProjet.ReevaluateIfNecessary()

    def load(self):
        if not self._MsProjet:
            self._MsProjet = self._ProjectCollection.LoadProject(self.Id.NomCompletStr)
        self.RevalueProjectMsBuild()

    def unLoad(self):
        self._ProjectCollection.UnloadProject(self._MsProjet)

    def __init__(self, id: IdProjet):
        self._PropXml = None
        self._MsProjet = None
        self.Id = id
        self.load()

    def __enter__(self):
        self.load()
        return self

    def __exit__(self, type, value, traceback):
        self.unLoad()

    @property
    def PropXml(self):
        if not self._PropXml:
            self._PropXml = {item.Name: item.EvaluatedValue for item in self._MsProjet.AllEvaluatedProperties}
        return self._PropXml

    def sous_projets(self):
        return [pp.EvaluatedInclude for pp in self._MsProjet.AllEvaluatedItems if pp.ItemType == "Projects"]

    @property
    def FinalOutput(self):
        return self.PropXml["FinalOutput"]

    # TODO Path
    @property
    def FinalOutputName(self):
        return os.path.split(self.FinalOutput)[1]

    # TODO Path
    @property
    def ExtFinalOutput(self):
        return os.path.splitext(self.FinalOutput)[1][1:]

    @property
    def estExe(self):
        return self.ExtFinalOutput == "exe"

    @property
    def estLib(self):
        return self.ExtFinalOutput == "lib" or self.ExtFinalOutput == "a"

    @property
    def estPackage(self):
        return not self.estExe and not self.estLib

    @property
    def siDesignOnlyPackage(self):
        return "DesignOnlyPackage" in self.PropXml and self.PropXml["DesignOnlyPackage"] == "true"

    @property
    def siRuntimeOnlyPackage(self):
        return "RuntimeOnlyPackage" in self.PropXml and self.PropXml["RuntimeOnlyPackage"] == "true"

    @property
    def siDesignAndExePackage(self):
        return not self.siDesignOnlyPackage and not self.siRuntimeOnlyPackage and self.estPackage

    @property
    def SanitizedProjectName(self):
        return self._PropXml["SanitizedProjectName"]

    @property
    def siTest(self):
        return self.SanitizedProjectName.upper().find("TEST") != -1

    @property
    def typeProjet(self) -> TypeProjet:
        if self.siRuntimeOnlyPackage or self.siDesignAndExePackage:
            return TypeProjet.PackageExe
        if self.siDesignOnlyPackage:
            return TypeProjet.PackageIde
        if self.siTest:
            return TypeProjet.Test
        if self.estLib:
            return TypeProjet.Librairie
        return TypeProjet.Application
