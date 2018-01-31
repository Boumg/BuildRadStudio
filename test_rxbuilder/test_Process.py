#-*- coding: utf-8 -*-

import unittest
from jeux_rxbuilder import *
from rxbuilder.Process import *
from rxbuilder.IdProjet import IdProjet
from rxbuilder.Options import OptionBuild

class TestProcess(unittest.TestCase):
    def testCleanProjetLib(self) :
        proc = Process(IdProjet(LibProjet))
        proc.actions(OptionBuild(" --clean --win32 -r"))
        proc.actions(OptionBuild(" --clean --win64 -d"))

if __name__ == '__main__':
    unittest.main()
