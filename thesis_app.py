# # -*- coding: utf-8 -*-
# """
# Created on Sat Apr  9 17:17:43 2022

# @author: patta
# """
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
import matplotlib.cm as cm
import matplotlib
import matplotlib as mpl





st.title('Cobalt Trade Network')

# Network._repr_html_ = net_repr_html
st.sidebar.title('Select cobalt product:')
product=st.sidebar.selectbox('Select one',('Cells and Batteries: primary lithium','X', 'Y'))
year_range=st.sidebar.selectbox('Select a yearly range',('2018 to 2020','X','Y'))
# trade_partners= st.slider('Minimum number of trade Partners', min_value=0, max_value=50, step=5)
tons_prod= st.slider('Minimum number of product traded (tons)', min_value=0, max_value=500, step=10)


if len(product) ==0:
    st.text('Please select 1 product to get started')
if len(year_range) ==0:
    st.text('Please select yearly range to get started')
 
else:
   
    if product=='Cells and Batteries: primary lithium' and year_range=='2018 to 2020':

        #import wgi
        df_interact = pd.read_csv('./network_product_data/TEST_NETWORK_2018.csv') 
        wgi_color = pd.read_csv('./data_pyvis/wgi_color.csv') 
        #wgi_color = wgi_color.drop(columns=['country_code'])
    
        df_select = df_interact.merge(wgi_color, how='left' ,left_on='sources',right_on='country_name_full')
        df_select = df_select.drop(columns=['Unnamed: 0_x','Unnamed: 0_y','t','i','j','k','v'])
        df_select = df_select.merge(wgi_color, how='left' ,left_on='targets',right_on='country_name_full')
        df_select = df_select.dropna()    
        df_select = df_select[df_select['q'] >= tons_prod]
        
        # Create networkx graph object from pandas dataframe
        G = nx.from_pandas_edgelist(df_select, 'sources', 'targets', 'q')
        # d = nx.coloring.equitable_color(G, num_colors=3)
        # nx.algorithms.coloring.equitable_coloring.is_equitable(G, d)
        
        scale=500 # Scaling the size of the nodes by 1*degree
        d = dict(nx.betweenness_centrality(G, normalized = True, endpoints = False))
        #Updating dict
        d.update((x, scale*y) for x, y in d.items())
        
        
        #nodes dataframe
        d = pd.DataFrame.from_dict(d, orient='index').reset_index()
        d.columns = ['country', 'bet_centrality']
        nodes_s = df_select[['sources', 'country_code_x', 'IndexAvg_x', 'color_x']]
        nodes_t = df_select[['targets', 'country_code_y', 'IndexAvg_y', 'color_y']]
        nodes_cols = ['country', 'country_code', 'WGI', 'color']
        nodes_s.columns = nodes_cols
        nodes_t.columns = nodes_cols
        nodes = pd.concat([nodes_s, nodes_t]).drop_duplicates().reset_index(drop=True)
        nodes = pd.merge(nodes, d, how='inner', on='country')
        

        nt = Network(height="1000px", width="100%", directed=True, bgcolor='white', font_color='black')
        nt.add_nodes(list(nodes['country_code']),
        label = list(nodes['country']),
        size = list(nodes['bet_centrality']),
        color = [matplotlib.colors.rgb2hex(cm.RdYlGn(x)) for x in nodes['WGI']])
        #color = list(nodes['color']))
        
        
        for index, row in df_select.iterrows():
            nt.add_edge(row['country_code_x'], row['country_code_y'], width=20*(row['q'])/(df_select['q'].sum()))
        
        # Generate network with specific layout settings
        nt.repulsion(node_distance=500, central_gravity=0.01,
                            spring_length=150, spring_strength=0.20,
                            damping=0.95)
        
        # Save and read graph as HTML file (on Streamlit Sharing)
        try:
            path = '/tmp'
            nt.save_graph('LI_1820.html')
            HtmlFile = open('LI_1820.html', 'r', encoding='utf-8')

        # Save and read graph as HTML file (locally)
        except:
            path = '/html'
            nt.save_graph('LI_1820.html')
            HtmlFile = open('LI_1820.html', 'r', encoding='utf-8')


        # Load HTML file in HTML component for display on Streamlit page
        components.html(HtmlFile.read(), height = 800,width=800, scrolling = True)
        
        df_interact = pd.read_csv('./data_pyvis/li_2018_to_2020.csv')
        HtmlFile = open("./html/HS6_850650.html", 'r', encoding='utf-8')
        
  

