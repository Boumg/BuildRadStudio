import pathlib
import sys
import unittest

if __name__ == '__main__':
    path = pathlib.Path(__file__).resolve().parent.parent
    sys.path.insert(0, str(path))

from rxbuilder.VerifAvantCompilation import siProcessEnCours, attenteArretBds, checkVarEnv


class TestVerifAvantCompilation(unittest.TestCase):

    def test_ProcessAbsent(self):
        self.assertFalse(siProcessEnCours('kkkkkkkk'))

    def test_ProcessEnCours(self):
        self.assertTrue(siProcessEnCours('svchost'))
    @unittest.skip("partie à la main, skipping")
    def test_AttenteBDE(self):
        attenteArretBds()

    def test_existeVariableEnv(self):
        self.assertTrue(checkVarEnv("USERPROFILE"))
        self.assertRaises(Exception, checkVarEnv, "PATH")
        self.assertRaises(Exception, checkVarEnv, "kkkkkkkk")

if __name__ == '__main__':
    unittest.main()
