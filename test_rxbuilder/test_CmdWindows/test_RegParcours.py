import unittest

from rxbuilder.CmdWindows import Registre


class TestRegistre(unittest.TestCase):
    def test_exiteRuche(self):
        c = Registre("Software")
        self.assertTrue(c.si_existe_ruche())
        self.assertTrue(c.si_existe_ruche('Microsoft'))
        self.assertFalse(c.si_existe_ruche("merdemerde"))
        b = Registre("merdemerde")
        self.assertFalse(b.si_existe_ruche())

if __name__ == '__main__':
    unittest.main()