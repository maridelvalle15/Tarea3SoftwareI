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
    # Al debitar la cuenta, el saldo queda en cero (monto a debitar=saldo disponible)
    def testSaldoFinalCero(self):
        billetera = BilleteraElectronica(5,'Andres','Navarro',21315197,'AAA12')
        billetera.recargar(20,'01/01/2015',501)
        billetera.consumir(20,'02/01/2015',502,'AAA12')
        self.assertEqual(billetera.saldo,0)
    # Recarga de monto muy grande
    def testMontoGrande(self):
        billetera = BilleteraElectronica(5,'Andres','Navarro',21315197,'AAA12')
        billetera.recargar(999999999999999999999999999,'10/10/2015',590)
        self.assertEqual(billetera.saldo,999999999999999999999999999)
    # Nombre invalido
    def testNombreInvalido(self):
        self.assertRaises(Exception,BilleteraElectronica,11,'','Perez',23456772,'32wqZ')
    # Apellido invalido
    def testApellidoInvalido(self):
        self.assertRaises(Exception,BilleteraElectronica,12,'Jorge','',22436780,'32wqZ')
    # Num cedula invalido
    def testCIInvalido(self):
        self.assertRaises(Exception,BilleteraElectronica,13,'Pedro','Perez',0,'32wqZ')
    # PIN invalido
    def testPINInvalido(self):
        self.assertRaises(Exception,BilleteraElectronica,14,'Marta','Perez',23456772,'')
    # Introduccion monto negativo para recargar
    def testRecargarNegativo(self):
        billetera = BilleteraElectronica(6,'Nelson','Saturno',20489547,'NAST9')
        self.assertRaises(Exception,billetera.recargar,-10,'02/05/2015',500)
    # Introduccion monto negativo para consumir
    def testConsumoNegativo(self):
        billetera = BilleteraElectronica(7,'Susana','Rodriguez',24289557,'Sus4R')
        billetera.recargar(20,'01/01/2015',501)
        self.assertRaises(Exception,billetera.consumir,-10,'02/01/2015',502,'Sus4R')
    # Introduccion monto consumo mayor a saldo disponible
    def testConsumoMayorASaldo(self):
        billetera = BilleteraElectronica(10,'Rodrigo','Teran',21367888,'1230O')
        billetera.recargar(20,'22/12/2014',510)
        self.assertRaises(Exception,billetera.consumir,21,'25/12/2014',511,'1230O')
        
    # Introduccion de clave erronea
    def testClaveErronea(self):
        billetera = BilleteraElectronica(8,'Mariana','Nunez',21345100,'AAA12')
        billetera.recargar(20,'01/01/2015',501)
        self.assertRaises(Exception,billetera.consumir,10,'02/01/2015',502,'AAA13')
    # Caracteres no numericos en cedula
    def testCILetras(self):
        self.assertRaises(Exception,BilleteraElectronica,9,'Belinda','Morillo','123q','6900',0,[],[])
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()