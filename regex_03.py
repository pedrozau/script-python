# _*_ coding: utf-8 _*_
import re


texto = '''
João trouse flores para sua amada namorada em 10 de janeiro de 1970,
Maria era  o nome dela


Foi um ano excelente na vida de joão. Teve 5 filhos, todos aldutos atualemente.
maria, hoje sua esposa, ainda faz aqule café com pão de queijo nas tardes de 
pão de quiejo
Não canso de ouvir a Maria:
"Jooooooooãooooooo, o café tá prontinho aqui. veeemm"!
'''
reg = re.compile(r'[A-Za-z]oão')
reg.sub('joão*',texto)
print(re.sub(r'jo+â+o','Pedro',texto))
print(re.findall(r'jo+ão',texto, flags=re.IGNORECASE))
print(re.findall(r've{3}m{1,2}',texto, flags=re.IGNORECASE))



