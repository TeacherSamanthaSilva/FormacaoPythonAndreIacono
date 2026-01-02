# Para este desafio crie duas funções: uma para calcular o dobro de um número e outra para calcular
# o quadrado de um número

def dobrodenumero(numero):
    numero *2
    return numero

def quadradodenumero(numero):
    numero * numero 
    return numero

numero = int(input("Digite um número qualquer"))

print(f"O dobro de {numero} é {dobrodenumero(numero)}")

print(f"O numero {numero} elevado ao quadrado é {quadradodenumero(numero)}")