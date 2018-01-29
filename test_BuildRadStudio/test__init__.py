import unittest
from jeux import *
from buildradstudio import ProcessMain

"""
    buildRadStudio(racine , list((repertoire, projet)) + ligne de cde : (option ) gourpeprojet1  gourpeprojet2
    
    forme 1
    buildRadStudio projet
        uninstall des packages win32 si packageide
        clean des configuration et des plateformes windows
        build de la plaform packages win32
            en mode debug puis release
        installation des packages win32 si packageide
        build win64 debug puis release
     forme 2
     buildRadStudio gourpeprojet
        pour tous les projet du groupe cf forme 1
    

"""


class TestProcessMax(unittest.TestCase):
    @unittest.skip("demonstrating skipping")
    def test_cleanWin32Release(self):
        opt = f"--clean --win32 -r {LibProjet}"
        ProcessMain(options=opt)

    @unittest.skip("demonstrating skipping")
    def test_cleanRelease(self):
        opt = f"--clean -r {LibProjet}"
        ProcessMain(options=opt)

    @unittest.skip("demonstrating skipping")
    def test_cleanAll(self):
        opt = f"--clean  {LibProjet}"
        ProcessMain(options=opt)

    @unittest.skip("demonstrating skipping")
    def test_Build_Win32Release(self):
        opt = f"--build --win64 -r {LibProjet}"
        ProcessMain(options=opt)

    @unittest.skip("demonstrating skipping")
    def test_BuildLib(self):
        opt = f"--build  {LibProjet}"
        ProcessMain(options=opt)

    @unittest.skip("demonstrating skipping")
    def test_BuildInstall(self):
        opt = f"  -i -r {PackageIdeProjet}"
        ProcessMain(options=opt)

    @unittest.skip("demonstrating skipping")
    def test_BuildUnInstall(self):
        opt = f"  -u -r {PackageIdeProjet}"
        ProcessMain(options=opt)

    @unittest.skip("demonstrating skipping")
    def test_BuildUnInstall(self):
        opt = f"  -r --win64 {GroupProjet}"
        ProcessMain(options=opt)

    @unittest.skip("demonstrating skipping")
    def test_LancementTest(self):
        opt = f" --build --test  --valide -r --win64 {GroupProjet}"
        ProcessMain(options=opt)

    def test_CleanGroup(self):
        opt = f" --clean  {GroupProjet}"
        ProcessMain(options=opt)


if __name__ == '__main__':
    unittest.main()
