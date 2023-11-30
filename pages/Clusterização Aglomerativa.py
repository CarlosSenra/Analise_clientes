import funcoes 
import pandas as pd
import numpy as np
import streamlit as st
#import plotly.express as px

df_principal = funcoes.df_principal('marketing_campaign.csv', '\t')

Mnt_data = funcoes.df_Mnt(df_principal)

Mnt_prop = funcoes.cria_df_com_proporcao(funcoes.cria_df_com_total(Mnt_data) ,coluna = 'Total')

Mnt_prop.set_index('ID',inplace = True)

agg_Mnt = funcoes.cluster(Mnt_prop).agg_cluster(n_clusters= 4 ,
                                                metric = 'euclidean',
                                                linkage = 'ward')

clientes_cluster = Mnt_prop.index

df_Mnt_clusters_agg = pd.DataFrame({'cliente_int_id':clientes_cluster,
                                    'cluster_cliente_Mnt_agg':agg_Mnt})

df_Mnt_agg = Mnt_data.copy()

df_Mnt_agg = df_Mnt_agg.merge(df_Mnt_clusters_agg, how='inner', left_on='ID', right_on='cliente_int_id')
df_Mnt_agg = df_Mnt_agg[['cliente_int_id','MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts',
                         'MntSweetProducts', 'MntGoldProds', 'cluster_cliente_Mnt_agg']]

medio, contagem = funcoes.cliente_medio_cluster(df_Mnt_agg)

df_principal_cluster = funcoes.add_cluster_df_original(df_Mnt_agg, df_principal)

#------------------------------------------------ Streamlit code
st.sidebar.markdown("#### Autor:")
st.sidebar.markdown("[Carlos Rafael Senra Brito](https://www.linkedin.com/in/carlos-senra/)")
st.sidebar.divider()
st.sidebar.markdown('Nesta página podemos realizar a aplicação de um modelo de Clusterização Hierárquica Aglomerativo.')



st.title('Clusterização de Clientes com modelo Aglomerativo')

st.markdown('''
            A clusterização hierárquica é um método de análise de dados que agrupa elementos semelhantes em clusters, formando uma estrutura de árvore ou dendrograma. 
            Esse modelo tem a característica de criar uma hierarquia de clusters, onde cada elemento inicialmente forma seu próprio cluster e, gradualmente, clusters 
            são combinados com base em sua similaridade.
            ''')

st.markdown('''
            ### Tratamento de dados
            ''')

st.markdown('''
            Para a aplicação do modelo farei uso somente de algumas das colunas do dataframe original, na primeira seção do projeto existe os dados de gasto do cliente,
            que mostra o valor gasto na categoria do produto nos últimos 2 anos. Sendo assim é possível realizar uma clusterização em relação ao que os clientes compraram
            nos últimos anos.

            No projeto foi realizado uma clusterização baseando-se na proporção de gasto dos clientes, uma vez que se espera que clientes que gastam em categorias especificas
            de produtos proporcionalmente a outros clientes tenham caracteristicas de compras parecidas. No entanto pode surgir um questionamento, será que a quantidade 
            gasto nas categorial não é tão relevante quanto as proporções e com isso deveria aplicar isso ao modelo ? Mas isso depende da análise, pois o quanto clientes 
            gastou em determidados produtos é motivo para estudar outra caracteristica do cliente, sendo assim para próximos passos é valido fazer esta clusterização.
            ''')

st.markdown('''
            Voltando ao centro do projeto, para a clusterização da proporção de gastos, para cada cliente foi calculado o total de gastos de cada individuo
            e para cada categoria foi calculada a proporção de gastos.
            ''')

st.dataframe(Mnt_data.head())

st.markdown('''
            Calculado o total de gastos de cada individuo, em seguida calculando a proporção de gastos por categoria temos :
            ''')


st.dataframe(Mnt_prop.head())


st.title('Ánalise de Dendograma')

st.markdown('''
            Fazendo uso do dataframe a cima foi feito o dendograma para termos uma ideia ds clusters.
            ''')


funcoes.dendogram_code()


st.image('Dendograma1.png')


st.markdown('''
            É válido observar do dendograma acima é que naturamente existem dois clusters, bem distantes um do outro e que em cada um desses clusters se dividem em mais dois com distâncias
            relevantes, o que nos leva a acreditar que uma clusterização com quatro clusters seria a melhor ou uma das melhores opções.
            ''')


st.title('Resultado da clusterização')

st.markdown('''
            Aplicando o modelo de clusterização hierarquica com quatro clusters obtivemos clusters com caracteristicas médias e tamanhos apresentados abaixo:
            ''')

st.table(medio)

st.table(contagem)