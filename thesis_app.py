# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 17:17:43 2022

@author: patta
"""
#imports
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import networkx as nx
from pyvis.network import Network

st.title('Hello Pyvis')

#Network._repr_html_ = net_repr_html
st.sidebar.title('Select cobalt product:')
product=st.sidebar.selectbox('Select one',('Cells and Batteries: primary lithium','X', 'Y'))
year_range=st.multiselect.selectbox('Select a yearly range',('2018 to 2020','X','Y'))
trade_partners= st.slider('Minimum number of trade Partners', min_value=0, max_value=50, step=5)
tons_prod= st.slider('Minimum number of product traded (tons)', min_value=0, max_value=100000, step=100)



if len(product) ==0:
    st.text('Please select 1 product to get started')
if len(year_range) ==0:
    st.text('Please select yearly range to get started')
 
else:
    
    if product=='Cells and Batteries: primary lithium' and year_range=='2018 to 2020':
        df_interact = pd.read_csv('./data_pyvis/li_2018_to_2020.csv')
        HtmlFile = open("./html/HS6_850650.html", 'r', encoding='utf-8')
        
        # source_code = HtmlFile.read() 
        
        # if trade_partners==int:
        #     for country in df_interact['sources','targets']:
        #         source_count = df_interact['sources'].isin(list(country).count()
        #         target_count = df_interact['targets'].isin(list(country).count()                                      
        #         source_count+target_count >= trade_partners
        # if tons_prod=int:
        #     for ton in df_interact['sources','targets']
              
      # source_code = HtmlFile.read() 
      # components.html(source_code, height = 1200,width=1000)
  


# if option=='GOT':
#   HtmlFile = open("gameofthrones.html", 'r', encoding='utf-8')
#   source_code = HtmlFile.read() 
#   components.html(source_code, height = 1200,width=1000)


# if option=='Karate':
#   HtmlFile = open("karate.html", 'r', encoding='utf-8')
#   source_code = HtmlFile.read() 
#   components.html(source_code, height = 1200,width=1000)