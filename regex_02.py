import re 

# meta caracteres: . ^ $ * + ? {} [] \ () 
texto = '''
João trouse flores para sua amada namorada em 10 de janeiro de 1970,
Maria era  o nome dela


Foi um ano excelente na vida de joão. Teve 5 filhos, todos aldutos atualemente.
maria, hoje sua esposa, ainda faz aqule café com pão de queijo nas tardes de 
pão de quiejo
Não canso de ouvir a Maria:
"Jooooooooãooooooo, o café tá prontinho aqui. veemm"!
'''
print(texto)
print(re.findall(r'[a-z]oão|[A-Z]aria|amada|[A-Za-z0-9]lores',texto))
print(re.findall(r'FILHOS|mAria',texto, flags=re.I))