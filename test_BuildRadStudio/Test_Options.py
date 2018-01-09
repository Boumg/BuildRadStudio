#-*- coding: utf-8 -*-

import unittest
from jeux import *
from buildradstudio.Options import OptionBuild
"""
    @property
    def TypeProjets(self):
         return self._TypeProjets
    @property
    def Plateformes(self):
        return tuple(self._Plateformes)
    @property
    def Configs(self):
        return tuple(self._Configs)
    @property
    def Targets(self):
        return  tuple(self._Targets)
    @property
    def Properties(self):
        return  tuple(self._Properties)
    @property
    def Projets(self):
        return  tuple(self._projets)

"""
class TestOptions(unittest.TestCase):
    def test_something(self):
        commande=str(LibProjet)
        opt=OptionBuild(commande)

        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
