# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# imports
import json
import pandas as pd
import numpy as np
# import math
from pyvis.network import Network
import networkx as nx

#%% PANORAMA Data
# Opening JSON file
dim_code = open('./Data/dim_code_label.json')
elem = open('./Data/elem.json')
extensions = open('./Data/extensions.json')
 
# returns JSON object as
# a dictionary
dim_code = json.load(dim_code)
elem = json.load(elem)
extensions = json.load(extensions)

# Creating DataFrames 
# Labels
region = dim_code['label']['reg']
product = dim_code['label']['pro']
industry = dim_code['label']['ind']

# Supply information
supply_values = elem['Co']['sup']['val']
supply_position = elem['Co']['sup']['pos']

# Collecting labels for supply - can combine to one for loop also (for later)
supply_region = []
for i in supply_position[0]:
    supply_region.append(region[i])   

supply_product = []
for i in supply_position[1]:
    supply_product.append(product[i])

supply_industry = []
for i in supply_position[2]:
    supply_industry.append(industry[i])
 
# Creating a Supply DataFrame
list_tuples = list(zip(supply_region,supply_product,supply_industry,supply_values))    # zip together list values
supply_df = pd.DataFrame(list_tuples, columns=['Region','Product','Industry','Value (tons)'])   # create df

#%% BACI Data
# import BACI data for 2017
BACI_df = pd.read_csv('./Data/BACI_HS17_Y2017_V202102.csv')
country_code_df = pd.read_csv('./Data/country_code.csv',encoding='unicode_escape')

# Calculating alpha
# filter by product
product = 260500    # Cobalt ores and concentrates
BACI_product = BACI_df.loc[BACI_df['k'].isin([product])].dropna()

#group by country
gb_exporter = BACI_product.groupby('i').sum()
gb_importer = BACI_product.groupby('j').sum()

# calculations https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0171184
Tij = BACI_product['q']
Ti = gb_exporter['q']
Tj = gb_importer['q']
T = Ti.sum() + Tj.sum()

efficiency = (Tij/T).sum()*np.log((Tij*T).sum()/(Ti*Tj).sum())
redundancy = (Tij/T).sum()*np.log((Tij**2).sum()/(Ti*Tj).sum())
alpha = efficiency/(redundancy+efficiency)
theoretical_resilience = (-alpha)*np.log(alpha)

# all_calc = [efficiency, redundancy, alpha]

#%% Getting names of all cobalt products

# import cobalt informaiton
HS6_composition_df = pd.read_csv('./Data/compostions_balanced_Co.csv')
prod_code_df = pd.read_csv('./Data/product_codes_HS17.csv')

# merge df
co_prod = BACI_df.merge(HS6_composition_df, left_on='k',right_on='HS6')
co_prod = co_prod.drop(columns=['Prod','HS6','v'])

#merge for names
names = country_code_df.drop(columns=['country_name_abbreviation','iso_2digit_alpha','iso_3digit_alpha'])

#for exporters
coprod_exp = co_prod.merge(names, left_on='i', right_on='country_code')
coprod_exp = coprod_exp.drop(columns=['country_code'])
coprod_exp = coprod_exp.rename({'country_name_full':'exporter'},axis='columns')
#for importers
coprod_imp = coprod_exp.merge(names,left_on='j', right_on='country_code')
coprod_imp = coprod_imp.drop(columns=['country_code'])
coprod_imp = coprod_imp.rename({'country_name_full':'importer'},axis='columns')
#for productnames
coprod_final = coprod_imp.merge(prod_code_df,left_on='k', right_on='code')
coprod_final = coprod_final.drop(columns=['code'])
coprod_final = coprod_final.rename({'description':'product'},axis='columns')

#to csv
prod_list_cobalt = coprod_final['product'].unique()
prod_list_cobalt_DF = pd.DataFrame(prod_list_cobalt)
prod_list_cobalt_DF = prod_list_cobalt_DF.merge(prod_code_df, left_on=0, right_on='description')
prod_list_cobalt_DF = prod_list_cobalt_DF.merge(HS6_composition_df, left_on='code', right_on='HS6')
prod_list_cobalt_DF = prod_list_cobalt_DF.drop(columns=['code','description','Prod',])
prod_list_cobalt_DF = prod_list_cobalt_DF.rename({0:'prod_name'},axis='columns')
BACI_prod_df = BACI_df.groupby('k').sum()
prod_list_cobalt_DF = prod_list_cobalt_DF.merge(BACI_prod_df, left_on='HS6', right_index=True)
prod_list_cobalt_DF = prod_list_cobalt_DF.drop(columns=['t','i','j','v',])
prod_list_cobalt_DF['co_quantity'] = prod_list_cobalt_DF['Balance_mean']*prod_list_cobalt_DF['q']
prod_list_cobalt_DF.to_csv('co_product_list.csv')

#%% Trying Pyvis
g = Network()
#plotting exporters
exporter_codes= BACI_product['i'].unique()
exporter_names = []

for i in exporter_codes:
    temp = country_code_df.query('country_code' == i)['country_name_full']
    exporter_names.append(temp)


g.add_nodes([1,2,3,4,5,6], value=gb_exporter['q'], 
            title=[BACI_product['i'].unique()], label='exporters')

nt = Network('500px', '500px')

# populates the nodes and edges data structures
nt.from_nx(g)
nt.show('g_plot.html')

#%%
nx_graph = nx.cycle_graph(10)
nx_graph.nodes[1]['title'] = 'Number 1'
nx_graph.nodes[1]['group'] = 1
nx_graph.nodes[3]['title'] = 'I belong to a different group!'
nx_graph.nodes[3]['group'] = 10
nx_graph.add_node(20, size=20, title='couple', group=2)
nx_graph.add_node(21, size=15, title='couple', group=2)
nx_graph.add_edge(20, 21, weight=5)
nx_graph.add_node(25, size=25, label='lonely', title='lonely node', group=3)
nt = Network('500px', '500px')
# populates the nodes and edges data structures
nt.from_nx(nx_graph)
nt.show('nx.html')