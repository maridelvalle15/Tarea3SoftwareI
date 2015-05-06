'''
Created on May 6, 2015

@author: marisela
'''
import unittest
from Tarea3 import *


class Test(unittest.TestCase):

    # Apellidos con Acentos
    def testApellidosAcentos(self):
        billetera = BilleteraElectronica(1,'Juan','Pérez',20495287,'A123B')
    # Apellidos con Ñ
    def testApellidosEnie(self):
        billetera = BilleteraElectronica(2,'Roberto','Patiño',20495281,'A123C')
    # Apellidos con dieresis
    def testApellidosDieresis(self):
        billetera = BilleteraElectronica(3,'Ricardo','Münch',20176224,'A234A')
    # Apellidos con guion
    def testApellidosGuion(self):
        billetera = BilleteraElectronica(4,'Maria','Del-Valle',26738111,'32ASo')
    # Caracteres no numericos en cedula
    def testCILetras(self):
        pass
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()