# -*- coding: utf-8 -*-

import unittest
from jeux_rxbuilder import *
from rxbuilder.MsbuildProjet import ProjetMsbuild
from rxbuilder.IdProjet import IdProjet


class TestMsProjet(unittest.TestCase):

    def testGroup(self):
        with ProjetMsbuild(IdProjet(GroupProjet)) as ms:
            ms.afficheProp()

    def testLib(self):
        with  ProjetMsbuild(IdProjet(LibProjet)) as ms:
            ms.afficheProp()

    def testSousProjets(self):
        with  ProjetMsbuild(IdProjet(GroupProjet)) as ms:
            sousprojet = ms.sous_projets()
            self.assertEqual(len(sousprojet), 5)

    def testSousProjets2(self):
        with  ProjetMsbuild(IdProjet(GroupProjet)) as ms:
            sousprojet = ms.sous_projets()
            self.assertEqual(len(sousprojet), 5)

    def testPropPackageIdeProjet(self):
        with  ProjetMsbuild(IdProjet(PackageIdeProjet)) as ms:
            self.assertTrue(ms.siDesignOnlyPackage)
            self.assertFalse(ms.siRuntimeOnlyPackage)
            self.assertFalse(ms.siDesignAndExePackage)

    def testPropPackageExecProjet(self):
        with ProjetMsbuild(IdProjet(PackageExecProjet))as ms:
            self.assertFalse(ms.siDesignOnlyPackage)
            self.assertTrue(ms.siRuntimeOnlyPackage)
            self.assertFalse(ms.siDesignAndExePackage)

    def testPropLibProjet(self):
        with ProjetMsbuild(IdProjet(LibProjet)) as ms:
            ms.afficheProp()
            self.assertFalse(ms.siDesignOnlyPackage)
            self.assertFalse(ms.siRuntimeOnlyPackage)
            self.assertFalse(ms.siDesignAndExePackage)

    def testPropExecProjet(self):
        with ProjetMsbuild(IdProjet(ExecProjet)) as ms:
            self.assertFalse(ms.siDesignOnlyPackage)
            self.assertFalse(ms.siRuntimeOnlyPackage)
            self.assertFalse(ms.siDesignAndExePackage)


if __name__ == '__main__':
    unittest.main()
