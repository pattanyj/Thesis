# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import json
 
# Opening JSON file
dim_code = open('./Data/dim_code_label.json')
elem = open('./Data/elem.json')
extensions = open('./Data/extensions.json')
 
# returns JSON object as
# a dictionary
dim_code = json.load(dim_code)
elem = json.load(elem)
extensions = json.load(extensions)

#%% Iterating through the json
# list
for i in elem['Co']:
    print(i)

# list
# for i in dim_code['code']:
#     print(i)
 
# Closing file
# f.close()