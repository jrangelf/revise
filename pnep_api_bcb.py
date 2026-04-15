import json
import time
import requests
import datetime
from datetime import datetime

class ApiBcb():

    def consulta_bc_ultimos(self, codigo_bcb, ultimos):
        url = f'https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo_bcb}/dados/ultimos/{ultimos}?formato=json'
        response = requests.get(url)    
        if response.status_code == 200:
            data = json.loads(response.text)            
            # Criar uma lista para armazenar os dicionários de dados
            df = []            
            for item in data:
                data_str = item['data']
                valor = float(item['valor'])                
                # Converter a data para o formato datetime
                data_datetime = datetime.strptime(data_str, '%d/%m/%Y')                
                # Criar o dicionário com a data e o valor e adicioná-lo à lista
                df.append({
                    'data': data_datetime,
                    'valor': valor
                })            
            return df
        else:
            print(f"Erro ao acessar a API. Código de status: {response.status_code}")
            return None


    def consulta_bc(self, codigo_bcb):
        url = f'http://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo_bcb}/dados?formato=json'
        response = requests.get(url)        
        if response.status_code == 200:
            data = json.loads(response.text)            
            # Criar uma lista para armazenar os dicionários de dados
            df = []            
            for item in data:
                data_str = item['data']
                valor = float(item['valor'])                
                # Converter a data para o formato datetime
                data_datetime = datetime.strptime(data_str, '%d/%m/%Y')                
                # Criar o dicionário com a data e o valor e adicioná-lo à lista
                df.append({
                    'data': data_datetime,
                    'valor': valor
                })            
            return data #df
        else:
            print(f"Erro ao acessar a API. Código de status: {response.status_code}")
            return None

    def consultar_bc_periodo(self, codigo_bcb, inicio, final):
        url = f'https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo_bcb}/dados?formato=json&dataInicial={inicio}&dataFinal={final}'
        
        try:
            # Definir timeout de 10 segundos para a solicitacao
            response = requests.get(url, timeout=10)
            # Definir atraso de 10 segundos para a proxima requisição            
            time.sleep(10)
            
            if response.status_code == 200:
                try:
                    data = json.loads(response.text)
                    return data
                except:
                    return None 
            else:                
                erro = response.json().get("erro")
                if erro:
                    detail = erro.get("detail", "Detalhe não encontrado")
                    print(f"\nÍndice não encontrado.\nurl: {url}\nCódigo de status: {response.status_code}\n{detail}\n[consultar_bc_periodo]\n")
                    return "not found"
                else:
                    print("Nenhuma informação de erro encontrada.")
                return "not info"
            
        except requests.Timeout:
            print(f"A solicitação {codigo_bcb} excedeu o tempo limite.\n[consultar_bc_periodo]")
            return None
        except requests.RequestException as e:
            print(f"Erro ao fazer a solicitaçao: {e}\nurl: {url}\n[consultar_bc_periodo]")
            return "erro"

