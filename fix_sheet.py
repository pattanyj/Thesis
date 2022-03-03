# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 15:23:14 2022

@author: patta
"""

# imports
# import json
import pandas as pd
import numpy as np
# from pyvis.network import Network
# import networkx as nx

# import BACI data
# BACI_df = pd.read_csv('./Data/BACI_HS17_Y2017_V202102.csv')
BACI_df = pd.read_csv('./Data/BACI_HS12_Y2018_V202201_clean.csv')
country_code_df = pd.read_csv('./Data/country_code.csv',encoding='unicode_escape')

# import cobalt information
HS6_composition_df = pd.read_csv('./Data/compostions_balanced_Co.csv')
prod_code_df = pd.read_csv('./Data/product_codes_HS17.csv')

#%% Getting names of all cobalt products

#collect country names
names = country_code_df.drop(columns=['country_name_abbreviation','iso_2digit_alpha','iso_3digit_alpha'])

# merge df
co_prod = BACI_df.merge(HS6_composition_df, left_on='k',right_on='HS6')
co_prod = co_prod.drop(columns=['Prod','HS6','v'])
all_cobalt_codes = co_prod['k'].unique()

#for exporters
coprod_exp = co_prod.merge(names, left_on='i', right_on='country_code')
coprod_exp = coprod_exp.drop(columns=['country_code'])
coprod_exp = coprod_exp.rename({'country_name_full':'exporter'},axis='columns')
coprod_exp.to_csv('coprod_exp.csv')

#for exporters and importers
coprod_imp = coprod_exp.merge(names,left_on='j', right_on='country_code')
coprod_imp = coprod_imp.drop(columns=['country_code'])
coprod_imp = coprod_imp.rename({'country_name_full':'importer'},axis='columns')
coprod_imp.to_csv('co_product_imp.csv')

#for product names
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
prod_list_cobalt_DF = prod_list_cobalt_DF.drop(columns=['t','i','j','v'])
prod_list_cobalt_DF['co_quantity'] = prod_list_cobalt_DF['Balance_mean']*prod_list_cobalt_DF['q']
prod_list_cobalt_DF.to_csv('co_product_list.csv')

#%% Resilience calculations
#collect product codes and create DF for final results
products = HS6_composition_df['HS6'].to_numpy()
resilience_df = pd.DataFrame(columns = ['product',"efficiency","redundancy",'alpha','theoretical_resilience']) 

for product in products:
    
    #collect individual products
    BACI_product = BACI_df.loc[BACI_df['k'].isin([product])].dropna().loc[~(BACI_df['q']==0)]
    
    #group by country
    gb_exporter = BACI_product.groupby('i').sum().reset_index().drop(columns = ['t','j','k','v']).rename(columns={"q": "Ti"})
    gb_importer = BACI_product.groupby('j').sum().reset_index().drop(columns = ['t','i','k','v']).rename(columns={"q": "Tj"})
    
    #Ti and Tj columns
    BACI_product_merge = BACI_product.merge(gb_exporter, left_on='i',right_on='i')
    BACI_product_merge = BACI_product_merge.merge(gb_importer, left_on='j',right_on='j')
    BACI_product_merge['T'] = BACI_product_merge['q'].sum()
    
    #calculating efficiency, redundancy, alpha and theoretical resilience
    BACI_product_merge['efficiency'] = (BACI_product_merge['q']/BACI_product_merge['T'])*np.log((BACI_product_merge['q']*BACI_product_merge['T'])/(BACI_product_merge['Ti']*BACI_product_merge['Tj']))
    BACI_product_merge['redundancy'] = -(BACI_product_merge['q']/BACI_product_merge['T'])*np.log((BACI_product_merge['q']**2)/(BACI_product_merge['Ti']*BACI_product_merge['Tj']))
    
    efficiency = BACI_product_merge['efficiency'].sum()
    redundancy = BACI_product_merge['redundancy'].sum()
    alpha = efficiency/(redundancy+efficiency)
    theoretical_resilience = (-alpha)*np.log(alpha)
    
    #results to df
    to_append = [product,efficiency, redundancy, alpha, theoretical_resilience]
    a_series = pd.Series(to_append, index = resilience_df.columns)
    resilience_df = resilience_df.append(a_series, ignore_index=True)

#%% 
#calculate df with names
resilience_2018 = resilience_df.merge(prod_list_cobalt_DF,left_on='product', right_on='HS6').drop(columns=['HS6','Balance_mean','q','co_quantity'])
resilience_2018 = resilience_2018[['product', 'prod_name','efficiency','redundancy','alpha','theoretical_resilience']]
resilience_2018.to_csv('./Results/resilience_2018.csv')
