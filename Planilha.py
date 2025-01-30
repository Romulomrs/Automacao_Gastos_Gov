import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./Arquivo./despesasPorOrgao.csv', delimiter=';')
df = pd.DataFrame(data)

# Substituir as vírgulas por pontos
df['Valor Empenhado'] = df['Valor Empenhado'].str.replace(',', '.')

# Remover os pontos de milhar (deve ser antes da conversão para numérico)
df['Valor Empenhado'] = df['Valor Empenhado'].str.replace('.', '', regex=False)

# conversão para valores numéricos
df['Valor Empenhado'] = pd.to_numeric(df['Valor Empenhado'], errors='coerce')

# Filtrando os dados
ministerio_fazenda = df[df['Órgão Superior'].str.contains('Ministério da Fazenda')]
outros = df[~df['Órgão Superior'].str.contains('Ministério da Fazenda')]

# Somando os valores dos outros órgãos
outros_total = outros['Valor Empenhado'].sum()

# Criando uma nova DataFrame para incluir "Outros"
df_final = pd.DataFrame({
    'Órgão Superior': ['Ministério da Fazenda', 'Outros'],
    'Valor Empenhado': [ministerio_fazenda['Valor Empenhado'].sum(), outros_total]
})

# Plotando o gráfico de pizza
plt.figure(figsize=(7, 7))
plt.pie(
    df_final['Valor Empenhado'], 
    labels=df_final['Órgão Superior'], 
    autopct='%1.1f%%', 
    startangle=90, 
    colors=plt.cm.Paired.colors
)
plt.title('Distribuição do Valor Empenhado por Órgão (%)', fontsize=14)
plt.axis('equal')  # Para manter o formato circular
plt.show()
