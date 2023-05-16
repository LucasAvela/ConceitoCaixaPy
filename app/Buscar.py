import json
import os
import datetime

produtos = []
produtosEncontrados = []
nomes = []
codigos = []
quantidades = []
valores = []

loop = 1

def buscar(codigo, Produtos):
    for item in Produtos:
        if (item["Cod"]) == codigo:
            return item
        elif item["Nome"].lower() == codigo.lower():
            return item
    return None

with open("Data/Produtos.json", "r") as json_file:
    produtos = json.load(json_file)

while loop == 1:
    busca = str(input("Busca: "))
    Produto = buscar(busca, produtos)

    if Produto:
        unidades = int(input("Quantidade: "))
        
        nomes.append(Produto["Nome"])
        codigos.append(Produto['Cod'])
        quantidades.append(unidades)
        valores.append(Produto["Valor"])
        
        os.system("cls")
        
        for codigo, nome, valor, quantidade in zip(codigos, nomes, valores, quantidades):
            print(f"{codigo}: {quantidade} . {nome} . R${valor}")
    else:
        Input = int(input(" \n1.Finalizar\n2.Tentar Novamente\n: "))

        if Input == 1:
            loop = 0
            os.system("cls")
        else:
            loop = 1
            os.system("cls")


for nome, valor, quantidade in zip(nomes, valores, quantidades):
    print(f"{quantidade} . {nome} . R${valor}")

total = [quantidade * valor for quantidade,
         valor in zip(quantidades, valores)]

soma = sum(total)
resultado = "{:.2f}".format(soma)
print("Total: R$", soma)

pagamento = ""
definirPagamento = int(input(" \nMetodo de Pagamento:\n1.Dinheiro\n2.Pix\n3.Debito\n4.Credito\n: "))

if definirPagamento == 1:
    pagamento = "Dinheiro"
elif definirPagamento == 2:
    pagamento = "Pix"
elif definirPagamento == 3:
    pagamento = "Debito"
elif definirPagamento == 4:
    pagamento = "Credito"

os.system("cls")
for nome, valor, quantidade in zip(nomes, valores, quantidades):
    print(f"{quantidade} . {nome} . R${valor}")
print("Total: R$", resultado)
print("Pago com:", pagamento)

input(".\nAperte Enter para Sair")

agora = datetime.datetime.now()
datahora = agora.strftime("%Y%m%d%H%M%S")
notafiscal = f"{datahora}"
diretorio = "./Notas/"

notas_json = {
    notafiscal: [
        {
            "Produto": nome,
            "Valor": valor,
            "Quantidade": quantidade
        }
        for nome, valor, quantidade in zip(nomes, valores, quantidades)
    ],
    "Total: ": resultado,
    "Pago com: ": pagamento
}

# Salvar os dados em um arquivo JSON
with open(diretorio + notafiscal + ".json", "w") as arquivo_json:
    json.dump(notas_json, arquivo_json, indent=4)
