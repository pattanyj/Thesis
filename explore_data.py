# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# imports
import json
import pandas as pd

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

#%% Import BACI Data
BACI_df = pd.read_csv('./Data/BACI_HS17_Y2017_V202102.csv')

#%% Creating DataFrames 
# Labels
region = dim_code['label']['reg']
product = dim_code['label']['pro']
industry = dim_code['label']['ind']

# Supply information
supply_values = elem['Co']['sup']['val']
supply_position = elem['Co']['sup']['pos']

# Collecting labels for supply
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


#%% Calculating alpha
BACI_cobalt = BACI_df.loc[BACI_df['k'].isin([260500,282200,810520,810530,810590,])]
# cobalt_china =  BACI_cobalt.loc[BACI_cobalt['j'].isin([156])]
# belgium_china = BACI_cobalt.loc[BACI_cobalt['i'].isin([56]) & BACI_cobalt['j'].isin([156])]
# tons_bc = belgium_china['q'].sum()

from equations import calculations

belg_chi = calculations(56,156) #theoretical resilience just under 0.37 therefore slightly redundant

#%% PLOT DATA

from pyvis.network import Network 

g = Network()
g.add_nodes([1,2,3], value=[10, 100, 400],
                         title=['I am node 1', 'node 2 here', 'and im node 3'],
                         x=[21.4, 54.2, 11.2],
                         y=[100.2, 23.54, 32.1],
                         label=['NODE 1', 'NODE 2', 'NODE 3'],
                         color=['#00ff1e', '#162347', '#dd4b39'])
