import numpy as np
import pandas as pd
import utils.datafile as util

# Carrega o arquivo de dados usando a função load_file do módulo utils
df = util.load_file('datasets', 'fifa.csv')

print("### Dados carregados com sucesso ###")
# 5 primeiras linhas do DataFrame
print(df.head(5))

# 10 ultimas linhas do DataFrame
# print(df.tail(10))

# exibir o nome das colunas do DataFrame
# print(df.columns)ß

# exibir o tipo de dados de cada coluna do DataFrame
# print(df.dtypes)

# exibir todas as colunas do DataFrame
# print(df.describe(include="all"))

# Informações gerais sobre o DataFrame, incluindo o número de entradas, colunas, tipos de dados e uso de memória
# print(df.info())

# Calcular media da idade dos jogadores
#media_idade = df['Age'].mean()
# print(f'Média de idade dos jogadores: {media_idade:.2f} anos')

# Substitua NaN pelo valor médio da coluna 'Age'
# df['Age'].fillna(media_idade, inplace=True)
# df['Age'].replace(np.nan, media_idade, inplace=True)
