class BilleteraElectronica:
    
    def __init__(self,id,nombres,apellidos,CI,PIN,saldo,recargas,consumos):
        self.id = identificador
        self.nombres = nombres
        self.apellidos = apellidos
        self.ci = CI
        self.pin = PIN
        self.saldo = saldo
        self.recargas = recargas
        self.consumos = consumos
       
        
    def recargar(self,monto,fecha,idEstablecimiento):
        if (monto<0) : return 1 
        self.saldo = self.saldo + monto
        self.recargas.append([monto,fecha,idEstablecimiento])
        return 0
    
    def consumir(self,monto,fecha,idEstablecimiento,clave):
        if (self.saldo < monto) or (monto<0) or (self.pin!=clave): return 1 
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
