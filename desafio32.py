# Para este desafio crie duas funções: uma para calcular o dobro de um número e outra para calcular
# o quadrado de um número

def dobrodenumero(numero):
    resultado = numero * 2
    return resultado

def quadradodenumero(numero):
   resultado =  numero * numero 
   return resultado


numero = int(input("Digite um número qualquer"))

print(f"O dobro de {numero} é {dobrodenumero(numero)}")

print(f"O numero {numero} elevado ao quadrado é {quadradodenumero(numero)}")