import pandas as pd
import numpy as np
import plotly.express as px 


# grafico de barras - para as varaiveis categoricas dos dados
def barra_contagem(coluna,dataframe):
  df = pd.DataFrame({coluna : dataframe[coluna].value_counts().sort_values(ascending=False).index,
                    'Count':dataframe[coluna].value_counts().sort_values(ascending=False).values})

  fig = px.bar(df, x=coluna, y='Count', text_auto=True)
  return fig




#Histograma
def histograma(coluna,dataframe,bins):
  df = dataframe[coluna]

  fig = px.histogram(df, x=coluna, nbins=bins, text_auto=True)
  fig.update_layout(bargap=0.1)
  return fig