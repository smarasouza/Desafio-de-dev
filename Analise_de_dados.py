import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt


# Carregar o conjunto de dados
# Substitua 'seu_arquivo.csv' pelo caminho do seu arquivo de dados
dados = pd.read_csv('seu_arquivo.csv')

# Exibir as primeiras linhas do conjunto de dados
print("Visualizando as primeiras linhas do conjunto de dados:")
print(dados.head())

# Informações gerais sobre o conjunto de dados
print("\nInformações gerais sobre o conjunto de dados:")
print(dados.info())

# Estatísticas descritivas
print("\nEstatísticas descritivas:")
print(dados.describe())

# Verificar valores ausentes
print("\nVerificando valores ausentes:")
print(dados.isnull().sum())

# Visualização de dados
# Substitua 'coluna1' e 'coluna2' pelos nomes das colunas do seu conjunto de dados
plt.figure(figsize=(10, 6))
sns.scatterplot(data=dados, x='coluna1', y='coluna2')
plt.title('Relação entre coluna1 e coluna2')
plt.show()

# Matriz de correlação
plt.figure(figsize=(10, 8))
sns.heatmap(dados.corr(), annot=True, cmap='coolwarm')
plt.title('Matriz de Correlação')
plt.show()

# Salvando os dados limpos (se necessário)
# Substitua 'dados_limpos.csv' pelo nome desejado para o arquivo de saída
dados.to_csv('dados_limpos.csv', index=False)
print("\nDados limpos salvos em 'dados_limpos.csv'.")