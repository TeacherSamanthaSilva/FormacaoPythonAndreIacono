""" Para este desafio crie uma lista de frutas e inclua maçã três vezes e outras frutas da sua escolha .
Use um loop for para contar quantas maça aparece na lista e imprima o resultado """

contador = 0

frutas = ["maçã", "uva","maçã","banana","maçã" ,"manga"]

for fruta in frutas:
    if fruta == "maçã":
        contador  += 1
    print(fruta)

print(f"A quantidade de maçãs é {contador}")


