import unittest
from rxbuilder.cmake_util import get_cmake_cde,get_ctest_cde, Cde, is_cmake


class TestCmake(unittest.TestCase):
    def test_get_cmake_cde(self):
        if is_cmake():
            Cde(get_cmake_cde() + "--version")

    def test_get_ctest_cde(self):
        if is_cmake():
            Cde(get_ctest_cde() + "--version")


if __name__ == '__main__':
    unittest.main()
