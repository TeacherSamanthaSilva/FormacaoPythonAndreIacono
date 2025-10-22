""" Crie um programa que leia a temperatura do churrasco
e dependendo da temperatura digitada ela retorne qual é o
ponto do cozimento da carne """


temperatura = int(input("Digite a temperatura da carne: "))

if temperatura >= 48:
    print("A carne está selada")
elif temperatura >=54 or temperatura < 60:
    print("A carne está no ponto")
else:
    print("A carne está bem passada")