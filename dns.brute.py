import sys
import dns.resolver 

argumentos = sys.argv 

try:
    dominio = argumentos[1]
    lista = argumentos[2]
except:
       print(f'Falta de argumento no comando...')
       sys.exit(1)
# Abrir a wordlist 
try:
    with  open(lista)  as arquivo:
        linha = arquivo.read().splitlines()
except:
       print(f'Arquivo não encontrado o indisponivel')