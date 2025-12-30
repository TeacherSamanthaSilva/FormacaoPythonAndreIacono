# Crie uma função para calcular o fatorial de um número

def fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * fatorial(numero - 1)

numero = int(input("Digite o número que você deseja calcular o fatorial: "))

print(f"O fatorial de {numero} é {fatorial(numero)}")