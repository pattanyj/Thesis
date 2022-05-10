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
import numpy as np
# import matplotlib.pyplot as plt

# import matplotlib as mpl
# from matplotlib import colors
# from math import e




st.title('Cobalt Trade Network')

#Network._repr_html_ = net_repr_html
st.sidebar.title('Select cobalt product:')
product=st.sidebar.selectbox('Select one',('Cells and Batteries: primary lithium','X', 'Y'))
year_range=st.sidebar.selectbox('Select a yearly range',('2018 to 2020','X','Y'))
# trade_partners= st.slider('Minimum number of trade Partners', min_value=0, max_value=50, step=5)
# tons_prod= st.slider('Minimum number of product traded (tons)', min_value=0, max_value=100000, step=100)


if len(product) ==0:
    st.text('Please select 1 product to get started')
if len(year_range) ==0:
    st.text('Please select yearly range to get started')
 
else:
   
    if product=='Cells and Batteries: primary lithium' and year_range=='2018 to 2020':
        df_interact = pd.read_csv('./data_pyvis/li_2018_to_2020.csv') 
        
        # 'df_select = set selection criteria'
        df_select = df_interact.dropna(axis=0)
        
        #import wgi
        wgi_color = pd.read_csv('./data_pyvis/wgi_color.csv') 
        wgi_color = wgi_color.drop(columns=['IndexAvg','country_code'])
        
        # Create networkx graph object from pandas dataframe
        #calculate degree centrality
        G = nx.from_pandas_edgelist(df_select, 'sources', 'targets', 'q_total')
        # d = nx.coloring.equitable_color(G, num_colors=3)
        # nx.algorithms.coloring.equitable_coloring.is_equitable(G, d)
        
        scale=1 # Scaling the size of the nodes by 1*degree
        d = dict(G.degree)
        #Updating dict
        d.update((x, scale*y) for x, y in d.items())
        #Setting up size attribute
        nx.set_node_attributes(G,d,'size')
        
        # Initiate PyVis network object
        net_2018_2020 = Network(height="1000px", width="100%", directed=True, bgcolor='white', font_color='black')   #

        # Take Networkx graph and translate it to a PyVis graph format
        net_2018_2020.from_nx(G)
         

        # # Generate network with specific layout settings
        # net_2018_2020.repulsion(node_distance=420, central_gravity=0.33,
        #                     spring_length=110, spring_strength=0.10,
        #                     damping=0.95)

       
        # Save and read graph as HTML file (on Streamlit Sharing)
        try:
            path = '/tmp'
            net_2018_2020.save_graph('LI_1820.html')
            HtmlFile = open('LI_1820.html', 'r', encoding='utf-8')

        # Save and read graph as HTML file (locally)
        except:
            path = '/html'
            net_2018_2020.save_graph('LI_1820.html')
            HtmlFile = open('LI_1820.html', 'r', encoding='utf-8')


        # Load HTML file in HTML component for display on Streamlit page
        components.html(HtmlFile.read(), height = 1200,width=1000, scrolling = True)
        
        df_interact = pd.read_csv('./data_pyvis/li_2018_to_2020.csv')
        HtmlFile = open("./html/HS6_850650.html", 'r', encoding='utf-8')
        
  


# if option=='GOT':
#   HtmlFile = open("gameofthrones.html", 'r', encoding='utf-8')
#   source_code = HtmlFile.read() 
#   components.html(source_code, height = 1200,width=1000)


# if option=='Karate':
#   HtmlFile = open("karate.html", 'r', encoding='utf-8')
#   source_code = HtmlFile.read() 
#   components.html(source_code, height = 1200,width=1000)