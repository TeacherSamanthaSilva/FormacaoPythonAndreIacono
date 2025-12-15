""" Para este desafio imagine que você tem uma loja de carros. Crie uma lista com os carros que você
tem em estoque e peça para o usuário para que ele insira o nome do carro que deseja comprar. 
Se o carro estiver em estoque imprima, este carro está disponível. Se você não tive o carro 
em estoque imprima Desculpe este carro não está disponível """

carros = ["Fiat Mobi","Fiat Argo","Chevrolet Onix","Hyundai HB20","Wolkswagen Gol","Renaul Kwid",
          "Peugeot 208","Toyota Etios","Fiat Uno","Chevrolet Celta","Ford Ka","Renault Sandero",
          "Wolkswagen Fox"]

pesquisa_carro = str(input("Digite o carro que você deseja comprar? "))

if pesquisa_carro in carros:
    print("Este carro está disponível. Você deseja compra-lo? ")
else:
    print("Desculpe, Nós não temos este carro no momento")