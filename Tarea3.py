'''
Created on May 4, 2015

@author: marisela
'''

class BilleteraElectronica:
    
    def __init__(self,identificador,nombres,apellidos,CI,PIN):
        self.id = identificador
        self.nombres = nombres
        self.apellidos = apellidos
        self.ci = CI
        self.pin = PIN
        
    def recargas(self,monto,fecha,idEstablecimiento):
        pass
    
    def consumos(self,monto,fecha,idEstablecimiento):
        pass
    
    def saldo(self):
        #return saldo
        pass
        
    def recargar(self):
        pass
    
    def consumir(self):
        pass
        
if __name__ == '__main__':
    pass

billetera = BilleteraElectronica(2363,"Marisela","Del Valle",23638870,1245)
print(billetera.id)
print(billetera.nombres)
print(billetera.apellidos)
print(billetera.ci)
print(billetera.pin)
