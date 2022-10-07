
import string

artistas = ["Pedro","José","Maria","Suzana","Marcos","Madalena","Luiz"]

def instrumentos(artistas):
    instro  = ["Bateria","Guitarra","Piano"]
    for person in artistas:
        for itens in instro:
            print(f'{person} Toca {itens}')

       


instrumentos(artistas)

def contar():
    cont = range(1,11)
    for cnt in  cont:
        print(cnt)
#contar()


"""
  Coleção 
   -lista
   -tupla
   -dicionario
"""

def numeros():
    i = 1;
    f = 3.14
    c = 3 + 4j
    print(type(i))
    print(type(f))
    print(type(c))
    print(f'Parte real: {c.real}')
    print(f'Parte imaginário:{c.imag}')
    print(f'conjugado:{c.conjugate()}')
#numeros()

def caractere():
    """
       
    """
    s = "Python"
    #print('Tamanho %s => %d'%(s,len(s)))
    a = string.ascii_letters
    for alf in a:
        print(' %s'%(alf.upper()))
#caractere()

def tranducao():
    try:
        eng = "Good norning"
        fr = "Bom jour"
        tab = string.maketrans(eng, fr)
        pt = "Bom dia"
        print(string.translate(pt,tab))
    except:
           print("Sorry..!!")
#tranducao()

