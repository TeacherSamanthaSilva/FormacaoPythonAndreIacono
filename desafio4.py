""" Crie um programa para calcular o índice de massa corporal de uma pessoa

se o indice for menor que 18.5 está muito baixo
se tiver entre 18.5 e 24.9 está normal 
se tiver entre 25 e 29.9 está com sobrepeso
se tiver entre 30 e 39.9 a pessoa está com obesidedade
se tiver acima de 40 a pessoa está com obesidade grave """


peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))
imc = peso/(altura * altura)

if imc < 18.5:
    print(f"O seu imc de {imc} está muito baixo")
elif imc >= 18.5 or imc <= 24.9:
    print(f"O seu imc de {imc} está normal")
elif imc >25 or imc <= 29.9:
    print(f" O seu imc é de {imc} você está com sobrepeso")
elif imc >30 or imc <= 39.9:
    print(f"O seu imc é de {imc} você está com obesidade")
else:
    print(f"O seu imc é de {imc} Você está com obesidade grave")