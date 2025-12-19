""" Para este desafio crie uma lista de números de 1 a 10. Use um for loop para iterar sobre a lista 
Se o número atual da iteração for par imprime este número é par e caso seja ímpar imprima este número
é ímpar"""

numero = [1,2,3,4,5,6,7,8,9,10]

for i in numero:
    if i % 2 == 0:
        print(numero[i])
        print("Este número é par")
    else:
        print("Este número é impar")
