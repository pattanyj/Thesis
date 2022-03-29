# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 13:50:53 2022

@author: patta
"""
# check for PYVIS filtering - streamlit (FIGURE OUT HOW)
# Looking at 2019 and 2020 and subtract them to replot the network
# we can see what is going on in a specific country and see what the context is
# column country then check the connections, way out and way in.
# top 20 imp/exp
# check quantities
# check connections
# if you find some missing data check comtrade
# check another product
# maybe 2019 discrepency bc 2019 values were reported in 2020 - when year ended

#%%
import pandas as pd
from pyvis.network import Network
import networkx as nx
import matplotlib.pyplot as plt
# import streamlit as st
# import streamlit.components.v1 as components

#import HS07 files
HS07_2019 = pd.read_csv('./clean_BACI/HS07/clean_BACI_HS07_Y2019_V202201.csv')
HS07_2020 = pd.read_csv('./clean_BACI/HS07/clean_BACI_HS07_Y2020_V202201.csv')

# #import HS12 files
HS12_2018 = pd.read_csv('./clean_BACI/HS12/clean_BACI_HS12_Y2018_V202201.csv')
HS12_2019 = pd.read_csv('./clean_BACI/HS12/clean_BACI_HS12_Y2019_V202201.csv')
HS12_2020 = pd.read_csv('./clean_BACI/HS12/clean_BACI_HS12_Y2020_V202201.csv')

#import country name files
HS07_country = pd.read_csv('./BACI_HS07/country_codes_V202201.csv',encoding='unicode_escape')
HS12_country = pd.read_csv('./BACI_HS12/country_codes_V202201.csv',encoding='unicode_escape')

#MERGE
#HS12

#2018
merge = HS12_2018.merge(HS12_country, left_on='i',right_on='country_code')
merge = merge.rename({'country_name_full':'sources'},axis='columns')
merge = merge.drop(columns=['Unnamed: 0','country_code','country_name_abbreviation','iso_2digit_alpha','iso_3digit_alpha'])
HS12_2018_final = merge.merge(HS12_country, left_on='j',right_on='country_code')
HS12_2018_final = HS12_2018_final.rename({'country_name_full':'targets'},axis='columns')
HS12_2018_final = HS12_2018_final.drop(columns=['country_code','country_name_abbreviation','iso_2digit_alpha','iso_3digit_alpha'])

#2019
merge_1 = HS12_2019.merge(HS12_country, left_on='i',right_on='country_code')
merge_1 = merge_1.rename({'country_name_full':'sources'},axis='columns')
merge_1 = merge_1.drop(columns=['Unnamed: 0','country_code','country_name_abbreviation','iso_2digit_alpha','iso_3digit_alpha'])
HS12_2019_final = merge_1.merge(HS12_country, left_on='j',right_on='country_code')
HS12_2019_final = HS12_2019_final.rename({'country_name_full':'targets'},axis='columns')
HS12_2019_final = HS12_2019_final.drop(columns=['country_code','country_name_abbreviation','iso_2digit_alpha','iso_3digit_alpha'])

#2020
merge_2 = HS12_2020.merge(HS12_country, left_on='i',right_on='country_code')
merge_2 = merge_2.rename({'country_name_full':'sources'},axis='columns')
merge_2 = merge_2.drop(columns=['Unnamed: 0','country_code','country_name_abbreviation','iso_2digit_alpha','iso_3digit_alpha'])
HS12_2020_final = merge_2.merge(HS12_country, left_on='j',right_on='country_code')
HS12_2020_final = HS12_2020_final.rename({'country_name_full':'targets'},axis='columns')
HS12_2020_final = HS12_2020_final.drop(columns=['country_code','country_name_abbreviation','iso_2digit_alpha','iso_3digit_alpha'])

#collecting df for lithium ion batteries
code = [850650]
libattery_nodes_2018 = HS12_2018_final[HS12_2018_final['k'].isin(code)]
libattery_nodes_2019 = HS12_2019_final[HS12_2019_final['k'].isin(code)]
libattery_nodes_2020 = HS12_2020_final[HS12_2020_final['k'].isin(code)]
#%%

new_df = pd.merge(libattery_nodes_2020, libattery_nodes_2019,  how='left', left_on=['sources','targets'], right_on = ['sources','targets'], )
libattery_nodes = new_df #.fillna(0)
libattery_nodes['q'] = libattery_nodes['q_x'] - libattery_nodes['q_y']
libattery_nodes = libattery_nodes.fillna(0)
libattery_nodes = libattery_nodes.drop(columns = ['i_y','j_y','k_y','v_y']).sort_values(by='q', ascending=False)
libattery_nodes.to_csv('./network_product_data/libattery_nodes_2020_subtract_2019.csv')

# group by exports
libattery_nodes_exports = libattery_nodes.groupby('sources').sum().reset_index().sort_values(by='q', ascending=False)
libattery_nodes_exports.to_csv('./network_product_data/libattery_nodes_exports_2020_subtract_2019.csv')
libattery_nodes_imports = libattery_nodes.groupby('targets').sum().reset_index().sort_values(by='q', ascending=False)
libattery_nodes_imports.to_csv('./network_product_data/libattery_nodes_imports_2020_subtract_2019.csv')

#%%
libattery_nodes_2018.to_csv('./network_product_data/libattery_nodes_2018.csv')
libattery_nodes_2019.to_csv('./network_product_data/libattery_nodes_2019.csv')
libattery_nodes_2020.to_csv('./network_product_data/libattery_nodes_2020.csv')
#%% Biggest importers/exporters NAMES

#2018
imp_2018 = libattery_nodes_2018.groupby('sources').sum().reset_index().sort_values(by='q', ascending=False)
imp_2018_names = imp_2018['sources'].head(10).to_list()
exp_2018 = libattery_nodes_2018.groupby('targets').sum().reset_index().sort_values(by='q', ascending=False)
exp_2018_names = exp_2018['targets'].head(10).to_list()

#2019
imp_2019 = libattery_nodes_2019.groupby('sources').sum().reset_index().sort_values(by='q', ascending=False)
imp_2019_names = imp_2019['sources'].head(10).to_list()
exp_2019 = libattery_nodes_2019.groupby('targets').sum().reset_index().sort_values(by='q', ascending=False)
exp_2019_names = exp_2019['targets'].head(10).to_list()

#2020
imp_2020 = libattery_nodes_2020.groupby('sources').sum().reset_index().sort_values(by='q', ascending=False)
imp_2020_names = imp_2020['sources'].head(10).to_list()
exp_2020 = libattery_nodes_2020.groupby('targets').sum().reset_index().sort_values(by='q', ascending=False)
exp_2020_names = exp_2020['targets'].head(10).to_list()

#unique names
top_imp = imp_2018_names+imp_2019_names+imp_2020_names 
set_imp = set(top_imp)
top_imp =  list(set_imp)

top_exp =exp_2018_names+exp_2019_names+exp_2020_names
set_exp = set(top_exp)
top_exp =  list(set_exp)

top_combined = top_imp+top_exp
set_combined = set(top_combined)
top_combined =  list(set_combined)
#%% Networkx 2018

# Generate a networkx graph
G = nx.from_pandas_edgelist(libattery_nodes_2018, source = 'sources', target = 'targets', edge_attr = 'q', create_using=nx.DiGraph)
#add edge attribute for q 

# G = nx.DiGraph(G)

# Give the graph a name
G.name = '2018 LI Battery Trade Network'

# Obtain general information of graph
print(nx.info(G))

# Get graph density
density = nx.density(G)
print("Network density:", density)

from operator import itemgetter

# Create dictionary to store degrees of nodes
degree_dict = dict(G.degree(G.nodes()))
nx.set_node_attributes(G, degree_dict, 'degree')

# Generate sorted list of tuples of drug entity and corresponding degree
sorted_degree = sorted(degree_dict.items(), key=itemgetter(1), reverse=True)

print("Top 20 countries by degree (2019):")
for d in sorted_degree[:20]:
    print(d)

#Degree Centrality
deg_centrality_2019 = nx.degree_centrality(G)
# in_deg_centrality_2019 = nx.in_degree_centrality(G)
# out_deg_centrality_2019 = nx.out_degree_centrality(G)
# bet_centrality_2019 = nx.betweenness_centrality(G, normalized = True, endpoints = False)
# print(deg_centrality_2019)

# #plot
# plt.figure(figsize =(15, 15))
# nx.draw_networkx(G, with_labels = True)
# plt.show()

# Out degree calc
way_out_deg_2018 = G.out_degree(weight='q')
way_out_deg_2018_df = pd.DataFrame(list(way_out_deg_2018), columns =['country', 'way_out_2018'])

# Way in calculation
way_in_deg_2018 = G.in_degree(weight='q')
way_in_deg_2018_df = pd.DataFrame(list(way_in_deg_2018), columns =['country', 'way_in_2018'])

#%% Networkx 2019

# Generate a networkx graph
G = nx.from_pandas_edgelist(libattery_nodes_2019, source = 'sources', target = 'targets', edge_attr = 'q', create_using=nx.DiGraph)
#add edge attribute for q 

# G = nx.DiGraph(G)

# Give the graph a name
G.name = '2019 LI Battery Trade Network'

# Obtain general information of graph
print(nx.info(G))

# Get graph density
density = nx.density(G)
print("Network density:", density)

from operator import itemgetter

# Create dictionary to store degrees of nodes
degree_dict = dict(G.degree(G.nodes()))
nx.set_node_attributes(G, degree_dict, 'degree')

# Generate sorted list of tuples of drug entity and corresponding degree
sorted_degree = sorted(degree_dict.items(), key=itemgetter(1), reverse=True)

print("Top 20 countries by degree (2019):")
for d in sorted_degree[:20]:
    print(d)

#Degree Centrality
deg_centrality_2019 = nx.degree_centrality(G)
# in_deg_centrality_2019 = nx.in_degree_centrality(G)
# out_deg_centrality_2019 = nx.out_degree_centrality(G)
# bet_centrality_2019 = nx.betweenness_centrality(G, normalized = True, endpoints = False)
# print(deg_centrality_2019)

# #plot
# plt.figure(figsize =(15, 15))
# nx.draw_networkx(G, with_labels = True)
# plt.show()

# Out degree calc
way_out_deg_2019 = G.out_degree(weight='q')
way_out_deg_2019_df = pd.DataFrame(list(way_out_deg_2019), columns =['country', 'way_out_2019'])

# Way in calculation
way_in_deg_2019 = G.in_degree(weight='q')
way_in_deg_2019_df = pd.DataFrame(list(way_in_deg_2019), columns =['country', 'way_in_2019'])


#%% Networkx 2020

# Generate a networkx graph
G = nx.from_pandas_edgelist(libattery_nodes_2020,  source = 'sources', target = 'targets', edge_attr = 'q', create_using=nx.DiGraph)

# Give the graph a name
G.name = '2020 LI Battery Trade Network'

# Obtain general information of graph
print(nx.info(G))

# Get graph density
density = nx.density(G)
print("Network density:", density)

from operator import itemgetter

# Create dictionary to store degrees of nodes
degree_dict = dict(G.degree(G.nodes()))
nx.set_node_attributes(G, degree_dict, 'degree')

# Generate sorted list of tuples of drug entity and corresponding degree
sorted_degree = sorted(degree_dict.items(), key=itemgetter(1), reverse=True)

print("Top 20 countries by degree (2020):")
for d in sorted_degree[:20]:
    print(d)
    
#Degree Centrality
deg_centrality_2020 = nx.degree_centrality(G)
in_deg_centrality_2020 = nx.in_degree_centrality(G)
out_deg_centrality_2020 = nx.out_degree_centrality(G)
bet_centrality_2020 = nx.betweenness_centrality(G, normalized = True, endpoints = False)
# print(deg_centrality_2019)

#plot
# plt.figure(figsize =(15, 15))
# nx.draw_networkx(G, with_labels = True)
# plt.show()

# Out degree calc
way_out_deg_2020 = G.out_degree(weight='q')
way_out_deg_2020_df = pd.DataFrame(list(way_out_deg_2020), columns =['country', 'way_out_2020'])

way_in_deg_2020 = G.in_degree(weight='q')
way_in_deg_2020_df = pd.DataFrame(list(way_in_deg_2020), columns =['country', 'way_in_2020'])

#%% Merge to get wayin/out matrix

#2018
centrality_2018 = way_out_deg_2018_df.merge(way_in_deg_2018_df, left_on='country',right_on='country')

#2019
centrality_2019 = way_out_deg_2019_df.merge(way_in_deg_2019_df, left_on='country',right_on='country')

#2020
centrality_2020 = way_out_deg_2020_df.merge(way_in_deg_2020_df, left_on='country',right_on='country')

#all
centrality_all = centrality_2018.merge(centrality_2019, left_on='country',right_on='country')
centrality_all = centrality_all.merge(centrality_2020, left_on='country',right_on='country')

# top_combined
centrality_top = centrality_all[centrality_all['country'].isin(top_combined)]


#%% Pyvis: All 2019 data
net_2019 = Network(height='800px', width='100%', bgcolor='white', font_color='midnightblue', heading='2019 Lithium Ion Battery Network')

# set the physics layout of the network
net_2019.barnes_hut()

    sources = libattery_nodes_2019['sources']   #exporters
    targets = libattery_nodes_2019['targets']   #importers
    weights = libattery_nodes_2019['q']         #tons of exports
    
    edge_data = zip(sources, targets, weights)
    
    for e in edge_data:
        src = e[0]
        dst = e[1]
        w = e[2]
    
        net_2019.add_node(src, src, title=src)
        net_2019.add_node(dst, dst, title=dst)
        net_2019.add_edge(src, dst, value=w)


neighbor_map = net_2019.get_adj_list()

# add neighbor data to node hover data
for node in net_2019.nodes:
    node['title'] += ' Trading partners:<br>' + '<br>'.join(neighbor_map[node['id']])
    node['value'] = len(neighbor_map[node['id']])

net_2019.show_buttons(filter_=all)
net_2019.show('net_2019.html')

#%% Pyvis:Top 20 exporters 2019
libattery_nodes_2019_groupby = libattery_nodes_2019.groupby(['sources']).sum().sort_values(by='q', ascending=False)
libattery_nodes_2019_top20df = libattery_nodes_2019_groupby.head(20).reset_index()

libattery_nodes_2019_top20names = libattery_nodes_2019_top20df['sources'].tolist()
libattery_nodes_2019_top20 = libattery_nodes_2019[libattery_nodes_2019['sources'].isin(libattery_nodes_2019_top20names)]

net_2019_top20 = Network(height='800px', width='100%', bgcolor='white', font_color='midnightblue', heading='Top 20 Exporters 2019 Lithium Ion Battery Network')

# set the physics layout of the network
net_2019_top20.barnes_hut()

sources = libattery_nodes_2019_top20['sources']   #exporters
targets = libattery_nodes_2019_top20['targets']   #importers
weights = libattery_nodes_2019_top20['q']         #tons of exports

edge_data = zip(sources, targets, weights)

for e in edge_data:
    src = e[0]
    dst = e[1]
    w = e[2]

    net_2019_top20.add_node(src, src, title=src)
    net_2019_top20.add_node(dst, dst, title=dst)
    net_2019_top20.add_edge(src, dst, value=w)

neighbor_map = net_2019_top20.get_adj_list()

# add neighbor data to node hover data
for node in net_2019_top20.nodes:
    node['title'] += ' Trading partners:<br>' + '<br>'.join(neighbor_map[node['id']])
    node['value'] = len(neighbor_map[node['id']])
    
net_2019_top20.show_buttons(filter_=['physics'])
# net_2019.Network.set_options()
net_2019_top20.show('net_2019_top20_exporters.html')

#%% Pyvis:Top 2 exporters 2019
libattery_nodes_2019_groupby = libattery_nodes_2019.groupby(['sources']).sum().sort_values(by='q', ascending=False)
libattery_nodes_2019_top20df = libattery_nodes_2019_groupby.head(2).reset_index()

libattery_nodes_2019_top20names = libattery_nodes_2019_top20df['sources'].tolist()
libattery_nodes_2019_top20 = libattery_nodes_2019[libattery_nodes_2019['sources'].isin(libattery_nodes_2019_top20names)]

net_2019_top20 = Network(height='800px', width='100%', bgcolor='white', font_color='midnightblue', heading='Top 2 Exporters 2019 Lithium Ion Battery Network')

# set the physics layout of the network
net_2019_top20.barnes_hut()

sources = libattery_nodes_2019_top20['sources']   #exporters
targets = libattery_nodes_2019_top20['targets']   #importers
weights = libattery_nodes_2019_top20['q']         #tons of exports

edge_data = zip(sources, targets, weights)

for e in edge_data:
    src = e[0]
    dst = e[1]
    w = e[2]

    net_2019_top20.add_node(src, src, title=src)
    net_2019_top20.add_node(dst, dst, title=dst)
    net_2019_top20.add_edge(src, dst, value=w)

neighbor_map = net_2019_top20.get_adj_list()

# add neighbor data to node hover data
for node in net_2019_top20.nodes:
    node['title'] += ' Trading partners:<br>' + '<br>'.join(neighbor_map[node['id']])
    node['value'] = len(neighbor_map[node['id']])
    
net_2019_top20.show_buttons(filter_=['physics'])
# net_2019.Network.set_options()
net_2019_top20.show('net_2019_top2_exporters.html')

#%% Pyvis:Top 20 importers 2019
libattery_nodes_2019_groupby = libattery_nodes_2019.groupby(['targets']).sum().sort_values(by='q', ascending=False)
libattery_nodes_2019_top20df = libattery_nodes_2019_groupby.head(20).reset_index()

libattery_nodes_2019_top20names = libattery_nodes_2019_top20df['targets'].tolist()
libattery_nodes_2019_top20 = libattery_nodes_2019[libattery_nodes_2019['targets'].isin(libattery_nodes_2019_top20names)]

net_2019_top2 = Network(height='800px', width='100%', bgcolor='white', font_color='midnightblue', heading='Top 20 Importers 2019 Lithium Ion Battery Network')

# set the physics layout of the network
net_2019_top2.barnes_hut()

sources = libattery_nodes_2019_top20['sources']   #exporters
targets = libattery_nodes_2019_top20['targets']   #importers
weights = libattery_nodes_2019_top20['q']         #tons of exports

edge_data = zip(sources, targets, weights)

for e in edge_data:
    src = e[0]
    dst = e[1]
    w = e[2]

    net_2019_top2.add_node(src, src, title=src)
    net_2019_top2.add_node(dst, dst, title=dst)
    net_2019_top2.add_edge(src, dst, value=w)

neighbor_map = net_2019_top20.get_adj_list()

# add neighbor data to node hover data
for node in net_2019_top20.nodes:
    node['title'] += ' Trading partners:<br>' + '<br>'.join(neighbor_map[node['id']])
    node['value'] = len(neighbor_map[node['id']])
    
net_2019_top2.show_buttons(filter_=['physics'])
# net_2019.Network.set_options()
net_2019_top2.show('net_2019_top20_importers.html')

#%% Pyvis:Top 2 importers 2019
libattery_nodes_2019_groupby = libattery_nodes_2019.groupby(['targets']).sum().sort_values(by='q', ascending=False)
libattery_nodes_2019_top20df = libattery_nodes_2019_groupby.head(2).reset_index()

libattery_nodes_2019_top20names = libattery_nodes_2019_top20df['targets'].tolist()
libattery_nodes_2019_top20 = libattery_nodes_2019[libattery_nodes_2019['targets'].isin(libattery_nodes_2019_top20names)]

net_2019_top20 = Network(height='800px', width='100%', bgcolor='white', font_color='midnightblue', heading='Top 2 Importers 2019 Lithium Ion Battery Network')

# set the physics layout of the network
net_2019_top20.barnes_hut()

sources = libattery_nodes_2019_top20['sources']   #exporters
targets = libattery_nodes_2019_top20['targets']   #importers
weights = libattery_nodes_2019_top20['q']         #tons of exports

edge_data = zip(sources, targets, weights)

for e in edge_data:
    src = e[0]
    dst = e[1]
    w = e[2]

    net_2019_top20.add_node(src, src, title=src)
    net_2019_top20.add_node(dst, dst, title=dst)
    net_2019_top20.add_edge(src, dst, value=w)

neighbor_map = net_2019_top20.get_adj_list()

# add neighbor data to node hover data
for node in net_2019_top20.nodes:
    node['title'] += ' Trading partners:<br>' + '<br>'.join(neighbor_map[node['id']])
    node['value'] = len(neighbor_map[node['id']])
    
net_2019_top20.show_buttons(filter_=['physics'])
# net_2019.Network.set_options()
net_2019_top20.show('net_2019_top2_importers.html')

#%% Pyvis: All 2020 data
net_2020 = Network(height='800px', width='100%', bgcolor='white', font_color='midnightblue', heading='2020 Lithium Ion Battery Network')

# set the physics layout of the network
net_2020.barnes_hut()

sources = libattery_nodes_2020['sources']
targets = libattery_nodes_2020['targets']
weights = libattery_nodes_2020['q']

edge_data = zip(sources, targets, weights)

for e in edge_data:
    src = e[0]
    dst = e[1]
    w = e[2]

    net_2020.add_node(src, src, title=src)
    net_2020.add_node(dst, dst, title=dst)
    net_2020.add_edge(src, dst, value=w)

neighbor_map = net_2020.get_adj_list()

# add neighbor data to node hover data
for node in net_2020.nodes:
    node['title'] += ' Neighbors:<br>' + '<br>'.join(neighbor_map[node['id']])
    node['value'] = len(neighbor_map[node['id']])

net_2020.show('net_2020.html')

#%% Pyvis:Top 20 exporters 2020
libattery_nodes_2020_groupby = libattery_nodes_2020.groupby(['sources']).sum().sort_values(by='q', ascending=False)
libattery_nodes_2020_top20df = libattery_nodes_2020_groupby.head(20).reset_index()

libattery_nodes_2020_top20names = libattery_nodes_2020_top20df['sources'].tolist()
libattery_nodes_2020_top20 = libattery_nodes_2020[libattery_nodes_2020['sources'].isin(libattery_nodes_2020_top20names)]

net_2020_top20 = Network(height='800px', width='100%', bgcolor='white', font_color='midnightblue', heading='Top 20 Exporters 2020 Lithium Ion Battery Network')

# set the physics layout of the network
net_2020_top20.barnes_hut()

sources = libattery_nodes_2020_top20['sources']   #exporters
targets = libattery_nodes_2020_top20['targets']   #importers
weights = libattery_nodes_2020_top20['q']         #tons of exports

edge_data = zip(sources, targets, weights)

for e in edge_data:
    src = e[0]
    dst = e[1]
    w = e[2]

    net_2020_top20.add_node(src, src, title=src)
    net_2020_top20.add_node(dst, dst, title=dst)
    net_2020_top20.add_edge(src, dst, value=w)

neighbor_map = net_2020_top20.get_adj_list()

# add neighbor data to node hover data
for node in net_2020_top20.nodes:
    node['title'] += ' Trading partners:<br>' + '<br>'.join(neighbor_map[node['id']])
    node['value'] = len(neighbor_map[node['id']])
    
net_2020_top20.show_buttons(filter_=['physics'])
# net_2019.Network.set_options()
net_2020_top20.show('net_2020_top20_exporters.html')

#%% Pyvis:Top 2 exporters 2020
libattery_nodes_2020_groupby = libattery_nodes_2020.groupby(['sources']).sum().sort_values(by='q', ascending=False)
libattery_nodes_2020_top2df = libattery_nodes_2020_groupby.head(2).reset_index()

libattery_nodes_2020_top2names = libattery_nodes_2020_top2df['sources'].tolist()
libattery_nodes_2020_top2 = libattery_nodes_2020[libattery_nodes_2020['sources'].isin(libattery_nodes_2020_top2names)]

net_2020_top2 = Network(height='800px', width='100%', bgcolor='white', font_color='midnightblue', heading='Top 2 Exporters 2020 Lithium Ion Battery Network')

# set the physics layout of the network
net_2020_top2.barnes_hut()

sources = libattery_nodes_2020_top2['sources']   #exporters
targets = libattery_nodes_2020_top2['targets']   #importers
weights = libattery_nodes_2020_top2['q']         #tons of exports

edge_data = zip(sources, targets, weights)

for e in edge_data:
    src = e[0]
    dst = e[1]
    w = e[2]

    net_2020_top2.add_node(src, src, title=src)
    net_2020_top2.add_node(dst, dst, title=dst)
    net_2020_top2.add_edge(src, dst, value=w)

neighbor_map = net_2020_top2.get_adj_list()

# add neighbor data to node hover data
for node in net_2020_top2.nodes:
    node['title'] += ' Trading partners:<br>' + '<br>'.join(neighbor_map[node['id']])
    node['value'] = len(neighbor_map[node['id']])
    
net_2020_top2.show_buttons(filter_=['physics'])

net_2020_top2.show('net_2020_top2_exporters.html')

#%% Pyvis:Top 20 importers 2020
libattery_nodes_2020_groupby = libattery_nodes_2020.groupby(['targets']).sum().sort_values(by='q', ascending=False)
libattery_nodes_2020_top20df = libattery_nodes_2020_groupby.head(20).reset_index()

libattery_nodes_2020_top20names = libattery_nodes_2020_top20df['targets'].tolist()
libattery_nodes_2020_top20 = libattery_nodes_2020[libattery_nodes_2020['targets'].isin(libattery_nodes_2020_top20names)]

net_2020_top20 = Network(height='800px', width='100%', bgcolor='white', font_color='midnightblue', heading='Top 20 Importers 2020 Lithium Ion Battery Network')

# set the physics layout of the network
net_2020_top20.barnes_hut()

sources = libattery_nodes_2020_top20['sources']   #exporters
targets = libattery_nodes_2020_top20['targets']   #importers
weights = libattery_nodes_2020_top20['q']         #tons of exports

edge_data = zip(sources, targets, weights)

for e in edge_data:
    src = e[0]
    dst = e[1]
    w = e[2]

    net_2020_top20.add_node(src, src, title=src)
    net_2020_top20.add_node(dst, dst, title=dst)
    net_2020_top20.add_edge(src, dst, value=w)

neighbor_map = net_2020_top20.get_adj_list()

# add neighbor data to node hover data
for node in net_2020_top20.nodes:
    node['title'] += ' Trading partners:<br>' + '<br>'.join(neighbor_map[node['id']])
    node['value'] = len(neighbor_map[node['id']])
    
net_2020_top20.show_buttons(filter_=['physics'])
# net_2019.Network.set_options()
net_2020_top20.show('net_2020_top20_importers.html')

#%% Pyvis:Top 2 exporters 2020
libattery_nodes_2020_groupby = libattery_nodes_2020.groupby(['targets']).sum().sort_values(by='q', ascending=False)
libattery_nodes_2020_top2df = libattery_nodes_2020_groupby.head(2).reset_index()

libattery_nodes_2020_top2names = libattery_nodes_2020_top2df['targets'].tolist()
libattery_nodes_2020_top2 = libattery_nodes_2020[libattery_nodes_2020['targets'].isin(libattery_nodes_2020_top2names)]

net_2020_top2 = Network(height='800px', width='100%', bgcolor='white', font_color='midnightblue', heading='Top 2 Importers 2020 Lithium Ion Battery Network')

# set the physics layout of the network
net_2020_top2.barnes_hut()

sources = libattery_nodes_2020_top2['sources']   #exporters
targets = libattery_nodes_2020_top2['targets']   #importers
weights = libattery_nodes_2020_top2['q']         #tons of exports

edge_data = zip(sources, targets, weights)

for e in edge_data:
    src = e[0]
    dst = e[1]
    w = e[2]

    net_2020_top2.add_node(src, src, title=src)
    net_2020_top2.add_node(dst, dst, title=dst)
    net_2020_top2.add_edge(src, dst, value=w)

neighbor_map = net_2020_top2.get_adj_list()

# add neighbor data to node hover data
for node in net_2020_top2.nodes:
    node['title'] += ' Trading partners:<br>' + '<br>'.join(neighbor_map[node['id']])
    node['value'] = len(neighbor_map[node['id']])
    
net_2020_top2.show_buttons(filter_=['physics'])

net_2020_top2.show('net_2020_top2_importers.html')

#%%