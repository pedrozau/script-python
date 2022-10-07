# _*_ coding: utf8 _*_
class Pessoa:

     def __init__(self, nome, idade,comer=False):
         self.nome = nome
         self.idade = idade
         self.comer = comer
     def inicio(self):
        print(f'O seu nome é {self.nome} e  a sua idade é {self.idade}')

     def come(self,alimento):
        if(self.comer):
            print(f'Estou comendo {alimento}')
        else:
            print(f'Não estas a coner')


class Aluno(Pessoa):
     
     def __init__(self):
         pass
