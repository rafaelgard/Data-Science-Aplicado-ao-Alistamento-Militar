#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd


# In[ ]:


# Importa o dataframe inicial
df = pd.read_csv("H:/Análises Python/Alistamento militar/sermil2007.csv", 
                 sep=",", 
                 encoding='ANSI', 
                 low_memory=False)

# Importando os 11 dataframes restantes

# O próximo dataframe após o inicial começa pelo ano 2008
i = 2008
while i < 2020:
    # Arquivos com encodificação ANSI
    if i <= 2016 or i == 2018:
        
        
        # Cria o nome da variável que armazenará o dataframe do ano
        nome_banco_importado = "sermil" + str(i)
        

        banco_importado = pd.read_csv("H:/Análises Python/Alistamento militar/" + nome_banco_importado + ".csv",
                                      sep=",",
                                      encoding='ANSI', 
                                      low_memory=False)
        

        # Faz um append para acrescentar o banco recém importado ao banco principal
        df = df.append(banco_importado)
        print("Banco ", i, " importado")
        

        # Atribui um dataframe vazio ao ultimo dataframe importado para liberar memória ram
        banco_importado = pd.DataFrame()

        i = i + 1
        
    # Arquivos com encodificação UTF-8
    if i == 2017 or i == 2019:
        # Cria o nome da variável que armazenará o dataframe do ano
        nome_banco_importado = "sermil" + str(i)
        banco_importado = pd.read_csv("H:/Análises Python/Alistamento militar/" + nome_banco_importado + ".csv", 
            sep=",",
            encoding='UTF-8', 
            low_memory=False)

        # Faz um append para acrescentar o banco recem importado ao banco principal
        df = df.append(banco_importado)
        print("Banco ", i, " importado")

        # Atribui um dataframe vazio ao ultimo dataframe importado para liberar memória ram
        banco_importado = pd.DataFrame()

        i = i + 1


# ## Verificando os dados únicos de cada coluna

# In[ ]:


print('=================================================')
for coluna in df.columns:
    print('Coluna: ', coluna)
    print(np.unique(df[coluna], return_counts = True)[0])
    print('=================================================')


# Verificando a coluna escolaridade é possível identificar uma série de valores dististos, buscando uma melhor comprensão eles serão substituidos por valores que estão de acordo com a nova nomeclatura do sistema de ensino brasileiro conforme a lei n° 144/2005

# Visando padronizar a classificação da escolaridade foi criado um dicionário para fazer a padronização dos valores. Este dicionário foi importado e posteriormente foi gerada uma lista de replaces que foram executados no próximo bloco de comando para substituir os valores antigos pelos novos.

# In[ ]:


#Importa o dicionário
dicionario = pd.read_csv("Alistamento militar/Dicionario_series.csv",sep=";",encoding='ANSI')

#Substitui os valores no padrão antigo pelos novos
i=0
while i<46:
    df['ESCOLARIDADE']=df['ESCOLARIDADE'].replace(dicionario['Valores_antigos'][i],dicionario['Valores_novos'][i])
    i=i+1
    
print("Valores atualizados")


# In[ ]:


# Salva o dataframe atulizado em formato .csv
df.to_csv("H:/Análises Python/Alistamento militar/df_atualizado_utf8.csv", sep=",", encoding='UTF-8')

print("O banco de dados atualizado foi salvo")

