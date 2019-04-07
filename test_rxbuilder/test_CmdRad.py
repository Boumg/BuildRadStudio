#-*- coding: utf-8 -*-


import unittest

from rxbuilder.CmdRad import CmdRad,Cde,CdeRad

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

class TestCmd(unittest.TestCase):
    def test_fctcde(self):
       Cde("dir")
       Cde("dir", "c:\\")

    def test_fctcdeRad(self):
       CdeRad("dir")
       CdeRad("dir", "c:\\")



if __name__ == '__main__':
     unittest.main()
