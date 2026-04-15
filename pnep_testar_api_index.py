import requests
from pnep_api_index import ApiIndex

api = ApiIndex()

# URL da API
#api_url = f"http://api-indice:8001/{indexador}/{mes}/{ano}"
#api_url = "http://api-indice:8001/ipca/11/2023"

data, valor = api.consulta_por_mes_ano('tr',9,2022)
print(f"data: {data} valor: {valor}")

dados = api.consulta_por_periodo('tr',1,2023,4,2024)
print(dados)






'''
try:
    # Fazendo a solicitação GET para a API
    response = requests.get(api_url)
    
    # Verificando se a solicitação foi bem-sucedida (código de status 200)
    if response.status_code == 200:
        # Imprimindo a resposta da API
        print("Resposta da API:")
        print(response.json())
    else:
        # Imprimindo uma mensagem de erro caso a solicitação não tenha sido bem-sucedida
        print("Erro ao acessar a API. Código de status:", response.status_code)

except requests.RequestException as e:
    # Imprimindo uma mensagem de erro se ocorrer uma exceção durante a solicitação
    print("Erro durante a solicitação para a API:", e)
'''