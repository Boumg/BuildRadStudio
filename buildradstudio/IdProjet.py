# -*- coding: utf-8 -*-
from enum import Enum
from pathlib import Path

__all__ = ["IdProjet", "ExtRadStudioProjet"]


class ExtRadStudioProjet(Enum):
    CPP = "cbproj"
    DEPLOY = "deployproj"
    DELPHIP = "dproj"
    GROUP = "groupproj"

    @classmethod
    def getEext(self, fichier):
        """
         retour le type de fichier msbuild,
         sinon une erreur si le fichier n'est pas msbuild
        """
        fic = Path(fichier.lower())
        ext = fic.suffix[1:]
        if ext[-4:] != "proj":
            raise Exception("Le fichier n'est pas de type msbuild , ", fichier)
        trouve = None
        for e in ExtRadStudioProjet:
            if ext == e.value:
                trouve = e
                break
        if not trouve:
            raise Exception("Le fichier n'est pas de type Rad Studio , ", fichier)
        return trouve


class IdProjet(object):
    """description of class"""

    def __init__(self, repertoire, projet=None, platform="win64", config="release"):
        self._NomComplet = Path()
        _nomComplet = Path()
        if repertoire:
            _nomComplet = Path(repertoire)
        if projet:
            _nomComplet = _nomComplet / Path(projet)
        self.NomComplet=_nomComplet
        self._Platform=platform
        self._Config=config


    def Verifier(self):
        if not (self._NomComplet.exists() and self._NomComplet.is_file()):
            raise Exception(f" Le fichier {self._NomComplet.expanduser()} n'existe pas")

    @property
    def NomComplet(self) -> Path:
        return self._NomComplet

    @NomComplet.setter
    def NomComplet(self, value):
        self._NomComplet = value
        self.Verifier()

    @property
    def NomCompletStr(self) -> Path:
        return str(self._NomComplet)

    @property
    def Repertoire(self):
        return self._NomComplet.parent

    """
    @Repertoire.setter
    def Repertoire(self, value):
        Repertoire = Path(value)
        if not Repertoire.is_dir():
            raise Exception(f" Le repertoire {Repertoire} n'existe pas"
        self._nomComplet =  Repertoire = Path(value)
    """

    @property
    def ProjetXml(self):
        return self._NomComplet.name

    """

    @ProjetXml.setter
    def ProjetXml(self, value):
        self._ProjetExt = ExtRadStudioProjet.getEext(value)
        self._ProjetXml = value
        self._MsProjet = None
    """

    @property
    def ProjetExt(self) -> str:
        return ExtRadStudioProjet.getEext(self.ProjetXml)

    @property
    def Platform(self) -> str:
        return self._Platform.title()

    @property
    def Config(self) -> str:
        return self._Config.title()
