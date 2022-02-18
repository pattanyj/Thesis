# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 16:54:12 2022

@author: patta
"""


#%%
# imports

import pandas as pd
import numpy as np
import math

# data
BACI_df = pd.read_csv('./Data/BACI_HS17_Y2017_V202102.csv')
cobalt_products = [260500,282200,810520,810530,810590]
BACI_cobalt = BACI_df.loc[BACI_df['k'].isin(cobalt_products)]

test = BACI_cobalt.groupby(['i','k']).sum()
#%%

def calculations(cobalt_products):

    calculations_df = pd.DataFrame(columns=['product','efficiency','redundancy','alpha',
                                        'theoretical_resilience'])

    for product in cobalt_products:  
        
        gb_exporter = BACI_cobalt.groupby(['i','k']).sum()
        gb_importer = BACI_cobalt.groupby(['j','k']).sum()
        
        Tij = BACI_cobalt['q'].loc[BACI_cobalt['k'].isin([product])].sum()
        Ti = gb_exporter['q'].loc[gb_exporter['k'].isin([product])].sum()
        Tj = gb_importer['q'].loc[gb_importer['k'].isin([product])].sum()
        T = Ti + Tj
 
        efficiency = (Tij/T)*math.log((Tij*T)/(Ti*Tj))
        redundancy = (Tij/T)*math.log((Tij**2)/(Ti*Tj))
        alpha = efficiency/(redundancy+efficiency)
        theoretical_resilience = (-alpha)*math.log(alpha)
        
        to_append = [product,efficiency,redundancy,alpha,theoretical_resilience]
        series = pd.Series(to_append, index = calculations_df.columns)
        calculations_df = calculations_df.append(series, ignore_index=True)
        
    return calculations_df

#%%
        
    
    
# def calculations(ISO_importer,ISO_exporter):   # https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0171184 for calc
   
    """ DO THIS
    Calculations model
    
    This function runs a model.
    
    Args:
        BACI_cobalt (DataFrame): explain here.

    Returns:
        array_like: explain here.
    """
    # per k (product) needs to be calc then groupby sums and calc eff, red, alpha, ...
    
    
    # Tij = BACI_cobalt['q'].loc[BACI_cobalt['i'].isin([ISO_importer]) & BACI_cobalt['j'].isin([ISO_exporter])].sum()
    # Ti = BACI_cobalt['q'].loc[BACI_cobalt['i'].isin([ISO_importer])].sum()
    # Tj = BACI_cobalt['q'].loc[BACI_cobalt['j'].isin([ISO_exporter])].sum()
    # T = Ti + Tj
    
    # efficiency = (Tij/T)*math.log((Tij*T)/(Ti*Tj))
    # redundancy = (Tij/T)*math.log((Tij**2)/(Ti*Tj))
    # alpha = efficiency/(redundancy+efficiency)
    # theoretical_resilience = (-alpha)*math.log(alpha)

    # return efficiency,redundancy,alpha,theoretical_resilience