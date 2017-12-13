#-*- coding: utf-8 -*-

from context import *
import os
from buildradstudio.CmdRad import CmdRad#todo a sup
from buildradstudio.MsbuildProjet import ProjetMsbuild 
from buildradstudio.IdProjet import IdProjet 

class TestMsProjet(unittest.TestCase) :
    Cmd = CmdRad()
    Cmd.miseAjourEnv(os.environ)
    def testGroup(self):
        groupproj = IdProjet(GroupProjet)
        ms=ProjetMsbuild(groupproj)
        print(ms.MsProjet)
        for e in ms._PropXml :
            print(e)
    def testLib(self):
        lib = IdProjet(LibProjet)
        ms=ProjetMsbuild(lib)
        msb=ms.MsProjet
        print(msb)


if __name__ == '__main__':
    unittest.main()