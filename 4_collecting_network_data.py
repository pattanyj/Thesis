# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 13:50:53 2022

@author: patta
"""

import pandas as pd
from pyvis.network import Network
import networkx as nx
import matplotlib.pyplot as plt

# 2012 to 2014 files
#import HS12 files
HS12_2012 = pd.read_csv('./clean_BACI/HS12/clean_BACI_HS12_Y2012_V202201.csv')
HS12_2013 = pd.read_csv('./clean_BACI/HS12/clean_BACI_HS12_Y2013_V202201.csv')
HS12_2014 = pd.read_csv('./clean_BACI/HS12/clean_BACI_HS12_Y2014_V202201.csv')

#import country name files
HS12_country = pd.read_csv('./BACI_HS12/country_codes_V202201.csv',encoding='unicode_escape')

#MERGE

#2012
merge = HS12_2012.merge(HS12_country, left_on='i',right_on='country_code')
merge = merge.rename({'country_name_full':'sources'},axis='columns')
merge = merge.drop(columns=['Unnamed: 0','country_code','country_name_abbreviation','iso_2digit_alpha','iso_3digit_alpha'])
HS12_2012_final = merge.merge(HS12_country, left_on='j',right_on='country_code')
HS12_2012_final = HS12_2012_final.rename({'country_name_full':'targets'},axis='columns')
HS12_2012_final = HS12_2012_final.drop(columns=['country_code','country_name_abbreviation','iso_2digit_alpha','iso_3digit_alpha'])

#2013
merge_1 = HS12_2013.merge(HS12_country, left_on='i',right_on='country_code')
merge_1 = merge_1.rename({'country_name_full':'sources'},axis='columns')
merge_1 = merge_1.drop(columns=['Unnamed: 0','country_code','country_name_abbreviation','iso_2digit_alpha','iso_3digit_alpha'])
HS12_2013_final = merge_1.merge(HS12_country, left_on='j',right_on='country_code')
HS12_2013_final = HS12_2013_final.rename({'country_name_full':'targets'},axis='columns')
HS12_2013_final = HS12_2013_final.drop(columns=['country_code','country_name_abbreviation','iso_2digit_alpha','iso_3digit_alpha'])

#2014
merge_2 = HS12_2014.merge(HS12_country, left_on='i',right_on='country_code')
merge_2 = merge_2.rename({'country_name_full':'sources'},axis='columns')
merge_2 = merge_2.drop(columns=['Unnamed: 0','country_code','country_name_abbreviation','iso_2digit_alpha','iso_3digit_alpha'])
HS12_2014_final = merge_2.merge(HS12_country, left_on='j',right_on='country_code')
HS12_2014_final = HS12_2014_final.rename({'country_name_full':'targets'},axis='columns')
HS12_2014_final = HS12_2014_final.drop(columns=['country_code','country_name_abbreviation','iso_2digit_alpha','iso_3digit_alpha'])

# 2015 to 2017 files
#import HS12 files
HS12_2015 = pd.read_csv('./clean_BACI/HS12/clean_BACI_HS12_Y2015_V202201.csv')
HS12_2016 = pd.read_csv('./clean_BACI/HS12/clean_BACI_HS12_Y2016_V202201.csv')
HS12_2017 = pd.read_csv('./clean_BACI/HS12/clean_BACI_HS12_Y2017_V202201.csv')


#2015
merge = HS12_2015.merge(HS12_country, left_on='i',right_on='country_code')
merge = merge.rename({'country_name_full':'sources'},axis='columns')
merge = merge.drop(columns=['Unnamed: 0','country_code','country_name_abbreviation','iso_2digit_alpha','iso_3digit_alpha'])
HS12_2015_final = merge.merge(HS12_country, left_on='j',right_on='country_code')
HS12_2015_final = HS12_2015_final.rename({'country_name_full':'targets'},axis='columns')
HS12_2015_final = HS12_2015_final.drop(columns=['country_code','country_name_abbreviation','iso_2digit_alpha','iso_3digit_alpha'])

#2016
merge_1 = HS12_2016.merge(HS12_country, left_on='i',right_on='country_code')
merge_1 = merge_1.rename({'country_name_full':'sources'},axis='columns')
merge_1 = merge_1.drop(columns=['Unnamed: 0','country_code','country_name_abbreviation','iso_2digit_alpha','iso_3digit_alpha'])
HS12_2016_final = merge_1.merge(HS12_country, left_on='j',right_on='country_code')
HS12_2016_final = HS12_2016_final.rename({'country_name_full':'targets'},axis='columns')
HS12_2016_final = HS12_2016_final.drop(columns=['country_code','country_name_abbreviation','iso_2digit_alpha','iso_3digit_alpha'])

#2017
merge_2 = HS12_2017.merge(HS12_country, left_on='i',right_on='country_code')
merge_2 = merge_2.rename({'country_name_full':'sources'},axis='columns')
merge_2 = merge_2.drop(columns=['Unnamed: 0','country_code','country_name_abbreviation','iso_2digit_alpha','iso_3digit_alpha'])
HS12_2017_final = merge_2.merge(HS12_country, left_on='j',right_on='country_code')
HS12_2017_final = HS12_2017_final.rename({'country_name_full':'targets'},axis='columns')
HS12_2017_final = HS12_2017_final.drop(columns=['country_code','country_name_abbreviation','iso_2digit_alpha','iso_3digit_alpha'])

# 2018 to 2020 files
#import HS12 files
HS12_2018 = pd.read_csv('./clean_BACI/HS12/clean_BACI_HS12_Y2018_V202201.csv')
HS12_2019 = pd.read_csv('./clean_BACI/HS12/clean_BACI_HS12_Y2019_V202201.csv')
HS12_2020 = pd.read_csv('./clean_BACI/HS12/clean_BACI_HS12_Y2020_V202201.csv')


# Merge 2018 to 2020 data
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

# #2020
merge_2 = HS12_2020.merge(HS12_country, left_on='i',right_on='country_code')
merge_2 = merge_2.rename({'country_name_full':'sources'},axis='columns')
merge_2 = merge_2.drop(columns=['Unnamed: 0','country_code','country_name_abbreviation','iso_2digit_alpha','iso_3digit_alpha'])
HS12_2020_final = merge_2.merge(HS12_country, left_on='j',right_on='country_code')
HS12_2020_final = HS12_2020_final.rename({'country_name_full':'targets'},axis='columns')
HS12_2020_final = HS12_2020_final.drop(columns=['country_code','country_name_abbreviation','iso_2digit_alpha','iso_3digit_alpha'])

#%%collecting df for lithium ion batteries
# code = [850650]

# #2018 to 2020ArithmeticError
# df_2018 = HS12_2018_final[HS12_2018_final['k'].isin(code)]
# df_2019 = HS12_2019_final[HS12_2019_final['k'].isin(code)]
# df_2020 = HS12_2020_final[HS12_2020_final['k'].isin(code)]

# new_df = pd.merge(df_2020, df_2019,  how='left', left_on=['sources','targets'], right_on = ['sources','targets'])
# network_18_20 = new_df #.fillna(0)
# network_18_20['q'] = network_18_20['q_x'] - network_18_20['q_y']
# network_18_20 = network_18_20.fillna(0)
# network_18_20 = network_18_20.drop(columns = ['i_y','j_y','k_y','v_y']).sort_values(by='q', ascending=False)
# network_18_20.to_csv('./network_product_data/libattery_nodes_2020_subtract_2019.csv')

# # group by exports
# exports = network_18_20.groupby('sources').sum().reset_index().sort_values(by='q', ascending=False)
# # exports.to_csv('./network_product_data/libattery_nodes_exports_2020_subtract_2019.csv')
# imports = network_18_20.groupby('targets').sum().reset_index().sort_values(by='q', ascending=False)
# imports.to_csv('./network_product_data/libattery_nodes_imports_2020_subtract_2019.csv')

#%%collecting df for all data
code = [260500, #Cobalt ores and concentrates (1988-2500)
750300, #Waste and scrap, of nickel alloys (excl. ingots or other similar unwrought shapes, of remelted nickel alloys waste and scrap, ashes and residues containing nickel alloys)
# 810530, #Cobalt waste and scrap (excl. ash and residues containingcobalt)(2002-2500)
810520, #Cobalt mattes and other intermediate products of cobalt metallurgy; unwrought cobalt; cobalt powders(2002-2500)
750110, #Nickel mattes
282200, #Cobalt oxides and hydroxides; commercial cobalt oxides(1988-2500)
282739, #Cobalt chlorides(2007-2500)
283329, #Sulphates of cobalt and of titanium(1988-2500)
# 840610, #Turbines: steam and other vapour turbines, for marine propulsion
840681, #Turbines: steam and other vapour turbines, (for other than marine propulsion), of an output exceeding 40MW
840682, #Turbines: steam and other vapour turbines, (for other than marine propulsion), of an output not exceeding 40MW
840690, #Turbines: parts of steam and other vapour turbines
# 841191, #Turbines: parts of turbo-jets and turbo-propellers
841199, #Turbines: parts of gas turbines (excluding turbo-jets and turbo-propellers)67
841810, #Refrigerators and freezers: combined refrigerator-freezers, fitted with separate external doors, electric or other"
# 841821, #Refrigerators: for household use, compression-type, electric or other"
# 841829, #Refrigerators: household, electric or not, other than compression-type"
841830, #Freezers: of the chest type, not exceeding 800l capacity"
841840, #Freezers: of the upright type, not exceeding 900l capacity"
841850, #Furniture incorporating refrigerating or freezing equipment: for storage and display, n.e.c. in item no. 8418.1, 8418.2, 8418.3 or 8418.4 (chests, cabinets, display counters, show-cases and the like)"
841861, #Heat pumps: other than air conditioning machines of heading no. 8415"
841869, #Refrigerating or freezing equipment: n.e.c. in heading no. 8418
841891, #Refrigerating or freezing equipment: parts, furniture designed to receive refrigerating or freezing equipment
841899, #Refrigerating or freezing equipment: parts thereof, other than furniture
711510, #Metal: catalysts in the form of wire cloth or grill, of platinum"
850440, #Electrical static converters
854140  #Electrical apparatus: photosensitive, including photovoltaic cells, whether or not assembled in modules or made up into panels, light emitting diodes
]

#2012 to 2020 
df_2012 = HS12_2012_final[HS12_2012_final['k'].isin(code)]
df_2013 = HS12_2013_final[HS12_2013_final['k'].isin(code)]
df_2014 = HS12_2014_final[HS12_2014_final['k'].isin(code)]
df_2015 = HS12_2015_final[HS12_2015_final['k'].isin(code)]
df_2016 = HS12_2016_final[HS12_2016_final['k'].isin(code)]
df_2017 = HS12_2017_final[HS12_2017_final['k'].isin(code)] 
df_2018 = HS12_2018_final[HS12_2018_final['k'].isin(code)]
df_2019 = HS12_2019_final[HS12_2019_final['k'].isin(code)]
df_2020 = HS12_2020_final[HS12_2020_final['k'].isin(code)]

#%%2012 to 2014 DF
new_df5 = pd.merge(df_2012, df_2013,  how='outer', left_on=['k','sources','targets'], right_on = ['k','sources','targets'])
new_df6 = pd.merge(new_df5, df_2014,  how='outer', left_on=['k','sources','targets'], right_on = ['k','sources','targets']) 
network_2012_2014 = new_df6.fillna(value={'q_x':0,'q_y':0,'q':0})
network_2012_2014['q_total'] = network_2012_2014['q_x'] + network_2012_2014['q_y'] + network_2012_2014['q']
network_2012_2014 = network_2012_2014.drop(columns = ['t_x', 'i','j','i_x','j_x','v_x','q_x',
                                      't_y','i_y','j_y','v_y','q_y','t','v','q'])
network_2012_2014.to_csv('./network_product_data/all_2012_2014_data.csv')

#2015 to 2017 DF
new_df = pd.merge(df_2015, df_2016,  how='outer', left_on=['k','sources','targets'], right_on = ['k','sources','targets'])
new_df2 = pd.merge(new_df, df_2017,  how='outer', left_on=['k','sources','targets'], right_on = ['k','sources','targets']) 
network_2015_2017 = new_df2.fillna(value={'q_x':0,'q_y':0,'q':0})
network_2015_2017['q_total'] = network_2015_2017['q_x'] + network_2015_2017['q_y'] + network_2015_2017['q']
network_2015_2017 = network_2015_2017.drop(columns = ['t_x', 'i','j','i_x','j_x','v_x','q_x',
                                      't_y','i_y','j_y','v_y','q_y','t','v','q'])
network_2015_2017.to_csv('./network_product_data/all_2015_2017_data.csv')

#2018 to 2020 DF
new_df3 = pd.merge(df_2018, df_2019,  how='outer', left_on=['k','sources','targets'], right_on = ['k','sources','targets'])
new_df4 = pd.merge(new_df3, df_2020,  how='outer', left_on=['k','sources','targets'], right_on = ['k','sources','targets'])
network_2018_2020 = new_df4.fillna(0)
network_2018_2020['q_total'] = network_2018_2020['q_x'] + network_2018_2020['q_y'] + network_2018_2020['q']
network_2018_2020 = network_2018_2020.drop(columns = ['t_x', 'i','j','i_x','j_x','v_x','q_x',
                                      't_y','i_y','j_y','v_y','q_y','t','v','q'])
network_2018_2020.to_csv('./network_product_data/all_2018_2020_data.csv')

# # group by exports
# exports = network_18_20.groupby('sources').sum().reset_index().sort_values(by='q', ascending=False)
# # exports.to_csv('./network_product_data/libattery_nodes_exports_2020_subtract_2019.csv')
# imports = network_18_20.groupby('targets').sum().reset_index().sort_values(by='q', ascending=False)
# # imports.to_csv('./network_product_data/master_data.csv')


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