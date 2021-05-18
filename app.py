import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import plotly.express as px
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import math

def read_data(csv):
    dataframe = pd.read_csv(csv)
    return dataframe

def forward_filling(pd_dataframe):
    pd_dataframe_new = pd_dataframe.ffill(axis=0)
    return pd_dataframe_new

def backward_filling(pd_dataframe):
    pd_dataframe_new = pd_dataframe.bfill(axis=0)
    return pd_dataframe_new

def data_cleaning(csv):
    dfd = read_data(csv)
    dfd = forward_filling(dfd)
    dfd = backward_filling(dfd)
    return dfd



st.title('Gapminder')

@st.cache
def data_preprocessing():
    df1 = data_cleaning('E:/HWR Course/Big data/Streamlit/life_expectancy_years.csv')
    df2 = data_cleaning('E:/HWR Course/Big data/Streamlit/ny_gnp_pcap_pp_cd.csv')
    df3 = data_cleaning('E:/HWR Course/Big data/Streamlit/population_total.csv')
    df1 = df1.melt(id_vars=['country'],var_name=['year'], value_name='life_expectancy')
    df2 = df2.melt(id_vars=['country'],var_name=['year'], value_name='GNI_perCapita')
    df3 = df3.melt(id_vars=['country'],var_name=['year'], value_name='Population')
    df_final = df1.merge(df2, how='outer', on =('country', 'year')).merge(df3, how='outer', on=('country', 'year'))
    df_final = df_final.fillna(0)
    df_final['year'] = df_final['year'].astype(str).astype(int)
    return df_final

df = data_preprocessing()

st.sidebar.title(f"Selection")
gdp_year = st.sidebar.slider("Select Year ",min_value=1990, max_value=2020, step=1, value=2018)
gdp_country = st.sidebar.multiselect("Select Region", df.country.unique().tolist(), default='Germany')

fig = px.scatter(df.loc[(df['year'] == gdp_year) & (df['country'].isin(gdp_country))] , x="GNI_perCapita", y="life_expectancy", text="country", log_x=True, size='Population')
    
st.plotly_chart(fig, use_container_width=True)
    

    


