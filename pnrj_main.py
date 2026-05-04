from pnrj_queries import QueriesSQL
from pnrj_conexao import Database
from pnrj_date_tools import DateTools
from pnrj_tabelas import Tabelas
from pnrj_api_bcb import ApiBcb
from pnrj_api_index import ApiIndex
from pnrj_sqldata import SQLData
from pnrj_indexadores import Indexadores
from pnrj_indices import Indices
from pnrj_juros import Juros

queries = QueriesSQL()
conexao = Database().conectar()
datetools = DateTools()

sqldata = SQLData(queries=queries, datetools=datetools, conexao=conexao)
tabelas = Tabelas(sqldata=sqldata)
apibcb = ApiBcb()
apiindex = ApiIndex()

# MARCAR AS TABELAS EM LOGATUALIZACAO QUE DEVEM SER ATUALIZADAS

# obtem as datas de atualizacao de todas as tabelas (data do ultimo registro)
# (nome da tabela, codigo, data, codigo_indexador)
_tabela_codigo_data_indexador = tabelas.obter_datas_atualizacao_tabelas()

# atualiza a tabela logatualizacao com as datas dos ultimos registros das tabelas
_registros = tabelas.atualizar_datas_logatualizacao(_tabela_codigo_data_indexador)

# marcar tabelas que devem ser atualizadas no logatualizacao (codigo e data)        
_tabelas_marcadas = tabelas.marcar_tabelas_para_atualizacao(datetools.dia_de_hoje())  

# gerar tabelas_para_atualizacao com (codigo, data, nome_tabela, codigo_indexador) 
# que sao as tabelas que devem ser atualizadas
mapa = {item[1]: (item[0], item[3]) for item in _tabela_codigo_data_indexador}

tabelas_atualizacao = [
    (codigo, data, mapa[codigo][0], mapa[codigo][1])
    for codigo, data in _tabelas_marcadas
    if codigo in mapa
]

if tabelas_atualizacao:
    print(f'\nTabelas que devem ser atualizadas')
    for i in tabelas_atualizacao:
        print(i)


# Atualizar os indexadores
indexadores = Indexadores(datetools=datetools, tabelas=tabelas, apibcb=apibcb, tabelas_atualizar=tabelas_atualizacao)
tabelas_bcb = indexadores.atualizar_indexadores()    

# Atualizar os indices PNRJ
indices = Indices(datetools=datetools, tabelas=tabelas, apiindex=apiindex)
tabelas_pnrj = indices.atualizar_indices()

# Atualizar os juros
juros = Juros(datetools=datetools, tabelas=tabelas, apiindex=apiindex)
tabelas_juros = juros.atualizar_juros()






