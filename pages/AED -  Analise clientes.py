import funcoes 
import pandas as pd
import numpy as np
import streamlit as st
#import plotly.express as px

df_principal = funcoes.df_principal()#pegando o df principal em funcoes

#Começando por adicionar um sidebar
st.sidebar.title("Explicação breve: ")
st.sidebar.markdown("#### Aluno:")
st.sidebar.markdown("Carlos Rafael Senra Brito:")
st.sidebar.divider()
st.sidebar.markdown('Nesta página podemos realizar um breve reconhecimento dos dados que serão utilizados.')
st.sidebar.markdown('''  
                    * O primeiro grafico interativo se refere as variáveis categóricas do dataframe  
                    * O Segundo é referente as variaveis númericas
                    ''')


# separando em duas listas as variaveis categoricas e numericas do meu dataset
variaveis_cat = ['Education', 'Marital_Status','Kidhome','Teenhome',
                'AcceptedCmp1','AcceptedCmp2','AcceptedCmp3','AcceptedCmp4','AcceptedCmp5',
                'Complain','Response']
variaveis_num = ['Year_Birth','Income','Recency', 
                'MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts','MntGoldProds',
                'NumDealsPurchases', 'NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases', 'NumWebVisitsMonth']


st.title('Análise descritiva de clientes:')

st.markdown("### Contagem das categorias selecionada:")
st.write("Selecione uma variável categórica:")
categoricas = st.selectbox(" ",label_visibility ="collapsed",
                        options=[x for x in variaveis_cat])

grafico_barra = funcoes.barra_contagem(categoricas,df_principal)
st.plotly_chart(grafico_barra)

st.divider()
#histograma(coluna,dataframe,bins)
st.markdown("### Histograma da variavel selecionada:")
st.write("Selecione uma variável numérica:")
numericas = st.selectbox(" ",label_visibility ="collapsed",
                        options=[x for x in variaveis_num])
n_bins = st.slider('Selecione a quantidade de bins', 10, 60, 30)
grafico_hist = funcoes.histograma(numericas,df_principal,n_bins)
st.plotly_chart(grafico_hist)
