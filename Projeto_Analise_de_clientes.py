import streamlit as st
import funcoes


st.title('Dinâmica de clientes')

col1, _ = st.columns(2)
with col1:
    st.markdown('''### Autor do projeto:  
                Carlos Rafael Senra Brito''')
    
st.markdown('## Resumo')
st.markdown('''A ideia central deste projeto tem com o intuito de realizar uma analise descritiva detalhada de um dataset que pode ser encontrado em
            <https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis>. Onde em seguida será realizada uma série de clusterizações com 
            o intuito de descobrir quais informações os clusters retornados por algoritimos diferentes retornam.  
            Inicialmente realizo uma análise exploratória de dados presente em "AED -  Analise clientes" e em seguida serão adicionadas
            as analises mais complexas.''')



st.markdown('## Informações do dataset:')
st.markdown('''
            #### Dados demográficos e de comportamento

            * ID: Identificador único do cliente
            * Year_Birth: Ano de nascimento do cliente
            * Education: Nível de escolaridade do cliente
            * Marital_Status: Estado civil do cliente
            * Income: Renda anual familiar do cliente
            * Kidhome: Número de crianças na casa do cliente
            * Teenhome: Número de adolescentes na casa do cliente
            * Dt_Customer: Data de inscrição do cliente na empresa
            * Recency: Número de dias desde a última compra do cliente
            * Complain: 1 se o cliente reclamou nos últimos 2 anos, 0 caso contrário

            #### Dados de gastos

            * MntWines: Valor gasto em vinho nos últimos 2 anos
            * MntFruits: Valor gasto em frutas nos últimos 2 anos
            * MntMeatProducts: Valor gasto em produtos de carne nos últimos 2 anos
            * MntFishProducts: Valor gasto em produtos de peixe nos últimos 2 anos
            * MntSweetProducts: Valor gasto em doces nos últimos 2 anos
            * MntGoldProds: Valor gasto em produtos de ouro nos últimos 2 anos

            #### Dados de participação em campanhas promocionais

            * NumDealsPurchases: Número de compras feitas com desconto
            * AcceptedCmp1: 1 se o cliente aceitou a oferta na 1ª campanha, 0 caso contrário
            * AcceptedCmp2: 1 se o cliente aceitou a oferta na 2ª campanha, 0 caso contrário
            * AcceptedCmp3: 1 se o cliente aceitou a oferta na 3ª campanha, 0 caso contrário
            * AcceptedCmp4: 1 se o cliente aceitou a oferta na 4ª campanha, 0 caso contrário
            * AcceptedCmp5: 1 se o cliente aceitou a oferta na 5ª campanha, 0 caso contrário
            * Response: 1 se o cliente aceitou a oferta na última campanha, 0 caso contrário

            #### Dados de canais de compra

            * NumWebPurchases: Número de compras feitas pelo site da empresa
            * NumCatalogPurchases: Número de compras feitas usando um catálogo
            * NumStorePurchases: Número de compras feitas diretamente nas lojas
            * NumWebVisitsMonth: Número de visitas ao site da empresa no último mês
            ''')


st.divider()

st.markdown('O código será atualizado com o passar de tempo')