#-*- coding: utf-8 -*-

import unittest
from jeux import *
from buildradstudio.Options import *

class TestOptions(unittest.TestCase):
    def test_AjoutProjet(self):
        opt = OptionBuild("toto.prj")
        listeComposants = [
            (r'gtestmock\radstudio', "ggmock_group.groupproj"),
            (r'ComPort-4.14\XE', "CPort.groupproj"),
            (r'AsyncPro-1.0\xe', "Delphi.groupproj"),
            (r'SpTBXLib\xe', "sptbxLib.groupproj"),
            (r'tdbf\xe\Delphi101', "tdbf101.groupproj"),
            (r'rapidxml-1.13\xe', "RapidXmlGroup.groupproj"),
            (r'McoXml\xe', "McoXmlGroup.groupproj"),
            (r'McoDebug\xe', "McoDebugGroup.groupproj"),
            (r'Mcobdd\xe', "McoBddGroup.groupproj"),
            (r'ConfigInit\xe', "ConfigInit.groupproj"),
            (r'Utils\xe', "UtilsComposants.groupproj")

        ]
        opt.AddProjets(listeComposants)
        self.assertEqual(len(opt.Projets),12 )

    def test_erreur(self):
        self.assertRaises(Exception,OptionBuild,"--merde")



    def test_something(self):
        commande=str(LibProjet)
        opt=OptionBuild(commande)

        self.assertEqual(opt.Plateformes, tuple(ToutesPlateformes))
        self.assertEqual(opt.Configs, tuple(ToutesConfigs))
        self.assertEqual(opt.Targets, tuple(TousTargets))
        a=opt.Projets
        #self.assertEqual(opt.Projets[0], tuple(TousTargets))

if __name__ == '__main__':
    unittest.main()
