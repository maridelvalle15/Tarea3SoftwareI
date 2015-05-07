
import unittest
from Tarea3 import *


class Test(unittest.TestCase):
    
    # Chequeo de funciones
    
    # Chequear crear instancia
    def testInit(self):
        billetera = BilleteraElectronica(100,'Luis','Iglesias',26718221,'Uyh76E',0,[],[])
        self.assertEqual(billetera.nombres,'Luis')
        self.assertEqual(billetera.apellidos,'Iglesias')
        self.assertEqual(billetera.ci,26718221)
        self.assertEqual(billetera.pin,'Uyh76E')
        self.assertEqual(billetera.id,100)
        self.assertEqual(billetera.saldo,0)
        self.assertEqual(billetera.recargas,[])
        self.assertEqual(billetera.consumos,[])
        

    # Chequear que se realizo la recarga
    def testRecarga(self):
        pruebabil = BilleteraElectronica(100,'Luis','Iglesias',26718221,'Uyh76E',0,[],[])
        pruebabil.recargar(100,'09/11/2014',599)
        self.assertEqual(pruebabil.verRecargas(),[[100,'09/11/2014',599]])
    # Chequear que se realizo el consumo
    def testConsumo(self):
        pruebabil = BilleteraElectronica(100,'Luis','Iglesias',26718221,'Uyh76E',0,[],[])
        pruebabil.recargar(100,'09/11/2014',599)
        pruebabil.consumir(50, '09/12/2014', 600, 'Uyh76E')
        self.assertEqual(pruebabil.verConsumos(),[[50,'09/12/2014',600]])
    # Chequear saldo disponible
    def testSaldo(self):
        pruebabil = BilleteraElectronica(102,'Oscar','Guillen',21652890,'a1A54E',100,[],[])
        pruebabil.recargar(100,'16/08/2014',298)
        self.assertEqual(pruebabil.verSaldo(),200)        
    
    # Casos de prueba
    
    # Apellidos con Acentos
    def testApellidosAcentos(self):
        billetera = BilleteraElectronica(1,'Juan','Pérez',20495287,'A123B')
        self.assertEqual(billetera.apellidos,'Pérez')
    # Apellidos con Ñ
    def testApellidosEnie(self):
        billetera = BilleteraElectronica(2,'Roberto','Patiño',20495281,'A123C')
        self.assertEqual(billetera.apellidos,'Patiño')
    # Apellidos con dieresis
    def testApellidosDieresis(self):
        billetera = BilleteraElectronica(3,'Ricardo','Münch',20176224,'A234A')
        self.assertEqual(billetera.apellidos,'Münch')
    # Apellidos con guion
    def testApellidosGuion(self):
        billetera = BilleteraElectronica(4,'Maria','Del-Valle',26738111,'32ASo')
        self.assertEqual(billetera.apellidos,'Del-Valle')
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
        self.assertRaises(Exception,BilleteraElectronica,11,5,'Perez',23456772,'32wqZ')
    # Nombre vacio
    def testNombreVacio(self):
        self.assertRaises(Exception,BilleteraElectronica,11,' ','Perez',23456772,'32wqZ')    
    # Apellido invalido
    def testApellidoInvalido(self):
        self.assertRaises(Exception,BilleteraElectronica,12,'Jorge',51,22436780,'32wqZ')
     # Apellido vacio
    def testApellidoVacio(self):
        self.assertRaises(Exception,BilleteraElectronica,12,'Jorge',' ',22436780,'32wqZ')
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