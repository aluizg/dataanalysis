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

def initializa_df_canada(df):
    # Removendo colunas desnecessárias
    print('\nRemovendo colunas desnecessárias...')
    df.drop(['AREA', 'REG', 'DEV', 'Type', 'Coverage'], axis=1, inplace=True)

    # Renomear colunas para facilitar o acesso
    print('\nRenomeando colunas para facilitar o acesso...')
    df.rename(columns={'OdName': 'Pais', 'AreaName': 'Continente', 'RegName': 'Região'}, inplace=True)

    # Adicionar uma coluna 'Total' que é a soma de todas as colunas de anos
    print('\nAdicionando coluna "Total" que é a soma de todas as colunas de anos...')
    df['Total'] = df.sum(axis=1, numeric_only=True)

    # Definindo coluna Total como ordenacao
    print(f'Ordenando o DataFrame pela coluna "Total" em ordem decrescente...')
    df.sort_values(by='Total', ascending=False, inplace=True)

    # Definindo a coluna Total como indice do DataFrame
    print('\nDefinindo a coluna "Pais" como índice do DataFrame...')
    df.set_index('Pais', inplace=True)

    # Tratamento das colunas como string
    df.columns = list(map(str, df.columns))
    print(f'Colunas sendo tratadas como string: {all(isinstance(column, str) for column in df.columns)}')
