#-*- coding: utf-8 -*-
from enum import Enum
from pathlib import Path


__all__=["IdProjet","ExtRadStudioProjet"] 

class ExtRadStudioProjet(Enum):
    CPP = "cbproj"
    DEPLOY = "deployproj"
    DELPHIP = "dproj"
    GROUP = "groupproj"
    @classmethod 
    def getEext(self, fichier) :
       """
        retour le type de fichier msbuild, 
        sinon une erreur si le fichier n'est pas msbuild
       """
       fic = Path(fichier.lower())
       ext = fic.suffix[1:]
       if ext[-4:] != "proj":
            raise Exception("Le fichier n'est pas de type msbuild , ", fichier)
       trouve = None
       for e in ExtRadStudioProjet :
           if ext == e.value:
               trouve = e
               break
       if not trouve :
            raise Exception("Le fichier n'est pas de type Rad Studio , ", fichier)
       return trouve
 


class IdProjet(object):
    """description of class"""

   
    def __init__(self, repertoire, projet=None, platform="win64",config="release"):
        if not projet :
            projet = Path(repertoire).name
            repertoire = str(Path(repertoire).parent)
        if not repertoire :
            repertoire = str(Path(projet).parent)
            projet = Path(projet).name

        self.Repertoire = repertoire

        self.ProjetXml = projet

        self._Platform = platform 
        self._Config = config
        nom = Path(self.NomComplet)
        if not(nom.exists() and nom.is_file()) :
            raise Exception(f" Le fichier {NomComplet.expanduser()} n'existe pas",chemin)


    @property
    def Repertoire(self):
        return self._Repertoire

    @Repertoire.setter
    def Repertoire(self, value):
        self._Repertoire = Path(value)
        if not self._Repertoire.is_dir():
            raise Exception(f" Le repertoire projet {chemin} n'est pas defini.",chemin)
 
    @property 
    def ProjetXml(self):
        return self._ProjetXml  

    @ProjetXml.setter
    def ProjetXml(self, value):
        self._ProjetExt = ExtRadStudioProjet.getEext(value)
        self._ProjetXml = value
        self._MsProjet = None

    @property
    def NomComplet(self) -> str:
        return str(self._Repertoire / self._ProjetXml)
    @property 
    def ProjetExt(self)-> str:
        return self._ProjetExt
    @property
    def Platform(self) -> str:
        return self._Platform.title()
   
    @property
    def Config(self):
        return self._Config.title()
