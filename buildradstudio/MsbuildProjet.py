#-*- coding: utf-8 -*-
import clr
from  Microsoft.Build.Evaluation import Project

from  .IdProjet import IdProjet


class ProjetMsbuild(object):
    """description of class"""
    def __init__(self, id : IdProjet) :
        self._MsProjet=None
        self.Id = id

        
    @property
    def MsProjet(self):
        if self._MsProjet == None :
           # self.old = os.environ.copy()
           # BuildProjets.Cmd.miseAjourEnv(os.environ)
           # if not(self.siProjetDejaEvalue(self._pathProjet)):

           self._MsProjet = Project(self.Id.NomCompletStr) #,self.PropertyExternes
           # listeProjetEvalue.append([self._pathProjet,self._MsProjet])
           # self.RevalueProjectMsBuild()     
           self._PropXml ={ item.Name : item.EvaluatedValue for item in self._MsProjet.AllEvaluatedProperties }
        return  self._MsProjet



