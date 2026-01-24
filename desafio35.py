# Para este desafio crie uma função lambda que aceite um número e retorne Par para o número for para ou
# retorne Impar se o número for ímpar

par_ou_impar = lambda numero : 'Par' if numero % 2 == 0 else 'Impar'

numero = int(input("Digite um número "))
print(f" O número {numero} é {par_ou_impar(numero)}")