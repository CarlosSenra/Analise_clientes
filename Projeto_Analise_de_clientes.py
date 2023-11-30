import streamlit as st
import funcoes

st.title('Dinâmica de clientes')


col1, _ = st.columns(2)
with col1:
    st.markdown('### Autor do projeto:')  
    st.markdown('[Carlos Rafael Senra Brito](https://www.linkedin.com/in/carlos-senra/)')
st.markdown('''
            # Introdução

            Toda empresa tem seus respectivos clientes, sendo os mesmos possuidores de características, onde estas podem ser as mais diversificadas possíveis. 
            Para um negócio dar certo é imprescindível o entendimento de personalidade de seus clientes, como o que eles compram ou os seus hábitos quando utilizam algum serviço da empresa. 
            Neste sentido são esses tipos de informações que ajudam na tomada de decisão do grande escalão empresarial, em determinadas jogadas de criação de produtos, determinação de promoção 
            direcionada a clientes específicos ou até mesmo sistema de recomendação de produtos.

            O objetivo do atual a trabalho consiste em aplicar uma análise descritiva dos dados, para um entendimento geral e em seguida a aplicação de clusterização de clientes, 
            com intuito de descobrir quais caracteristicas, que tais clusters, podem informar sobre os clientes. Para esta etapa foi utilizado o agrupamento hierarquico utilizando funções 
            já implementadas do [Scipy](https://docs.scipy.org/doc/scipy/reference/cluster.hierarchy.html#module-scipy.cluster.hierarchy) e 
            [Scikit-learn](https://scikit-learn.org/stable/modules/clustering.html#clustering) para clusterização de dados.
''')


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
