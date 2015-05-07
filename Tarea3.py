
class BilleteraElectronica:
    
    def __init__(self,id,nombres,apellidos,CI,PIN,saldo=0,recargas=[],consumos=[]):
        self.id = id
        self.nombres = nombres
        self.apellidos = apellidos
        self.ci = CI
        self.pin = PIN
        self.saldo = saldo
        self.recargas = recargas
        self.consumos = consumos
        
        if (nombres=='') or (apellidos==''):
            raise Exception ("Los campos de nombre y apellido deben contener al menos 1 letra")
        
        if (CI==0):
            raise Exception ("El numero de cedula es invalido")
        
        if (PIN==''):
            raise Exception ("Debe introducir un PIN valido")
        
        if not isinstance (CI,int):
            raise Exception ("La cedula solo debe contener caracteres numericos")
        
    def recargar(self,monto,fecha,idEstablecimiento):
        if (monto<0) : 
            raise Exception ("El monto a recargar no debe ser negativo")
        else :
            self.saldo = self.saldo + monto
            self.recargas.append([monto,fecha,idEstablecimiento])
    
    def consumir(self,monto,fecha,idEstablecimiento,clave):
        if (self.saldo < monto):
            raise Exception ("El monto a consumir no debe exceder el saldo disponible")
        elif (monto<0):
            raise Exception ("El monto a consumir no debe ser negativo")
        elif (self.pin!=clave): 
            raise Exception ("La clave introducida es incorrecta")
        else: 
            self.saldo = self.saldo - monto
            self.consumos.append([monto,fecha,idEstablecimiento])
        return 0
    
    def verRecargas(self):
        return self.recargas
    
    def verConsumos(self):
        return self.consumos
    
    def verSaldo(self):
        return self.saldo
       
        
        
if __name__ == '__main__':
    pass