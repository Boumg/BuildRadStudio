
import unittest

class TestLancement(unittest.TestCase):
    def test_something(self):
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

        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
