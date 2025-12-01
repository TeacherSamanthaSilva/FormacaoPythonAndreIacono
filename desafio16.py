""" Para este desafio crie uma lista de frutas e outra de vegetais . Use um Nested for loop (For loop
aninhado )  para imprimir todas as combinações possíveis de frutas e vegetais, com a fruta primeiro
e o vegetal em segundo. """

frutas = ["maça", "banana", "manga"]

vegetais = ["cenoura", "alface", "brocolis"]

for fruta in frutas:
    for vegetal in vegetais:
        print(fruta, vegetal)
