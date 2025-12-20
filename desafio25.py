""" Para este desafio crie uma lista com três cidades. Peça ao usuário para digitar o nome de uma cidade
Se a cidade estiver na lista imprima. A cidade está na lista de cidades. Se a cidade não estiver na lista 
Imprima a cidade não está na lista de cidades OBS: Pode usar tupla em vez de lista """

cidades = ("Lages", "Florianópolis","Pomerode")
cidade_digitada = str(input("Digite o nome de qualquer cidade: "))

if cidade_digitada in cidades:
    print("A cidade está na lista de cidades.")
else:
    print("A cidade não está na lista de cidades")