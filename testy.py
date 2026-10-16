import unittest
from eukaliptus import *


class NWDtests(unittest.TestCase):
    def test_NWD_RowneLiczby(self):
        self.assertEqual(5, NWD(5,5))
    def test_NWD_PierwszaWieksza(self):
        self.assertEqual(4, NWD(12,4))
    def test_NWD_PierwszaMniejsa(self):
        self.assertEqual(4, NWD(4,12))
    def test_NWD_LiczbyWzgledniePierwsze(self):
        self.assertEqual(1, NWD(7,11))
    def test_NWD_WspolnyDzielnik(self):
        self.assertEqual(6, NWD(18,24))
    def test_NWD_DuzeLiczby(self):
        self.assertEqual(12, NWD(120,84))
    def test_NWD_PierwszaLiczbaJeden(self):
        self.assertEqual(1, NWD(1,15))
    def test_NWD_DrugaLiczbaJeden(self):
        self.assertEqual(1, NWD(21, 1))
    def test_NWD_Wielokrotnosc(self):
        self.assertEqual(12, NWD(36,12))
    def Test_NWD_DwieLiczbyPierwsze(self):
        self.assertEqual(1, NWD(13,17))
if __name__ == '__main__':
    unittest.main()
