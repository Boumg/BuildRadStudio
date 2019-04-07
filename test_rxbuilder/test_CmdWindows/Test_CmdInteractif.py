import unittest
from pathlib import Path
from rxbuilder.CmdWindows import InteractiveCmd


class InteractiveCommand(unittest.TestCase):

    def test_creation_et_sortie(self):
        with InteractiveCmd() as p:
            print("ok prompt")
            p.sortie()


    def test_creation_avec_path(self):
        with InteractiveCmd(Path().resolve()) as p:
            p.send_line("dir")
            r = str(Path().resolve()).replace("\\", "\\\\")
            print(r)
            p.expect(r)

    def test_creation_avec_path2(self):
        with InteractiveCmd(Path().resolve()) as p:
            p.send_line("dir")
            r = str(Path().resolve().parent).replace("\\", "\\\\")
            print(r)
            p.expect(r)

    def test_creation(self):
        with InteractiveCmd() as p:
            print("ok prompt")



    def test_dirs(self):
        with InteractiveCmd() as p:
            p.cde("dir")
            p.cde("dir")
            self.assertTrue(p.is_alive())

    def test_sortie(self):
        with InteractiveCmd() as p:
            self.assertTrue(p.is_alive())
            p.sortie()
            self.assertFalse(p.is_alive())


    def test_kill(self):
        p = InteractiveCmd()
        p.kill()



if __name__ == '__main__':
    unittest.main()
