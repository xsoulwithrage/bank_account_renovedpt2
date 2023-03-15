
class CuentaBancaria:
    accounts = []
    def __init__(self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        CuentaBancaria.accounts.append(self)

    def deposito(self, amount):
        self.balance += amount
        return self

    def retiro(self,amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Fondos insuficientes: Cobrando una tarifa de $5")
            self.balance -= 5
        return self
    
    def mostrar_informacion_cuenta(self):
        print(f"Balance: {self.balance}")
        return self

    def generar_interes(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def imprime_todas_cuentas(cls):
        for account in cls.accounts:
            account.mostrar_informacion_cuenta()

class Usuario:
    def __init__(self, name):
        self.name = name
        self.account = {
            "cheques" : CuentaBancaria(.05,2000),
            "ahorros" : CuentaBancaria(.02,3000)
        }
        

    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.name}, cheques Balance: {self.account['cheques'].mostrar_informacion_cuenta()}")
        print(f"Usuario: {self.name}, ahorros Balance: {self.account['ahorros'].mostrar_informacion_cuenta()}")
        return self

    def transfer_money(self,amount,usuario):
        self.amount -= amount
        usuario.amount += amount
        self.mostrar_balance_usuario()
        usuario.mostrar_balance_usuario()
        return self


Edson = Usuario("Edson")

Edson.account['cheques'].deposito(100)
Edson.mostrar_balance_usuario()