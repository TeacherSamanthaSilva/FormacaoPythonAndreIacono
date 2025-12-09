""" Para este desafio peça ao usuário para digitar a sua idade. Se a idade for menor que 13 anos imprima
você é uma criança, se a idade for entre 13 e 18 anos imprima você é adolescente, e se for maior que 18
imprime você é adulto """

idade = int(input("Digite a sua idade: "))

if idade < 13:
    print("Você é criança")
elif idade >= 13 and idade <18:
    print("Você é adolescente")
else: 
    print("Você é adulto")