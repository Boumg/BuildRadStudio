#-*- coding: utf-8 -*-
import unittest
from jeux_rxbuilder import *

from rxbuilder.IdProjet import * 
from rxbuilder.TypeProjet import Plateforme,Config,RXSuffix


class TestExtRadStudioProjet(unittest.TestCase):
    def testExtension(self):
        self.assertTrue(RXSuffix.getEext("monfichier.groupproj") == RXSuffix.GROUP, "test type")
        with self.assertRaises(Exception):
           RXSuffix.getEext("groupproddj")
        with self.assertRaises(Exception):
           RXSuffix.getEext("monfichier.groupproddj")


class TestIdProjet(unittest.TestCase):
    repertoire = RepertoireXe
    def testIdWithRepertoireAndName(self):
        groupproj = IdProjet(self.repertoire / "TstBuild.groupproj")
        self.assertEqual(groupproj.NomComplet,self.repertoire / "TstBuild.groupproj")
        self.assertEqual(groupproj.Repertoire,self.repertoire)
        self.assertEqual(groupproj.ProjetXml,"TstBuild.groupproj")
        self.assertEqual(groupproj.ProjetExt, RXSuffix.GROUP)
        self.assertEqual(groupproj.Config,Config.RELEASE)
        self.assertEqual(groupproj.Platform,Plateforme.WIN64)
        self.assertTrue(groupproj.siGroup)

    def testIdWithRerpertoireNone(self):
        groupproj = IdProjet(None, self.repertoire / "TstBuild.groupproj")
        self.assertEqual(groupproj.NomComplet,self.repertoire / "TstBuild.groupproj")
        self.assertEqual(groupproj.Repertoire,self.repertoire)
        self.assertEqual(groupproj.ProjetXml,"TstBuild.groupproj")
        self.assertEqual(groupproj.ProjetExt, RXSuffix.GROUP)
        self.assertEqual(groupproj.Config,Config.RELEASE)
        self.assertEqual(groupproj.Platform,Plateforme.WIN64)

if __name__ == '__main__':
    unittest.main()