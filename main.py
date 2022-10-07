from oop import *
from exemplo import Fisica 

"""
person =  Pessoa("Pedro","19",True)

person2 = Pessoa("Jose","17")

person.inicio()

person.come("Arroz vom feijão")

person2.inicio()
person2.come("Pão com chá")
"""
v = int(input("Velocidade:"))
t = int(input("Tempo:"))
d = int(input("Deslocamento:"))
fisica = Fisica(v,t,d)
fisica.dados()
fisica.calcular()