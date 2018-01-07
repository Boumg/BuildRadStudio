#-*- coding: utf-8 -*-

from context import *
from buildradstudio.Process import *
from buildradstudio.IdProjet import IdProjet 

class TestProcess(unittest.TestCase):
    def testCleanProjetLib(self) :
        proc = Process(str(RepertoireJeux))
        m=MsMake(Process.Cmd)
        f=IdProjet(str(LibProjet))
        for platefrom in ["win32", "win64"]:
             for debug in ["release", "debug"]:
                f._Platform=platefrom
                f._Config=debug
                m.Process(f)

if __name__ == '__main__':
    unittest.main()
