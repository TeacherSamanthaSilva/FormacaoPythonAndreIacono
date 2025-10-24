""" Crie um programa que receba a altura e a largura de uma parede e diga quantas latas de tinta
vai precisar sabendo que cada lata pinta 5m2 de parede """

altura = int(input("Digite a altura da parede"))
largura = int(input("Digite a largura da parede"))

area = altura * largura
quantidadedetinta = area / 5
print(f"A quantidade de tinta necessária para pintar a parede é {quantidadedetinta}")