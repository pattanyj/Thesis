# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 16:54:12 2022

@author: patta
"""
#%% EXAMPLE

def logistic(x, start, K, x_peak, r):
    """
    Logistic model
    
    This function runs a logistic model.
    
    Args:
        x (array_like): The control variable as a sequence of numeric values \
        in a list or a numpy array.
        start (float): The initial value of the return variable.
        K (float): The carrying capacity.
        x_peak (float): The x-value with the steepest growth.
        r (float): The growth rate.
        
    Returns:
        array_like: A numpy array or a single floating-point number with \
        the return variable.
    """
    
    if isinstance(x, list):
        x = np.array(x)
    return start + K / (1 + np.exp(r * (x_peak-x)))

#%%
# imports

import pandas as pd
import numpy as np
import matplotlib as plt
import math
# from explore_data import 

BACI_df = pd.read_csv('./Data/BACI_HS17_Y2017_V202102.csv')
BACI_cobalt = BACI_df.loc[BACI_df['k'].isin([260500,282200,810520,810530,810590,])]

def calculations(ISO_importer,ISO_exporter):
    
    Tij = BACI_cobalt['q'].loc[BACI_cobalt['i'].isin([ISO_importer]) & BACI_cobalt['j'].isin([ISO_exporter])].sum()
    Ti = BACI_cobalt['q'].loc[BACI_cobalt['i'].isin([ISO_importer])].sum()
    Tj = BACI_cobalt['q'].loc[BACI_cobalt['j'].isin([ISO_exporter])].sum()
    T = Ti + Tj
    
    efficiency = (Tij/T)*math.log((Tij*T)/(Ti*Tj))
    redundancy = (Tij/T)*math.log((Tij**2)/(Ti*Tj))
    alpha = efficiency/(redundancy+efficiency)
    theoretical_resilience = (-alpha)*math.log(alpha)

    return efficiency,redundancy,alpha,theoretical_resilience