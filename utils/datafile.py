# funcoes gerais para manipulacao de arquivos de dados
from pathlib import Path
from pandas import pandas as pd
import os


"""
Carrega um arquivo de dados do tipo especificado (csv, xlsx, json) e retorna um DataFrame do pandas.

Parâmetros:
- dir_name: Diretório onde o arquivo está localizado.
- file_name: Nome do arquivo a ser carregado.
- file_type: Tipo do arquivo ('csv', 'xlsx', 'json'). Padrão é 'csv'.

Retorna:
- DataFrame do pandas contendo os dados carregados.
"""
def load_file(dir_name, file_name, file_type='csv'):
    # obtem diretorio atual
    base_dir = Path(__file__).parent.parent.absolute()

    # obtem o arquivo a
    file_path = os.path.join(base_dir, dir_name, file_name)

    print(f'Carregando arquivo {file_type}: {file_path}')

    if 'csv' in file_type or 'data' in file_type:
        return pd.read_csv(file_path)
    elif file_type == 'xlsx':
        return pd.read_excel(file_path,
    sheet_name='Canada by Citizenship',
    skiprows=range(20),
    skipfooter=2)
    elif file_type == 'json':
        return pd.read_json(file_path)
    else:
        raise ValueError(f'Tipo de arquivo {file_name} não suportado. Use csv, xlsx ou json')