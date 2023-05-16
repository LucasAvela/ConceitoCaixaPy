import os
import json

produtos = []
loop = 1

if os.path.exists("Data/Produtos.json"):
    with open("Data/Produtos.json", "r") as json_file:
        produtos = json.load(json_file)

while loop == 1:

    nome = input("Digite o Nome do produto: ")
    cod = str(input("Escaneie o Código do produto: "))
    valor = float(input("Entre com o Preço do produto: "))

    item = {
        "Nome": nome,
        "Cod": cod,
        "Valor": valor
    }

    produtos.append(item)

    Input = int(input(" \n1.Continuar\n2.Finalizar\n: "))

    if Input == 1:
        loop = 1
    else:
        loop = 0

json_data = json.dumps(produtos, indent=4)

with open("./Data/Produtos.json", "w") as json_file:
    json_file.write(json_data)
