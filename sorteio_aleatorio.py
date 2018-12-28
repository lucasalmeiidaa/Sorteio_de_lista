#Script para sortear elementos de uma lista.
#Autor: Lucas Evangelista de Almeida

import random
numero_inferior = int(input("Sua lista inicia em que número? "))
numero_superior = int(input("Sua lista termina em que número? "))
lista = list(range(numero_inferior, (numero_superior + 1)))

print (input("\n\nPressione enter para escolher aleatóriamente um número..."))

while lista != []:
    elemento = random.choice(lista)
    print ("\nNÚMERO SORTEADO:",elemento, "\nEste número não será sorteado novamente." )
    lista.remove(elemento)
    print (input("\n \n Pressione enter para escolher aleatóriamente outro número..."))
    continue

if lista == []:
    print("\n\n Todos elementos da lista foram sorteados. \n\n\n")
