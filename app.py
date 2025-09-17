import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Configuração da página
st.set_page_config(page_title="Projetos com Notebooks + Py Ciência de Dados", layout="wide")

# TABS principais
tabs = st.tabs(["📊 Limpeza de Dados", "🧠 Funções Python", "📂 Operações com Listas", "🧠 Introdução à Ciência de Dados"])

# --- Limpeza de Dados ---
with tabs[0]:
    st.title("📘 Projeto: Visualização de Notebooks")
    st.markdown("---")
    st.subheader("📊 Limpeza e Preparação de Dados")
    st.markdown("Demonstrações de como importar, limpar e preparar dados em um dataset.")

    with st.expander("📥 Importação de bibliotecas"):
        st.code("import pandas as pd\nimport numpy as np", language="python")

    with st.expander("📄 Leitura e visualização inicial"):
        st.code('df = pd.read_csv("DADOS_ALUNOS.csv", sep=";")\ndf.head()', language="python")

    with st.expander("🔍 Verificação e tratamento de dados ausentes"):
        st.code('df.isnull().sum()\ndf["Nota"] = df["Nota"].fillna(0)', language="python")

    with st.expander("🧹 Remoção de duplicatas e renomeação"):
        st.code('df = df.drop_duplicates()\ndf = df.rename(columns={"Nota": "Nota_Final"})\ndf.head()', language="python")

# --- Funções ---
with tabs[1]:
    st.subheader("🧠 Funções em Python")
    st.markdown("Exemplos de criação e uso de funções, incluindo parâmetros padrão e retornos múltiplos.")

    with st.expander("🙋‍♀️ Saudação personalizada"):
        st.code("""
def saudacao(nome):
    return f"Olá, {nome}!"
""", language="python")

    with st.expander("📐 Função com parâmetro padrão"):
        st.code("""
def potencia(base, expoente=2):
    return base ** expoente

potencia(3)      # 3² = 9
potencia(3, 3)   # 3³ = 27
""", language="python")

    with st.expander("🔁 Retorno múltiplo"):
        st.code("""
def operacoes(a, b):
    soma = a + b
    sub = a - b
    return soma, sub

s, sub = operacoes(10, 5)
print(f"Soma: {s}, Subtração: {sub}")
""", language="python")

    with st.expander("💬 Repetição com argumentos nomeados"):
        st.code("""
def mensagem(texto, vezes=1):
    for _ in range(vezes):
        print(texto)

mensagem("Estudando funções", 3)
""", language="python")

# --- Listas e Operações ---
with tabs[2]:
    st.subheader("📂 Operações com Listas (2CDD02)")
    st.markdown("Códigos para manipulação de listas e estruturas em Python.")

    with st.expander("➕ Soma e média"):
        st.code("""
lista = [1, 2, 3, 4, 5]
soma = sum(lista)
media = soma / len(lista)
print(f"Soma: {soma}, Média: {media}")
""", language="python")

    with st.expander("📐 Quadrados com list comprehension"):
        st.code("""
quadrados = [x**2 for x in lista]
print("Quadrados:", quadrados)
""", language="python")

    with st.expander("📍 Enumerando elementos"):
        st.code("""
for i, valor in enumerate(lista):
    print(f"Índice: {i}, Valor: {valor}")
""", language="python")

    with st.expander("📏 Fatiamento e modificação"):
        st.code("""
print(lista[1:4])  # do segundo ao quarto elemento

lista.append(6)
lista.remove(2)
print(lista)
""", language="python")

# --- Introdução à Ciência de Dados ---
with tabs[3]:
    st.title("🧠 Py - Sua Porta de Entrada para a Ciência de Dados")
    st.subheader("Aprenda Ciência de Dados do zero com Python de forma prática!")
    
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

    st.markdown("---")
    st.header("🔢 O que são Dados?")
    st.write("""
Dados são **informações brutas**, que ainda precisam ser organizadas para fazer sentido.

Exemplos de dados:
- Números de vendas
- Notas de alunos
- Temperaturas registradas ao longo do dia
""")

    st.markdown("---")
    st.header("🧱 Tipos de Dados")
    st.write("""
- **Numéricos** (int, float): 10, 3.14  
- **Texto (strings)**: "Olá", "Ciência"  
- **Booleanos**: `True`, `False`  
- **Categorias**: "Masculino", "Feminino", "Outros"
""")

    st.markdown("---")
    st.header("🐍 Primeiros passos com Python")
    st.write("""
O Python é uma linguagem simples e poderosa, perfeita para Ciência de Dados. Vamos começar com alguns exemplos básicos:
""")

    st.subheader("✅ Exemplo 1: Olá, Mundo!")
    code_1 = '''
# Exemplo de código em Python
print("Olá, mundo da Ciência de Dados com Py!")
'''
    st.code(code_1, language="python")

    st.subheader("✅ Exemplo 2: Trabalhando com Variáveis")
    code_2 = '''
# Criando variáveis
nome = "Ana"
idade = 25
print(nome, idade)
'''
    st.code(code_2, language="python")

    st.markdown("---")
    st.header("📦 Bibliotecas úteis")

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

    dados = {
        "Nome": ["Ana", "Carlos", "Beatriz"],
        "Idade": [23, 35, 29]
    }
    df = pd.DataFrame(dados)
    st.dataframe(df)

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

    fig, ax = plt.subplots()
    ax.bar(df['Nome'], df['Idade'], color='mediumseagreen')
    ax.set_title('Idade por Pessoa')
    ax.set_xlabel('Nome')
    ax.set_ylabel('Idade')
    st.pyplot(fig)

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

    idades = np.array([23, 35, 29])
    media = np.mean(idades)
    st.write(f"Média das idades: {media}")

    st.markdown("---")
    st.header("📊 Análise Simples de Dados")
    st.write("""
Vamos realizar algumas análises simples nos dados:
""")

    st.subheader("📈 Estatísticas Descritivas")
    st.write("""
O método `describe()` retorna estatísticas úteis sobre um DataFrame, como média, desvio padrão, mínimo e máximo.
""")
    code_6 = '''
df.describe()
'''
    st.code(code_6, language="python")

    st.dataframe(df.describe())

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

    mais_velha = df[df["Idade"] == df["Idade"].max()]
    st.write(mais_velha)

    st.markdown("---")
    st.header("🎯 Mini Projeto: Notas de Alunos")
    st.write("""
Vamos analisar as notas de alguns alunos e criar um gráfico de barras:
""")

    notas = {
        "Aluno": ["João", "Maria", "Pedro", "Ana"],
        "Nota": [7.5, 9.0, 6.0, 8.5]
    }

    notas_df = pd.DataFrame(notas)
    st.dataframe(notas_df)

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

    fig, ax = plt.subplots()
    ax.bar(notas_df["Aluno"], notas_df["Nota"], color="orange")
    ax.set_title("Notas dos Alunos")
    ax.set_ylim(0, 10)
    st.pyplot(fig)

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
