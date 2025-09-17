# app.py
import streamlit as st
import pandas as pd
import numpy as np

# Configuração da página
st.set_page_config(page_title="Py - Introdução à Ciência de Dados", layout="wide")

# Cabeçalho principal
st.title("🧠 Py - Sua Porta de Entrada para a Ciência de Dados")
st.subheader("Aprenda Ciência de Dados do zero com Python de forma prática!")

# Seção: O que é Ciência de Dados
st.markdown("---")
st.header("📌 O que é Ciência de Dados?")
st.write("""
**Ciência de Dados** é o processo de coletar, organizar, analisar e interpretar dados para tomar decisões informadas.

Ela envolve:
- Estatísticas
- Programação (Python é a linguagem mais usada!)
- Visualização de dados
- Conhecimento do domínio (entender o problema)
""")

# Seção: O que são Dados
st.markdown("---")
st.header("🔢 O que são Dados?")
st.write("""
Dados são **informações brutas**, que ainda precisam ser organizadas para fazer sentido.

Exemplos de dados:
- Números de vendas
- Notas de alunos
- Temperaturas registradas ao longo do dia
""")

# Seção: Tipos de Dados
st.markdown("---")
st.header("🧱 Tipos de Dados")
st.write("""
- **Numéricos** (int, float): 10, 3.14  
- **Texto (strings)**: "Olá", "Ciência"  
- **Booleanos**: `True`, `False`  
- **Categorias**: "Masculino", "Feminino", "Outros"
""")

# Seção: Começando com Python
st.markdown("---")
st.header("🐍 Primeiros passos com Python")
st.write("""
O Python é uma linguagem simples e poderosa, perfeita para Ciência de Dados. Vamos começar com alguns exemplos básicos:
""")

# Exemplo 1: Olá Mundo
st.subheader("✅ Exemplo 1: Olá, Mundo!")
code_1 = '''
# Exemplo de código em Python
print("Olá, mundo da Ciência de Dados com Py!")
'''
st.code(code_1, language="python")

# Exemplo 2: Trabalhando com variáveis
st.subheader("✅ Exemplo 2: Trabalhando com Variáveis")
code_2 = '''
# Criando variáveis
nome = "Ana"
idade = 25
print(nome, idade)
'''
st.code(code_2, language="python")

# Seção: Bibliotecas úteis
st.markdown("---")
st.header("📦 Bibliotecas úteis")

# pandas
st.subheader("🐼 pandas – Para trabalhar com tabelas")
st.write("""
A biblioteca `pandas` facilita a manipulação de dados em forma de tabelas (DataFrames). Vamos ver um exemplo:
""")
code_3 = '''
import pandas as pd

# Criando um DataFrame com pandas
dados = {
    "Nome": ["Ana", "Carlos", "Beatriz"],
    "Idade": [23, 35, 29]
}

df = pd.DataFrame(dados)
df
'''
st.code(code_3, language="python")

# Exibindo DataFrame
dados = {
    "Nome": ["Ana", "Carlos", "Beatriz"],
    "Idade": [23, 35, 29]
}
df = pd.DataFrame(dados)
st.dataframe(df)

# matplotlib
st.subheader("📊 matplotlib – Para criar gráficos")
st.write("""
A biblioteca `matplotlib` é útil para criar gráficos simples. Veja como fazer um gráfico de barras:
""")
code_4 = '''
import matplotlib.pyplot as plt

# Gráfico de barras
plt.bar(df["Nome"], df["Idade"])
plt.title("Idade por Pessoa")
plt.xlabel("Nome")
plt.ylabel("Idade")
plt.show()
'''
st.code(code_4, language="python")

# Gerando o gráfico no Streamlit
fig, ax = plt.subplots()
ax.bar(df['Nome'], df['Idade'], color='mediumseagreen')
ax.set_title('Idade por Pessoa')
ax.set_xlabel('Nome')
ax.set_ylabel('Idade')
st.pyplot(fig)

# numpy
st.subheader("🔢 numpy – Para cálculos e arrays")
st.write("""
A biblioteca `numpy` é ideal para realizar cálculos numéricos. Vamos calcular a média das idades:
""")
code_5 = '''
import numpy as np

# Calculando a média das idades
idades = np.array([23, 35, 29])
media = np.mean(idades)
print("Média das idades:", media)
'''
st.code(code_5, language="python")

# Média das idades no Streamlit
idades = np.array([23, 35, 29])
media = np.mean(idades)
st.write(f"Média das idades: {media}")

# Seção: Análise simples de dados
st.markdown("---")
st.header("📊 Análise Simples de Dados")
st.write("""
Vamos realizar algumas análises simples nos dados:
""")

# Estatísticas descritivas
st.subheader("📈 Estatísticas Descritivas")
st.write("""
O método `describe()` retorna estatísticas úteis sobre um DataFrame, como média, desvio padrão, mínimo e máximo.
""")
code_6 = '''
df.describe()
'''
st.code(code_6, language="python")

# Exibindo estatísticas no Streamlit
st.dataframe(df.describe())

# Exemplo: Encontrando a pessoa mais velha
st.subheader("🔍 Quem é a pessoa mais velha?")
st.write("""
Vamos encontrar quem tem a maior idade no DataFrame.
""")
code_7 = '''
# Encontrando a pessoa mais velha
mais_velha = df[df["Idade"] == df["Idade"].max()]
mais_velha
'''
st.code(code_7, language="python")

# Exibindo a pessoa mais velha
mais_velha = df[df["Idade"] == df["Idade"].max()]
st.write(mais_velha)

# Seção: Mini Projeto - Notas de Alunos
st.markdown("---")
st.header("🎯 Mini Projeto: Notas de Alunos")
st.write("""
Vamos analisar as notas de alguns alunos e criar um gráfico de barras:
""")

# Dados das notas
notas = {
    "Aluno": ["João", "Maria", "Pedro", "Ana"],
    "Nota": [7.5, 9.0, 6.0, 8.5]
}

notas_df = pd.DataFrame(notas)
st.dataframe(notas_df)

# Gráfico das notas
st.subheader("📊 Gráfico das Notas")
st.write("""
Agora, vamos criar um gráfico para visualizar as notas dos alunos.
""")
code_8 = '''
import matplotlib.pyplot as plt

# Gráfico das notas
plt.bar(notas_df["Aluno"], notas_df["Nota"], color="orange")
plt.title("Notas dos Alunos")
plt.ylim(0, 10)
plt.show()
'''
st.code(code_8, language="python")

# Gerando o gráfico no Streamlit
fig, ax = plt.subplots()
ax.bar(notas_df["Aluno"], notas_df["Nota"], color="orange")
ax.set_title("Notas dos Alunos")
ax.set_ylim(0, 10)
st.pyplot(fig)

# Seção: Conclusão
st.markdown("---")
st.header("✅ Conclusão")
st.write("""
Parabéns! 🎉 Você aprendeu:
- O que é Ciência de Dados
- Como usar Python para manipulação e visualização de dados
- Criar gráficos e fazer análises simples

Agora, você pode seguir aprendendo:
- Limpeza de dados
- Trabalhar com arquivos CSV
- Modelos de machine learning

Continue sua jornada em Ciência de Dados com o **Py**!
""")

