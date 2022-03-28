# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 14:22:33 2022

@author: patta
"""

# Import dependencies
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import networkx as nx
from pyvis.network import Network


# Read dataset
# libattery_nodes_2018 = pd.read_csv('./network_product_data/libattery_nodes_2018.csv')
# libattery_nodes_2019 = pd.read_csv('./network_product_data/libattery_nodes_2019.csv')
# libattery_nodes_2020 = pd.read_csv('./network_product_data/libattery_nodes_2020.csv')
libattery_nodes = pd.read_csv('./network_product_data/libattery_nodes_2019_subtract_2020.csv')

# Set header title
st.title('Network Graph Visualization of Lithium Ion Trade Interactions')

# Define selection options and sort alphabetically
HS12_country = pd.read_csv('./BACI_HS12/country_codes_V202201.csv',encoding='unicode_escape')


country_list = list(HS12_country['country_name_full'])
country_list.sort()

# Implement multiselect dropdown menu for option selection
selected_countries = st.multiselect('Select country or countries to visualize', country_list)

# Set info message on initial site load
if len(selected_countries) == 0:
    st.text('Choose at least 1 country to get started')

# Create network graph when user selects >= 1 item
else:
    df_select = libattery_nodes.loc[libattery_nodes['targets'].isin(selected_countries) | \
                                libattery_nodes['sources'].isin(selected_countries)]
    df_select = df_select.reset_index(drop=True)

# Create networkx graph object from pandas dataframe
    G = nx.from_pandas_edgelist(libattery_nodes,'sources', 'targets', 'q')
    
    # Initiate PyVis network object
    drug_net = Network(height='465px', bgcolor='#222222', font_color='white')


# Take Networkx graph and translate it to a PyVis graph format   
    drug_net.from_nx(G)
    
    # Generate network with specific layout settings
    drug_net.repulsion(node_distance=420, central_gravity=0.33,
                       spring_length=110, spring_strength=0.10,
                       damping=0.95)

    # Save and read graph as HTML file (on Streamlit Sharing)
    try:
        path = '/tmp'
        drug_net.save_graph('Plots/2019-2020_LithiumIon.html')
        HtmlFile = open('Plots/2019-2020_LithiumIon.html', 'r', encoding='utf-8')

    # Save and read graph as HTML file (locally)
    except:
        path = '/html_files'
        drug_net.save_graph('Plots/2019-2020_LithiumIon.html')
        HtmlFile = open('Plots/2019-2020_LithiumIon.html', 'r', encoding='utf-8')

    # Load HTML file in HTML component for display on Streamlit page
    components.html(HtmlFile.read(), height=435)