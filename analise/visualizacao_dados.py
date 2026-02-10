import utils.datafile as util
import matplotlib as mpl
import matplotlib.pyplot as plt

print('### Visualização de Dados ###')
print(f'Carregando os dados do arquivo "Canada.xlsx"...')

# Carregar os dados do arquivo Excel
try:
    df = util.load_file('datasets', 'Canada.xlsx', 'xlsx')
    print('Dados carregados com sucesso!')
except Exception as e:
    print(f'Erro ao carregar os dados: {e}')
    exit()


# Exibir as primeiras linhas do DataFrame
print('\nPrimeiras 5 linhas do DataFrame:')
print(df.head())

# Exibir as últimas linhas do DataFrame
print('\nÚltimas 5 linhas do DataFrame:')
print(df.tail())

# Exibir informações gerais sobre o DataFrame
print('\nInformações gerais sobre o DataFrame:')
print(df.info(verbose=False))

# Exibir estatísticas descritivas do DataFrame
print('\nEstatísticas descritivas do DataFrame:')
print(df.describe())

# Exibir o número de linhas e colunas do DataFrame
print('\nNúmero de linhas e colunas do DataFrame:')
print(df.shape)

# Exibir os nomes das colunas do DataFrame
print('\nNomes das colunas do DataFrame:')
print(df.columns)

# Exibir os indices do DataFrame
print('\nÍndices do DataFrame:')
print(df.index)

# obter o indice e colunas como listas
print('\nÍndices do DataFrame como lista:')
print(type(df.index.tolist()))

print('\nColunas do DataFrame como lista:')
print(type(df.columns.tolist()))

# Tamanho do DataFrame
print('\nTamanho do DataFrame:')
print(df.size)

# remover colunas desnecessárias
print('\nRemovendo colunas desnecessárias...')
df.drop(['AREA', 'REG', 'DEV', 'Type', 'Coverage'], axis=1, inplace=True)
print('Colunas removidas com sucesso!')
print(df.head(2))

# Renomear colunas para facilitar o acesso
print('\nRenomeando colunas para facilitar o acesso...')
df.rename(columns={'OdName': 'Pais', 'AreaName': 'Regiao', 'RegName': 'Continente'}, inplace=True)
print('Colunas renomeadas com sucesso!')

# Adicionar uma coluna 'Total' que é a soma de todas as colunas de anos
print('\nAdicionando coluna "Total" que é a soma de todas as colunas de anos...')
df['Total'] = df.sum(axis=1, numeric_only=True)
print('Coluna "Total" adicionada com sucesso!')
print(df.head(2))

# Verificar se há valores nulos no DataFrame
print('\nVerificando se há valores nulos no DataFrame...')
print(df.isnull().sum())

print('\nVerificando se há valores nulos no DataFrame (porcentagem):')
print(df.isnull().mean() * 100)

print(df.describe())

# Filtrando pela coluna Pais
print('\nFiltrando pela coluna "Pais"...')
# print(df['Pais'].head(10))
print(df.Pais)

# Filtrando coluna 'Pais' para verificar os dados de 'Brasil' e 'Japão'
print('\nFiltrando coluna "Pais" para verificar os dados de "Brasil" e "Japão"...')
lista_paises = ['Brazil', 'Japan', 'India','Chile']
# india_data = df[df['Pais'] == 'Brazil']
# print(india_data)
paises_filtrados = df[df['Pais'].isin(lista_paises)]
print(paises_filtrados)


# Filtrando coluna 'Pais' pelos anos de 1980 a 1985
print('\nFiltrando coluna "Pais" pelos anos de 1980 a 1985...')
filtro = df[['Pais', 1980, 1981, 1982, 1983, 1984, 1985]]
print(filtro.head(10))

# Definindo o índice do DataFrame para a coluna 'Pais'
print('\nDefinindo o índice do DataFrame para a coluna "Pais"...')
df.set_index('Pais', inplace=True)
print('Índice definido com sucesso!')
print(df.head(3))

# Verificando todas as imigracoes do japao
print('\nVerificando todas as imigrações do Japão...')
japan_data = df.loc['Japan']
print(japan_data)

# filtrando regiao
print('\nFiltrando por região "Asia"...')
asia_data = df[df['Regiao'] == 'Asia']
print(asia_data.head(10))

# Visualizando dados com matplotlib
print('\nVisualizando dados com matplotlib... versão do matplotlib: ', mpl.__version__)
print(plt.style.available)
mpl.style.use('ggplot')

# Grafico de imigracao do Haiti para o Canada
print('\nCriando gráfico de imigração do Haiti para o Canadá...')
haiti_data = df.loc['Haiti', 1980:2013]
print(haiti_data.head())

haiti_data.index = haiti_data.index.map(int)
haiti_data.plot(kind='line', figsize=(10, 6), title='Imigração do Haiti para o Canadá (1980-2013)', ylabel='Número de Imigrantes', xlabel='Ano')
plt.show()