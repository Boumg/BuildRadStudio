import pathlib
import sys
import unittest

if __name__ == '__main__':
    path = pathlib.Path(__file__).resolve().parent.parent
    sys.path.insert(0, str(path))

from buildradstudio.VerifAvantCompilation import siProcessEnCours, AttenteArretBds, checkVarEnv


class TestVerifAvantCompilation(unittest.TestCase):

    def test_ProcessAbsent(self):
        self.assertFalse(siProcessEnCours('kkkkkkkk'))

    def test_ProcessEnCours(self):
        self.assertTrue(siProcessEnCours('svchost'))

    def test_AttenteBDE(self):
        AttenteArretBds()

    def test_existeVariableEnv(self):
        self.assertTrue(checkVarEnv("USERPROFILE"))
        self.assertFalse(checkVarEnv("PATH"))
        self.assertFalse(checkVarEnv("kkkkkkkk"))


if __name__ == '__main__':
    unittest.main()
