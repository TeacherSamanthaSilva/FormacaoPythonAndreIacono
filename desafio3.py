""" Crie um programa que gere três listas de acordo com as necessidades abaixos
Lista 1 - Funcionários que tem carro e trabalha a noite
Lista 2 - Funcionários que tem carro e trabalham durante o dia
Lista 3 - Funcionários que não tem carro """

Funcionarios = ["Thiago","Guilherme","Gabriel","Jader","Suzana","Kevin","Felipe"]
turnododia = ["Thiago","Guilherme","Gabriel","Jader"]
turnodanoite = ["Suzana","Kevin","Felipe"]
temcarro = ["Thiago","Guilherme","Kevin","Felipe"]

#Lista 1 - Funcionários que tem carro e trabalham a noite

lista1 = set(temcarro).intersection(turnodanoite)
print(lista1)

#Lista 2 - Funcionários que tem carro e trabalham durante o dia

lista2 = set(temcarro).intersection(turnododia)
print(lista2)

#Lista 3 - Funcionários que não tem carro

lista3 = set(Funcionarios).difference(temcarro)
print(lista3)