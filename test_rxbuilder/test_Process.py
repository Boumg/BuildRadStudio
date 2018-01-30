#-*- coding: utf-8 -*-

import unittest
from jeux_rxbuilder import *
from rxbuilder.Process import *
from rxbuilder.IdProjet import IdProjet 

class TestProcess(unittest.TestCase):
    def testCleanProjetLib(self) :
        proc = Process(IdProjet(LibProjet))
        # m=MsMake(Process.Cmd)
        # for platefrom in ["win32", "win64"]:
        #      for debug in ["release", "debug"]:
        #         f._Platform=platefrom
        #         f._Config=debug
        #         m.Process(f)

if __name__ == '__main__':
    unittest.main()
