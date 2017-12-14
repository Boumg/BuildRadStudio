#-*- coding: utf-8 -*-
from .context import *
from buildradstudio.CmdRad import CmdRad 



class TestCmdRad(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.cmd=CmdRad()

    def test_set(self):
       self.cmd.Cde("set ")

    def test_msbuild(self):
       self.cmd.MsBuild("/help")

    def test_bcc64(self):
       self.cmd.Cde("bcc64 --help ")

    def test_msbuildErreur(self):
        self.assertRaises(Exception, self.cmd.MsBuild, " merde ")

    def test_ResolutionEnv(self):
        r=self.cmd.ResolutionEnv("%COMPUTERNAME%")
        self.assertGreater(len(r),0)
    


if __name__ == '__main__':
    unittest.main()