import unittest
import os
from jeux_rxbuilder import *
from rxbuilder import rxbuild

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
    #@unittest.skip("demonstrating skipping")
    def test_cleanWin32Release(self):
        opt = f"--clean --win32 -r {LibProjet} "
        rxbuild(options=opt,lignecde=False)

    #@unittest.skip("demonstrating skipping")
    def test_cleanRelease(self):
        opt = f"--clean -r {LibProjet}"
        rxbuild(options=opt,lignecde=False)

    #@unittest.skip("demonstrating skipping")
    def test_cleanAll(self):
        opt = f"--clean  {LibProjet}"
        rxbuild(options=opt,lignecde=False)

    #@unittest.skip("demonstrating skipping")
    def test_CleanGroup(self):
        opt = f" --clean  {GroupProjet}"
        rxbuild(options=opt,lignecde=False)

    #@unittest.skip("demonstrating skipping")
    def test_Build_Win32Release(self):
        opt = f"--build --win64 -r {LibProjet}"
        rxbuild(options=opt,lignecde=False)

    #@unittest.skip("demonstrating skipping")
    def test_BuildLib(self):
        opt = f"--build  {LibProjet}"
        rxbuild(options=opt,lignecde=False)

    #@unittest.skip("demonstrating skipping")
    def test_BuildInstall(self):
        opt = f"  -i -r {PackageIdeProjet}"
        rxbuild(options=opt,lignecde=False)

    #@unittest.skip("demonstrating skipping")
    def test_BuildUnInstall(self):
        opt = f"  -u -r {PackageIdeProjet}"
        rxbuild(options=opt,lignecde=False)

    #@unittest.skip("demonstrating skipping")
    def test_Build_release_win64(self):
        opt = f"  -r --win64 {GroupProjet}"
        rxbuild(options=opt,lignecde=False)

    #@unittest.skip("demonstrating skipping")
    def test_LancementTest(self):
        opt = f" --build --test  --valide -r --win64 {GroupProjet}"
        rxbuild(options=opt,lignecde=False)


    # def test_CleanGroup(self):
    #     listeComposants = [
    #         (r'gtestmock\radstudio', "ggmock_group.groupproj")
    #         #    (r'ComPort-4.14\XE',"CPort.groupproj"),
    #         #     (r'AsyncPro-1.0\xe',"Delphi.groupproj"),
    #         #     (r'SpTBXLib\xe',"sptbxLib.groupproj"),
    #         #     (r'tdbf\xe\Delphi101',"tdbf101.groupproj"),
    #         #     (r'rapidxml-1.13\xe',"RapidXmlGroup.groupproj"),
    #         #     (r'McoXml\xe',"McoXmlGroup.groupproj"),
    #         #     (r'McoDebug\xe',"McoDebugGroup.groupproj"),
    #         #     (r'Mcobdd\xe',"McoBddGroup.groupproj"),
    #         #     (r'ConfigInit\xe',"ConfigInit.groupproj"),
    #         #     (r'Utils\xe',"UtilsComposants.groupproj")
    #
    #     ]
    #
    #     ProcessMain("%COMPOSANTS%", listeComposants, " --clean  ")

class TesLigneCde(unittest.TestCase):
    @unittest.skip("demonstrating skipping")
    def test_vide(self):
        os.chdir(str(RepertoireXe))
        rxbuild(lignecde=False)

    @unittest.skip("demonstrating skipping")
    def test_Racinevide(self):
        os.chdir(str(RepertoireXe))
        print("test_Racinevide")
        print(str(RepertoireXe))
        print(os.getcwd())
        opt = f" --valide -r --win64 Test_tst\Test_tst.cbproj"
        rxbuild(options=opt,lignecde=False)



if __name__ == '__main__':
    unittest.main()
