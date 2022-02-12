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

kmf = KaplanMeierFitter()
kmf.fit() 
