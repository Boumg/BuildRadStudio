#-*- coding: utf-8 -*-
import unittest
from rxbuilder.Embarcadero import *


class TestEmbarcadero(unittest.TestCase):
    def test_getDerniereVersion(self):
        e = Embarcadero() 
        print(e.getVersions())
        print(e.getDerniereVersion())
        print(e.RootDir)
        print(e.Bin)
        print(e.getrsvars())

nomPackage = "PLB.BPL"

class TestEcritureSuppressionValeur(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.e = Embarcadero()

    @classmethod
    def tearDownClass(cls):
         c = cls.e.getRucheBDS.get_registre("Known Packages")
         c.effacer_valeur_si_existe(nomPackage)

    def test_writedelv(self):
        e = Embarcadero()
        c = e.getRucheBDS.get_registre("Known Packages")
                
        self.assertFalse(c.si_existe_valeur(nomPackage))
        c.set_valeur(nomPackage, "toto")
        self.assertTrue(c.si_existe_valeur(nomPackage))
        c.effacer_valeur(nomPackage)
        self.assertFalse(c.si_existe_valeur(nomPackage))
        
       
class TestCheckPresencePath(unittest.TestCase):        
    chaineTest = "PLB"
    @classmethod
    def setUpClass(cls):
        cls.e = Embarcadero()

    @classmethod
    def tearDownClass(cls):
        cls.nettoie(subKeyWin32,inclPath)
        cls.nettoie(subKeyWin32,libPath)
        cls.nettoie(subKeyWin32,inclPath_Clang32)
        cls.nettoie(subKeyWin32,libPath_Clang32)
        cls.nettoie(subKeyWin64,inclPath)
        cls.nettoie(subKeyWin64,libPath)

    @classmethod
    def nettoie(cls,subkey_name,value_name):
        cle = cls.e.getRucheBDS.get_registre(subkey_name)
        valeurs = cle.lister_valeurs(value_name)
        if (cls.chaineTest in valeurs):
            valeurs.remove(cls.chaineTest)
            cle.set_valeur(value_name, ";".join(valeurs))

    
    def test_presence(self):

        self.assertTrue(self.e.checkIncludeRegWin32("$(BDSCOMMONDIR)\\hpp\\Win32") or self.e.checkIncludeRegWin32CLang("$(BDSCOMMONDIR)\\hpp\\$(Platform)"))
        self.assertTrue(self.e.checkIncludeRegWin32CLang("$(BDSCOMMONDIR)\\hpp\\Win32") or self.e.checkIncludeRegWin32CLang("$(BDSCOMMONDIR)\\hpp\\$(Platform)"))
        self.assertTrue(self.e.checkIncludeRegWin64("$(BDSCOMMONDIR)\\hpp\\Win64") or self.e.checkIncludeRegWin32CLang("$(BDSCOMMONDIR)\\hpp\\$(Platform)"))
        self.assertTrue(self.e.checkAddLibRegWin32("$(BDSLIB)\\win32\\release"))
        self.assertTrue(self.e.checkAddLibRegWin32CLang("$(BDSLIB)\\win32c\\release"))
        self.assertTrue(self.e.checkAddLibRegWin64("$(BDSLIB)\\win64\\release"))
        
    def test_absenceAjout(self):

        self.assertFalse(self.e.checkIncludeRegWin32(self.chaineTest))
        self.assertFalse(self.e.checkIncludeRegWin32CLang(self.chaineTest))
        self.assertFalse(self.e.checkIncludeRegWin64(self.chaineTest))

        self.assertFalse(self.e.checkAddLibRegWin32(self.chaineTest))
        self.assertTrue(self.e.checkIncludeRegWin32(self.chaineTest))

        self.assertFalse(self.e.checkAddLibRegWin32CLang(self.chaineTest))
        self.assertTrue(self.e.checkIncludeRegWin32CLang(self.chaineTest))

        self.assertFalse(self.e.checkAddLibRegWin64(self.chaineTest))
        self.assertTrue(self.e.checkIncludeRegWin64(self.chaineTest))


if __name__ == '__main__':
    unittest.main()