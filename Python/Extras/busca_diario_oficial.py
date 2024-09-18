import requests

data_inicial = "01/09/2024"
texto_busca = "Felipe Gustavo Braiani Santos"
url = "https://www.spdo.ms.gov.br/DiarioDOE/Index/Index/1"

print(f"Iremos buscar no Diário Oficial do Estado de Mato Grosso do Sul os diários publicados a partir de {data_inicial} que contenham o texto '{texto_busca}'")

if input("Deseja alterar a data inicial? (s para sim): ").lower() == "s":
    data_inicial = input("Digite a nova data inicial (dd/mm/aaaa): ")
    if not data_inicial:
        print("Data inválida")
        data_inicial = "01/09/2024"
        print(f"Data mantida em {data_inicial}")

if input("Deseja alterar o texto de busca? (s para sim): ").lower() == "s":
    texto_busca = input("Digite o novo texto de busca: ")
    if not texto_busca:
        print("Texto inválido")
        texto_busca = "Felipe Gustavo Braiani Santos"
        print(f"Texto mantido em '{texto_busca}'")

print()
post_data = {
    "Filter.Numero": "",
    "Filter.DataInicial": data_inicial,
    "Filter.DataFinal": "",
    "Filter.Texto": texto_busca,
    "Filter.TipoBuscaEnum": "1",
}

try:
    response = requests.post(url, data=post_data)
    response.raise_for_status()

    data = response.json()
    if not data["dataElastic"]:
        print("Nenhum resultado encontrado")
        exit()

    for item in data["dataElastic"]:
        link_diario = f"https://www.spdo.ms.gov.br/diariodoe/Index/Download/{item['Source']['NomeArquivo'].replace('.pdf', '')}"
        print(f"Diário n. {item['Source']['Numero']} - {item['Source']['Descricao']}")
        print(f"Link Download: {link_diario}")
        if input("Deseja baixar o diário? (s para sim): ").lower() == "s":
            print("Baixando...")
            download = requests.get(link_diario)
            with open(f"{item['Source']['Numero']} - {item['Source']['Descricao']}.pdf", "wb") as file:
                file.write(download.content)
            print("Download concluído")
        print("\n")
except Exception as e:
    print("Erro ao fazer a requisição: ", e)