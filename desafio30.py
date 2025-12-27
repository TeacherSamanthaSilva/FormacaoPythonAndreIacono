# Para este desafio crie uma função que calcule a potência de um número: A função deve aceitar dois 
# argumentos a base e o expoente. 

def potencia(base, expoente):
    resultado = base ** expoente
    return resultado

base = int(input("Digite o valor da base"))
expoente = int(input("Digite o valor do expoente"))

print(f"O resultado de {base} elavado no {expoente} é {potencia(base,expoente)}")