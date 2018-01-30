# -*- coding: utf-8 -*-

from pathlib import Path

from rxbuilder import RXSuffix
from .TypeProjet import Plateforme, Config, RXSuffix

__all__ = ["IdProjet"]


class IdProjet(object):
    """description of class"""

    def __init__(self, repertoire, projet=None, platform=Plateforme.WIN64, config=Config.RELEASE):
        self._NomComplet = Path()
        _nomComplet = Path()
        if repertoire:
            _nomComplet = Path(repertoire)
        if projet:
            _nomComplet = _nomComplet / Path(projet)
        self.NomComplet = _nomComplet
        self.Platform = platform
        self.Config = config

    def Verifier(self):
        if not (self._NomComplet.exists() and self._NomComplet.is_file()):
            raise Exception(f" Le fichier {self.NomCompletStr} n'existe pas")

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
        return RXSuffix.getEext(self.ProjetXml)

    @property
    def siGroup(self) -> bool:
        return self.ProjetExt == RXSuffix.GROUP

    @property
    def siProjetCppOrPas(self) -> bool:
        return self.ProjetExt == RXSuffix.CPP or self.ProjetExt == RXSuffix.DELPHIP

