import utils.datafile as util
import matplotlib as mpl
import matplotlib.pyplot as plt

def metodo_procedural(top5):
    # Criando o gráfico de área
    print(f'Criando o gráfico de área...')
    top5.plot(kind='area', alpha=0.25, stacked=False, figsize=(20, 10))
    plt.title('Número de Imigrantes para o Canadá (1980-2013) - Top 5 Países')
    plt.xlabel('Ano')
    plt.ylabel('Número de Imigrantes')
    plt.legend(title='Países', loc='upper left')
    plt.grid(True)
    plt.show()

def metodo_orientado_objeto(def_imigrantes, transparencia, descricao):
    # Criando o gráfico de área usando orientação a objetos
    print(f'Criando o gráfico de área usando orientação a objetos...')
    fig, ax = plt.subplots(figsize=(20, 10))
    def_imigrantes.plot(kind='area', alpha=transparencia, stacked=False, ax=ax)
    ax.set_title(f'Número de Imigrantes para o Canadá (1980-2013) - {descricao}')
    ax.set_xlabel('Ano')
    ax.set_ylabel('Número de Imigrantes')
    ax.legend(title='Países', loc='upper left')
    ax.grid(True)
    plt.show()

print('### Visualização de Dados ###')
print(f'Carregando os dados do arquivo "Canada.xlsx"...')

# Carregar os dados do arquivo Excel
try:
    df = util.load_file('datasets', 'Canada.xlsx', 'xlsx')
    print('\nDados carregados com sucesso!')
except Exception as e:
    print(f'Erro ao carregar os dados: {e}')
    exit()

print('\nInicializando o DataFrame...')
try:
    util.initializa_df_canada(df)
    print('\nDataFrame inicializado com sucesso!')
except Exception as e:
    print(f'Erro ao inicializar o DataFrame: {e}')
    exit()

print('\n')
print('Informações do DataFrame...')
print(f'Dimensões do DataFrame: {df.shape}')
print(f'Número total de elementos no DataFrame: {df.size}')
print(f'Número de colunas no DataFrame: {len(df.columns)}')
print(f'Número de linhas no DataFrame: {len(df.index)}')

# Visualização de dados usando um gráfico de área
mpl.style.use('ggplot')
print(f'Visualizando dados usando um gráfico de área... versão do Matplotlib: {mpl.__version__}')

# Obtem as 5 primeiras linhas do DataFrame
top5 = df.head()

# Transpondo o DataFrame para facilitar a plotagem
print(f'Realizando a transposição do DataFrame para facilitar a plotagem...')
years = list(map(str, range(1980, 2014)))
top5 = top5[years].transpose()

# Modificando os valores do índice para o formato inteiro para facilitar a leitura do gráfico
print(f'Modificando os valores do índice para o formato inteiro para facilitar a leitura do gráfico...')
top5.index = top5.index.map(int)

# Gerando o gráfico de área usando o mét0do procedural
# metodo_procedural(top5)

# Gerando o gráfico de área usando o mét0do orientado a objetos
# metodo_orientado_objeto(top5, 0.35, 'Top 5 Países')

# Obtem os ultimos 5 países do DataFrame
bottom5 = df.tail()
bottom5 = bottom5[years].transpose()
bottom5.index = bottom5.index.map(int)

# Gerando o gráfico de área usando o mét0do orientado a objetos para os ultimos 5 países
# metodo_orientado_objeto(bottom5, 0.45, 'Ultimos 5 Países')