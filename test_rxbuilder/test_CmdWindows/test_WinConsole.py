import unittest

from rxbuilder.CmdWindows import get_code_page

class Test_Winconsole(unittest.TestCase):
    def test_something(self):
        print ("code page console", get_code_page())
        self.assertTrue(len(get_code_page()) > 3)


if __name__ == '__main__':
    unittest.main()
