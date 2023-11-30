import funcoes 
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

df_principal = funcoes.df_principal('marketing_compaign_agg_clusters.csv',',')#pegando o df principal em funcoes
df_principal.drop(columns=['Unnamed: 0'],inplace=True)

clusters_num = np.sort(df_principal.iloc[:,1].unique())


# separando em duas listas as variaveis categoricas e numericas do meu dataset
variaveis_cat = ['Education', 'Marital_Status','Kidhome','Teenhome',
                'AcceptedCmp1','AcceptedCmp2','AcceptedCmp3','AcceptedCmp4','AcceptedCmp5',
                'Complain','Response']
variaveis_num = ['Year_Birth','Income','Recency', 
                'MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts','MntGoldProds',
                'NumDealsPurchases', 'NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases', 'NumWebVisitsMonth']


#Começando por adicionar um sidebar
st.sidebar.markdown("#### Autor:")
st.sidebar.markdown("[Carlos Rafael Senra Brito](https://www.linkedin.com/in/carlos-senra/)")
st.sidebar.divider()
st.sidebar.markdown('Nesta página está o Dashboard geral dos clusters, como ele podemos comparar as caracteristicas médias dos clusters.')


st.title('Dashboard Geral Cluster Aglomerativo')
with st.container():
    st.divider()
    col1, col2 = st.columns([20,80])
    with col1:
        st.markdown('#### Selecione o Cluster:')
        cluster_select = st.selectbox(" ",label_visibility ="collapsed",
                                  options=clusters_num)
        st.divider()
        
        with st.container():
            cluster_df = df_principal[df_principal.iloc[:,1] == cluster_select]
            with st.container():
                _, col0 = st.columns([15,85])
                with col0:
                    st.markdown('&nbsp; &nbsp; &nbsp;&nbsp;&nbsp; Qnt. Clientes:')
                    st.markdown(f'### &nbsp;&nbsp;&nbsp;&nbsp; &nbsp; &nbsp; {len(cluster_df)}')

            with st.container():    
                st.divider()
                _, col0 = st.columns([15,85])
                with col0:
                    st.markdown('&nbsp; &nbsp; &nbsp;&nbsp;&nbsp; Média Income:')
                    st.markdown(f'### &nbsp;&nbsp;&nbsp; R$ {funcoes.media_coluna_clusterizado(df_principal,"Income",cluster_select,2)}')
                    
            with st.container():
                st.divider()
                _, col0 = st.columns([15,85])
                with col0:
                    st.markdown(' Média ano nascimento:')
                    st.markdown(f'### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp; {funcoes.media_coluna_clusterizado(df_principal,"Year_Birth",cluster_select,0)}')
            
            with st.container():
                st.divider()
                _, col0 = st.columns([13,87])
                with col0:
                    st.markdown('Média Compras com Desconto:')
                    st.markdown(f'### &nbsp;&nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; {funcoes.media_coluna_clusterizado(df_principal,"NumDealsPurchases",cluster_select,0)}')
        

    with col2:
        with st.container():
            col1_1, col2_1, col3_1, col4_1, col5_1, col6_1 = st.columns(6)
            
            col1_1.markdown('Média Consumo Vinho:')
            col1_1.markdown(f'### &nbsp; &nbsp; &nbsp; R$ {funcoes.media_coluna_clusterizado(df_principal,"MntWines",cluster_select,2)}')
            
            col2_1.markdown('Média Consumo Fruta:')
            col2_1.markdown(f'### &nbsp; &nbsp; &nbsp; R$ {funcoes.media_coluna_clusterizado(df_principal,"MntFruits",cluster_select,2)}')

            col3_1.markdown('Média Consumo Carne:')
            col3_1.markdown(f'### &nbsp; &nbsp; &nbsp; R$ {funcoes.media_coluna_clusterizado(df_principal,"MntMeatProducts",cluster_select,2)}')
            
            col4_1.markdown('Média Consumo Peixe:')
            col4_1.markdown(f'### &nbsp; &nbsp; &nbsp; R$ {funcoes.media_coluna_clusterizado(df_principal,"MntFishProducts",cluster_select,2)}')
            
            col5_1.markdown('Média Consumo Doce:')
            col5_1.markdown(f'### &nbsp; &nbsp; &nbsp; R$ {funcoes.media_coluna_clusterizado(df_principal,"MntSweetProducts",cluster_select,2)}')
            
            col6_1.markdown('Média Consumo Ouro:')
            col6_1.markdown(f'### &nbsp; &nbsp; &nbsp; R$ {funcoes.media_coluna_clusterizado(df_principal,"MntGoldProds",cluster_select,2)}')
            st.divider()
        with st.container():
            col1_1, col2_1 = st.columns([70,30])
            with col1_1:
                st.write("Selecione uma variável numérica:")
                numericas = st.selectbox(" ",label_visibility ="collapsed",
                                        options=[x for x in variaveis_num])
                n_bins = st.slider('Selecione a quantidade de bins', 10, 60, 30)
                grafico_hist = funcoes.histograma_cluster(numericas,df_principal,n_bins,cluster_select)
                st.plotly_chart(grafico_hist, use_container_width=True)

            with col2_1:
                st.write("Selecione uma variável categórica:")
                categoricas = st.selectbox(" ",label_visibility ="collapsed",
                                        options=[x for x in variaveis_cat])

                grafico_h_barra = funcoes.barra_h_contagem_cluster(categoricas,df_principal,cluster_select)
                st.plotly_chart(grafico_h_barra, use_container_width=True)

            
                
          






            