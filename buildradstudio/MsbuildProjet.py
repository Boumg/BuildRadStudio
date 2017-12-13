#-*- coding: utf-8 -*-
import clr
from  Microsoft.Build.Evaluation import Project

from  .IdProjet import IdProjet


class ProjetMsbuild(object):
    """description of class"""
    def __init__(self, id : IdProjet) :
        self.Id = id
    @property
    def _MsProjet(self):
        return  self.Id._MsProjet

    @_MsProjet.setter
    def _MsProjet(self, value):
        self.Id._MsProjet = value
        
    @property
    def MsProjet(self):
        if self._MsProjet == None :
           # self.old = os.environ.copy()
           # BuildProjets.Cmd.miseAjourEnv(os.environ)
           # if not(self.siProjetDejaEvalue(self._pathProjet)):
           nom=self.Id.NomComplet
           self._MsProjet = Project(nom) #,self.PropertyExternes
           # listeProjetEvalue.append([self._pathProjet,self._MsProjet])
           # self.RevalueProjectMsBuild()     
           self._PropXml ={ item.Name : item.EvaluatedValue for item in self._MsProjet.AllEvaluatedProperties }
        return  self._MsProjet



