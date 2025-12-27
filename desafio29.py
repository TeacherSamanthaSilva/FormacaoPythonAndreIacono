# Para este desafio crie uma função que aceite dois números como entrada e retorne a soma desses números


def soma(num1,num2):
    resultado = num1 + num2
    return resultado

num1 = int(input("Digite um número qualquer: "))
num2 = int(input("Digite um número qualquer: "))


print(f"A soma de {num1} e {num2} é {soma(num1,num2)}")