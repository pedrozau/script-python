class User:
    def __init__(self,name,salario):
        self.name = name
        self.salario = salario

    @property 
    def name(self):
        return self._name
    @name.setter
    def name(self,valor):
        self._name = valor.replace("e","i")
        

    @property 
    def salario(self):
        return self._salario
    @salario.setter
    def salario(self,valor):
        self._salario = valor.replace('Kz','')

    def show(self):
        print(f'{self.name}')
        print(f'Seu salario: {self.salario}')


p = User('Pedro','1000Kz')

p.show()
