""" Para este desafio crie dois conjuntos, cada um contendo 5 nomes, Alguns nomes devem estar presentes
em ambos os conjuntos. Use um métódo para encontrar quais nomes aparecem em ambos os conjuntos
e imprima o resultado """

friends1 = {"Guilherme","Gabriel","Camila","Milena","Matheus"}
friends2 = {"João","Milena","Gabriel","Ulysses","Leonardo"}

interseccao = friends1.intersection(friends2)
print(interseccao)

uniao = friends1.union(friends2)
print(uniao)

diferenca = friends1.difference(friends2)
print(diferenca)