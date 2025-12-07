""" Para este desafio que que você peça ao usuário para digitar um número qualquer se este número for 
menor que 10 diga este número é menor que dez, se este número for igual a dez diga este número é igual
a 10 e se este número foi maior que 10 diga este número é maior que dez """

numero = int(input("Digite um número qualquer: "))

if numero < 10:
    print("Este número é menor que dez")
elif numero == 10:
    print("Este número é igual a dez")
else:
    print("Este número é maior que dez")