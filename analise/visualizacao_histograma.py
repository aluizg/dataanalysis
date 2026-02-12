
import utils.datafile as util
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

from analise.visualizacao_dados_area_plot import years


def histrograma(df, ano):
    # Criando o histograma
    print(f'Criando o histograma para o ano de {ano}...')
    count, bins = np.histogram(df[ano], bins=10)
    print(f'Contagem de imigrantes por faixa de valores: {count}')
    print(f'Faixas de valores (bins): {bins}')

    plt.figure(figsize=(10, 6))
    plt.hist(df[ano], bins=10, alpha=0.7, color='blue')
    plt.title(f'Histograma do Número de Imigrantes para o Canadá em {ano}')
    plt.xlabel('Número de Imigrantes')
    plt.ylabel('Frequência')
    plt.grid(True)
    plt.show()

def histograma_lista_paises(df, lista_paises, lista_anos):
    # Criando o histograma para uma lista de países e anos
    print(f'Criando o histograma para os países: {lista_paises}...')
    df_filtro = df.loc[lista_paises, lista_anos].transpose()
    count, bins = np.histogram(df_filtro.values.flatten(), bins=10)
    print(f'Contagem de imigrantes por faixa de valores: {count}')
    print(f'Faixas de valores (bins): {bins}')

    # Configuracao para gerar o grafico via matplotlib
    plt.figure(figsize=(10, 6))
    ax = plt.gca()
    df_filtro.plot(kind='hist', ax=ax)
    plt.title(f'Histograma do Número de Imigrantes para o Canadá - Países: {", ".join(lista_paises)}')
    plt.xlabel('Número de Imigrantes')
    plt.ylabel('Numero de anos')
    plt.grid(True)
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
print('Visualizando dados do ano de 2013 com Histograma e Boxplot...')
print(df['2013'].head())

# Criando o histograma
count, bins = np.histogram(df['2013'], bins=10)
print(f'Contagem de imigrantes por faixa de valores: {count}')
print(f'Faixas de valores (bins): {bins}')
# histrograma(df, '2013')

histograma_lista_paises(df, ['Denmark', 'Norway', 'Sweden'], years)