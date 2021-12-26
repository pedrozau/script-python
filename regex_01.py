#_*_  coding: utf8 _*_ 
import  re 

"""
findall search sub compile
"""

string = "Este é um teste de expressões regulares."

print(re.search(r'teste', string))
print(re.findall(r'teste',string))
print(re.sub(r'teste','aula',string))
print(re.sub(r'um','uma',string))

regx = re.compile(r'teste')

print(regx.search(string))
print(regx.findall(string))
print(regx.sub('You',string))