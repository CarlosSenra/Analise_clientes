import pandas as pd
import numpy as np
import plotly.express as px
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering, KMeans, BisectingKMeans
import streamlit as st

# --------------- funçoes que retornam dataframes
def df_principal(nome_df,separador)->pd.pandas:
    '''
    função que retorna o df principal de clientes
    '''
    df_principal = pd.read_csv(nome_df, sep=separador)
    return df_principal


def df_Mnt(df:pd.pandas)->pd.pandas:
   '''
   função que retorna os dados de tipos de produtos que o cliente comprou
   '''
   Mnt_data  = df[['ID',
                'MntWines', 'MntFruits',
                'MntMeatProducts', 'MntFishProducts', 
                'MntSweetProducts', 'MntGoldProds']]
   return Mnt_data


def df_Num(df:pd.pandas)->pd.pandas:
   Num_data = df[['ID',
               'NumWebPurchases','NumCatalogPurchases', 
               'NumStorePurchases']] 
   return Num_data



def cliente_medio_cluster(df_com_cluster):  
    df_com_cluster = df_com_cluster.drop(columns = ['cliente_int_id'])
    medio = df_com_cluster.groupby(by=df_com_cluster.columns[-1]).mean()
    contagem = df_com_cluster[df_com_cluster.columns[-1]].value_counts()

    return medio, contagem


def add_cluster_df_original(df_com_cluster, df_original):
    df_aux1 = df_com_cluster[['cliente_int_id',df_com_cluster.columns[-1]]]
    df = df_aux1.merge(df_original, how='inner', right_on='ID', left_on='cliente_int_id')
    
    return df.drop(columns=['ID'])


#----------


#---------- fonçoes de tratamento de dados para calcular a proporçao dos clientes
def cria_df_com_total(dataframe): 
    '''
    retorna um df com uma coluna que soma os valores das colunas por linha
    '''
    df = dataframe.copy()
    soma = lambda row : np.sum(row)
    df.set_index('ID',inplace=True)
    df['Total'] = df.apply(soma,axis=1)
    df.reset_index(inplace =True)
    return df

def cria_df_com_proporcao(dataframe,coluna = 'Total'): 
    '''
    pega a coluna de um df que é o 'Total' e divide todo df por essa coluna, retornando
    um dataframe de proporção das variaveis
    '''
    df = dataframe.copy()
    df.set_index('ID',inplace=True)
    df = df.div(df[coluna],axis=0)
    df.drop(columns=coluna,inplace = True)
    df.reset_index(inplace =True)
    return df

#------------

#------------ funcoes que retornam graficos

def barra_contagem(coluna,dataframe):
  df = pd.DataFrame({coluna : dataframe[coluna].value_counts().sort_values(ascending=False).index,
                    'Count':dataframe[coluna].value_counts().sort_values(ascending=False).values})

  fig = px.bar(df, x=coluna, y='Count', text_auto=True)
  return fig


def histograma(coluna,dataframe,bins):
  df = dataframe[coluna]

  fig = px.histogram(df, x=coluna, nbins=bins, text_auto=True)
  fig.update_layout(bargap=0.1)
  return fig


#------

#------ classe de clusters

class cluster:
    #classe de cluster
    def __init__(self,df):
        self.df = df
        
        
    def agg_cluster(self,
                    n_clusters= 4 ,
                    metric = 'euclidean',
                    linkage = 'ward'):
        
        clustering = AgglomerativeClustering(n_clusters = n_clusters,
                                             metric = metric,
                                             linkage = linkage)
        
        return clustering.fit_predict(self.df)
    
    def kmeans(self,
               n_clusters=4,
               n_init = 20,
               max_iter = 2000,
               random_state = None):
        clustering = KMeans(n_clusters=n_clusters,
                            n_init = n_init,
                            max_iter = max_iter,
                            random_state = random_state)
        clustering.fit(self.df)
        inercia = clustering.inertia_
        clusters = clustering.fit_predict(self.df)
        return clusters, inercia
        
    
    def bisc_kmeans(self,
               n_clusters=4,
               n_init = 20,
               max_iter = 2000,
               random_state = None):
        clustering = BisectingKMeans(n_clusters=n_clusters,
                                     n_init = n_init,
                                     max_iter = max_iter,
                                     random_state = random_state)
        clustering.fit(self.df)
        inercia = clustering.inertia_
        clusters = clustering.fit_predict(self.df)
        return clusters, inercia 
    





#---------- mostra codigo do dendograma na clusterização hierarquica
def dendogram_code():
    with st.expander("Veja o código do Dendograma"):
      code = '''
              import numpy as np
              import matplotlib.pyplot as plt
              import scipy.cluster.hierarchy as sch

              linkage_matrix = sch.linkage(Mnt_prop, method='ward')

              fig, ax = plt.subplots()
              dendrogram = sch.dendrogram(linkage_matrix,p=11, ax=ax)

              plt.yticks(range(0,17,2))
              plt.grid(linestyle=':',axis='y')
              plt.title('Dendograma das proporções da quantidade de compras do cliente')
              plt.show()
            '''
      st.code(code, language='python')




#------- funcoes para dash
def df_filtrado_cluster(dataframe,cluster):
   return dataframe[dataframe.iloc[:,1] == cluster]

def media_coluna_clusterizado(dataframe,nome_coluna,cluster,casas_decimais) -> str:
    df_filtrado = dataframe[dataframe.iloc[:,1] == cluster]
    media = round(df_filtrado[nome_coluna].mean(),casas_decimais)
    return str(media)

def contagem_coluna_clusterizado(dataframe,nome_coluna,cluster) -> str:
    df_filtrado = dataframe[dataframe.iloc[:,1] == cluster]
    media = df_filtrado[nome_coluna].count()
    return str(media)

def barra_h_contagem_cluster(coluna,dataframe,cluster):
  df_filtrado = dataframe[dataframe.iloc[:,1] == cluster]
  df = pd.DataFrame({coluna : df_filtrado[coluna].value_counts().sort_values(ascending=True).index,
                    'Count':df_filtrado[coluna].value_counts().sort_values(ascending=True).values})

  fig = px.bar(df, x='Count', y=coluna, text_auto=True, orientation='h')
  return fig

def histograma_cluster(coluna,dataframe,bins,cluster):
  df_filtrado = dataframe[dataframe.iloc[:,1] == cluster]
  df = df_filtrado[coluna]

  fig = px.histogram(df, x=coluna, nbins=bins, text_auto=True)
  fig.update_layout(bargap=0.1)
  return fig