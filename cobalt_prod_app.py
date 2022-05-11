# -*- coding: utf-8 -*-
"""
Created on Wed May 11 14:49:54 2022

@author: patta
"""

# # -*- coding: utf-8 -*-
# """
# Created on Sat Apr  9 17:17:43 2022

# @author: patta
# """
# -*- coding: utf-8 -*-
"""
Creator: Jasmine Pattany

please send inquiries to pattanyj@gmail.com
"""
#imports
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import networkx as nx
from pyvis.network import Network
import matplotlib.cm as cm
import matplotlib
# import matplotlib as mpl

#import files
data_2012_2014 =pd.read_csv('./network_product_data/all_2012_2014_data.csv')
data_2015_2017 =pd.read_csv('./network_product_data/all_2015_2017_data.csv')
data_2018_2020 =pd.read_csv('./network_product_data/all_2015_2017_data.csv')

st.title('Cobalt Trade Network')

# Network._repr_html_ = net_repr_html
st.sidebar.title('Select cobalt product:')
product=st.sidebar.selectbox('Select one',('HS12: 260500 - Cobalt ores and concentrates (1988-2500)',
'HS12: 750300 Waste and scrap, of nickel alloys (excl. ingots or other similar unwrought shapes, of remelted nickel alloys waste and scrap, ashes and residues containing nickel alloys)',
# 810530, #Cobalt waste and scrap (excl. ash and residues containingcobalt)(2002-2500)
'HS12: 810520 - Cobalt mattes and other intermediate products of cobalt metallurgy; unwrought cobalt; cobalt powders(2002-2500)',
'HS12: 750110 - Nickel mattes',
'HS12: 282200 - Cobalt oxides and hydroxides; commercial cobalt oxides(1988-2500)',
'HS12: 282739 - Cobalt chlorides(2007-2500)',
'HS12: 283329 - Sulphates of cobalt and of titanium(1988-2500)',
# 840610, #Turbines: steam and other vapour turbines, for marine propulsion
'HS12: 840681 - Turbines: steam and other vapour turbines, (for other than marine propulsion), of an output exceeding 40MW',
'HS12: 840682 - Turbines: steam and other vapour turbines, (for other than marine propulsion), of an output not exceeding 40MW',
'HS12: 840690 - Turbines: parts of steam and other vapour turbines',
# 841191, #Turbines: parts of turbo-jets and turbo-propellers
'HS12: 841199 - Turbines: parts of gas turbines (excluding turbo-jets and turbo-propellers)',
'HS12: 841810 - Refrigerators and freezers: combined refrigerator-freezers, fitted with separate external doors, electric or other',
# 841821, #Refrigerators: for household use, compression-type, electric or other"
# 841829, #Refrigerators: household, electric or not, other than compression-type"
'HS12: 841830 - Freezers: of the chest type, not exceeding 800l capacity',
'HS12: 841840 - Freezers: of the upright type, not exceeding 900l capacity',
'HS12: 841850 - Furniture incorporating refrigerating or freezing equipment: for storage and display, n.e.c. in item no. 8418.1, 8418.2, 8418.3 or 8418.4 (chests, cabinets, display counters, show-cases and the like)',
'HS12: 841861 - Heat pumps: other than air conditioning machines of heading no. 8415',
'HS12: 841869 - Refrigerating or freezing equipment: n.e.c. in heading no. 8418',
'HS12: 841891 - Refrigerating or freezing equipment: parts, furniture designed to receive refrigerating or freezing equipment',
'HS12: 841899 - Refrigerating or freezing equipment: parts thereof, other than furniture',
'HS12: 711510 - Metal: catalysts in the form of wire cloth or grill, of platinum',
'HS12: 850440 - Electrical static converters',
'HS12: 854140  - Electrical apparatus: photosensitive, including photovoltaic cells, whether or not assembled in modules or made up into panels, light emitting diodes',
))
year_range=st.sidebar.selectbox('Select a yearly range',('2012 to 2014','2015 to 2016','2018 to 2020',))
# trade_partners= st.slider('Minimum number of trade Partners', min_value=0, max_value=50, step=5)
tons_prod= st.slider('Minimum number of product traded (tons)', min_value=0, max_value=500, step=10)

if len(product) ==0:
    st.text('Please select 1 product to get started')
if len(year_range) ==0:
    st.text('Please select yearly range to get started')
 
else:
   
    if year_range=='2012 to 2014':

        #import wgi
        df_interact = pd.read_csv('./network_product_data/all_2012_2014_data.csv') 
        wgi_color = pd.read_csv('./data_pyvis/wgi_color.csv') 
        wgi_color = wgi_color.drop(columns=['country_code'])
        
        df_select = df_interact.merge(wgi_color, how='left' ,left_on='sources',right_on='country_name_full')
        df_select = df_select.drop(columns=['Unnamed: 0_x','Unnamed: 0_y']) #t','i','j','k','v'
        df_select = df_select.merge(wgi_color, how='left' ,left_on='targets',right_on='country_name_full')
        df_select = df_select.dropna()     
        df_select = df_select[df_select['q_total'] >= tons_prod]
        
        if product== 'HS12: 260500 - Cobalt ores and concentrates (1988-2500)':
            
            #CHANGE THIS VALUE!!!
            code = [260500]
            st.subheader('Cobalt ores and concentrates (1988-2500)')
            
        
            df_select = df_select[df_select['k'].isin(code)]
            
            # Create networkx graph object from pandas dataframe
            G = nx.from_pandas_edgelist(df_select, 'sources', 'targets', 'q_total')
            
            scale=100 # Scaling the size of the nodes by 1*degree
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
                nt.add_edge(row['country_code_x'], row['country_code_y'], width=20*(row['q_total'])/(df_select['q_total'].sum()))
            
            # Generate network with specific layout settings
            nt.repulsion(node_distance=300, central_gravity=0.01,
                                spring_length=150, spring_strength=0.05,
                                damping=0.95)
            
            # Save and read graph as HTML file (on Streamlit Sharing)
            try:
                path = '/tmp'
                nt.save_graph('HS12_260500.html')
                HtmlFile = open('HS12_260500.html', 'r', encoding='utf-8')
    
            # Save and read graph as HTML file (locally)
            except:
                path = '/html'
                nt.save_graph('HS12_260500.html')
                HtmlFile = open('HS12_260500.html', 'r', encoding='utf-8')
    

        
  

