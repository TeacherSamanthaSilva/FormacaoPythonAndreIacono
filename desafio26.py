""" Para este desafio crie uma lista com 5 nomes de países e as capitais desses países. Peça ao 
usuário para digitar o nome de um país. Se o pais estiver na lista imprima a capital do pais é
Se o pais não estiver na lista imprima. Desculpe não temos informação sobre a capital deste pais """

cidades = {
    "Brasil":"Brasília",
    "Argentina": "Buenos Aires",
    "Chile":"Santiago",
    "Austrália":"Camberra",
    "Canadá":"Ottawa"
}

pais_usuario = str(input("Digite qualquer nome de pais "))

if pais_usuario in cidades:
    print(f"A capital do {pais_usuario} é {cidades[pais_usuario]}" )
else:
    print("Desculpe não temos informação sobre a capital desse pais ")