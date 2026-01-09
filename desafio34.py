# Para este desafio crie uma função lambda que aceite dois números e retorne a multiplicação desses número

multiplicacao = lambda numero1,numero2: numero1 * numero2

numero1 = int(input("Digite o primeiro número "))
numero2 = int(input("Digite o segundo número "))

print(f"A multiplicação de {numero1} por {numero2} é {multiplicacao(numero1,numero2)}")