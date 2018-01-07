#-*- coding: utf-8 -*-
import unittest
from jeux import *
import sys
for f in sys.path:
    print(f)
#from context import *
from buildradstudio.IdProjet import * 

class TestExtRadStudioProjet(unittest.TestCase):
    def testExtension(self):
        self.assertTrue(ExtRadStudioProjet.getEext("monfichier.groupproj") == ExtRadStudioProjet.GROUP, "test type")
        with self.assertRaises(Exception):
           ExtRadStudioProjet.getEext("groupproddj")
        with self.assertRaises(Exception):
           ExtRadStudioProjet.getEext("monfichier.groupproddj") 


class TestIdProjet(unittest.TestCase):
    repertoire = RepertoireXe
    def testIdWithRepertoireAndName(self):
        groupproj = IdProjet(str(self.repertoire / "TstBuild.groupproj"))
        self.assertEqual(groupproj.NomComplet,str(self.repertoire / "TstBuild.groupproj"))
        self.assertEqual(groupproj.Repertoire,self.repertoire)
        self.assertEqual(groupproj.ProjetXml,"TstBuild.groupproj")
        self.assertEqual(groupproj.ProjetExt,ExtRadStudioProjet.GROUP)
        self.assertEqual(groupproj.Config,"Release")
        self.assertEqual(groupproj.Platform,"Win64")
    
    def testIdWithRerpertoireNone(self):
        groupproj = IdProjet(None, (self.repertoire / "TstBuild.groupproj"))
        self.assertEqual(groupproj.NomComplet,str(self.repertoire / "TstBuild.groupproj"))
        self.assertEqual(groupproj.Repertoire,self.repertoire)
        self.assertEqual(groupproj.ProjetXml,"TstBuild.groupproj")
        self.assertEqual(groupproj.ProjetExt,ExtRadStudioProjet.GROUP)
        self.assertEqual(groupproj.Config,"Release")
        self.assertEqual(groupproj.Platform,"Win64")

if __name__ == '__main__':
    unittest.main()