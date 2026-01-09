# Para este desafio crie uma funçao lambda que aceite um número e retorne o cubo desse número. 

cubo = lambda numero:  numero ** 3 

numero = int(input("Digite um número qualquer "))
print(f"O cubo de {numero} é {cubo(numero)}")