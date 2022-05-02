# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 17:22:39 2022

@author: patta
"""

import pandas as pd
import matplotlib.pyplot as plt


#HS07
#import resilience files and small clean 
HS07_BACI_2010 = pd.read_csv('./Resilience/HS07/resilience_2010.csv')
# HS07_BACI_2010['Year'] = 2010 
# HS07_BACI_2010 = HS07_BACI_2010.iloc[: , 1:]
# HS07_BACI_2010.to_csv('./Resilience/HS07/resilience_2010.csv')

HS07_BACI_2011 = pd.read_csv('./Resilience/HS07/resilience_2011.csv')
# HS07_BACI_2011['Year'] = 2011
# HS07_BACI_2011 = HS07_BACI_2011.iloc[: , 1:]
# HS07_BACI_2011.to_csv('./Resilience/HS07/resilience_2011.csv')

HS07_BACI_2012 = pd.read_csv('./Resilience/HS07/resilience_2012.csv')
# HS07_BACI_2012['Year'] = 2012
# HS07_BACI_2012 = HS07_BACI_2012.iloc[: , 1:]
# HS07_BACI_2012.to_csv('./Resilience/HS07/resilience_2012.csv')

HS07_BACI_2013 = pd.read_csv('./Resilience/HS07/resilience_2013.csv')
# HS07_BACI_2013['Year'] = 2013
# HS07_BACI_2013 = HS07_BACI_2013.iloc[: , 1:]
# HS07_BACI_2013.to_csv('./Resilience/HS07/resilience_2013.csv')

HS07_BACI_2014 = pd.read_csv('./Resilience/HS07/resilience_2014.csv')
# HS07_BACI_2014['Year'] = 2014
# HS07_BACI_2014 = HS07_BACI_2014.iloc[: , 1:]
# HS07_BACI_2014.to_csv('./Resilience/HS07/resilience_2014.csv')

HS07_BACI_2015 = pd.read_csv('./Resilience/HS07/resilience_2015.csv')
# HS07_BACI_2015['Year'] = 2015
# HS07_BACI_2015 = HS07_BACI_2015.iloc[: , 1:]
# HS07_BACI_2015.to_csv('./Resilience/HS07/resilience_2015.csv')

HS07_BACI_2016 = pd.read_csv('./Resilience/HS07/resilience_2016.csv')
# HS07_BACI_2016['Year'] = 2016
# HS07_BACI_2016 = HS07_BACI_2016.iloc[: , 1:]
# HS07_BACI_2016.to_csv('./Resilience/HS07/resilience_2016.csv')

HS07_BACI_2017 = pd.read_csv('./Resilience/HS07/resilience_2017.csv')
# HS07_BACI_2017['Year'] = 2017
# HS07_BACI_2017 = HS07_BACI_2017.iloc[: , 1:]
# HS07_BACI_2017.to_csv('./Resilience/HS07/resilience_2017.csv')

HS07_BACI_2018 = pd.read_csv('./Resilience/HS07/resilience_2018.csv')
# HS07_BACI_2018['Year'] = 2018
# HS07_BACI_2018 = HS07_BACI_2018.iloc[: , 1:]
# HS07_BACI_2018.to_csv('./Resilience/HS07/resilience_2018.csv')

HS07_BACI_2019 = pd.read_csv('./Resilience/HS07/resilience_2019.csv')
# HS07_BACI_2019['Year'] = 2019
# HS07_BACI_2019 = HS07_BACI_2019.iloc[: , 1:]
# HS07_BACI_2019.to_csv('./Resilience/HS07/resilience_2019.csv')

HS07_BACI_2020 = pd.read_csv('./Resilience/HS07/resilience_2020.csv')
# HS07_BACI_2020['Year'] = 2020
# HS07_BACI_2020 = HS07_BACI_2011.iloc[: , 1:]
# HS07_BACI_2020.to_csv('./Resilience/HS07/resilience_2020.csv')


#HS12
#import resilience files and small clean 
HS12_BACI_2012 = pd.read_csv('./Resilience/HS12/resilience_2012.csv')
# HS12_BACI_2012['Year'] = 2012
# HS12_BACI_2012 = HS12_BACI_2012.iloc[: , 1:]
# HS12_BACI_2012.to_csv('./Resilience/HS12/resilience_2012.csv')

HS12_BACI_2013 = pd.read_csv('./Resilience/HS12/resilience_2013.csv')
# HS12_BACI_2013['Year'] = 2013
# HS12_BACI_2013 = HS12_BACI_2013.iloc[: , 1:]
# HS12_BACI_2013.to_csv('./Resilience/HS12/resilience_2013.csv')

HS12_BACI_2014 = pd.read_csv('./Resilience/HS12/resilience_2014.csv')
# HS12_BACI_2014['Year'] = 2014
# HS12_BACI_2014 = HS12_BACI_2014.iloc[: , 1:]
# HS12_BACI_2014.to_csv('./Resilience/HS12/resilience_2014.csv')

HS12_BACI_2015 = pd.read_csv('./Resilience/HS12/resilience_2015.csv')
# HS12_BACI_2015['Year'] = 2015
# HS12_BACI_2015 = HS12_BACI_2015.iloc[: , 1:]
# HS12_BACI_2015.to_csv('./Resilience/HS12/resilience_2015.csv')

HS12_BACI_2016 = pd.read_csv('./Resilience/HS12/resilience_2016.csv')
# HS12_BACI_2016['Year'] = 2016
# HS12_BACI_2016 = HS12_BACI_2016.iloc[: , 1:]
# HS12_BACI_2016.to_csv('./Resilience/HS12/resilience_2016.csv')

HS12_BACI_2017 = pd.read_csv('./Resilience/HS12/resilience_2017.csv')
# HS12_BACI_2017['Year'] = 2017
# HS12_BACI_2017 = HS12_BACI_2012.iloc[: , 1:]
# HS12_BACI_2017.to_csv('./Resilience/HS12/resilience_2017.csv')

HS12_BACI_2018 = pd.read_csv('./Resilience/HS12/resilience_2018.csv')
# HS12_BACI_2018['Year'] = 2018
# HS12_BACI_2018 = HS12_BACI_2018.iloc[: , 1:]
# HS12_BACI_2018.to_csv('./Resilience/HS12/resilience_2018.csv')

HS12_BACI_2019 = pd.read_csv('./Resilience/HS12/resilience_2019.csv')
# HS12_BACI_2019['Year'] = 2019
# HS12_BACI_2019 = HS12_BACI_2019.iloc[: , 1:]
# HS12_BACI_2019.to_csv('./Resilience/HS12/resilience_2019.csv')

HS12_BACI_2020 = pd.read_csv('./Resilience/HS12/resilience_2020.csv')
# HS12_BACI_2020['Year'] = 2020
# HS12_BACI_2020 = HS12_BACI_2012.iloc[: , 1:]
# HS12_BACI_2020.to_csv('./Resilience/HS12/resilience_2020.csv')

# sort descending or select max 10 (q)
HS07_sort_2010 = HS07_BACI_2010.sort_values(by='alpha', ascending=False)
HS07_sort_2011 = HS07_BACI_2011.sort_values(by='alpha', ascending=False)
HS07_sort_2012 = HS07_BACI_2012.sort_values(by='alpha', ascending=False)
HS07_sort_2013 = HS07_BACI_2013.sort_values(by='alpha', ascending=False)
HS07_sort_2014 = HS07_BACI_2014.sort_values(by='alpha', ascending=False)
HS07_sort_2015 = HS07_BACI_2015.sort_values(by='alpha', ascending=False)
HS07_sort_2016 = HS07_BACI_2016.sort_values(by='alpha', ascending=False)
HS07_sort_2017 = HS07_BACI_2017.sort_values(by='alpha', ascending=False)
HS07_sort_2018 = HS07_BACI_2018.sort_values(by='alpha', ascending=False)
HS07_sort_2019 = HS07_BACI_2019.sort_values(by='alpha', ascending=False)
HS07_sort_2020 = HS07_BACI_2020.sort_values(by='alpha', ascending=False)

HS12_sort_2012 = HS12_BACI_2012.sort_values(by='alpha', ascending=False)
HS12_sort_2013 = HS12_BACI_2013.sort_values(by='alpha', ascending=False)
HS12_sort_2014 = HS12_BACI_2014.sort_values(by='alpha', ascending=False)
HS12_sort_2015 = HS12_BACI_2015.sort_values(by='alpha', ascending=False)
HS12_sort_2016 = HS12_BACI_2016.sort_values(by='alpha', ascending=False)
HS12_sort_2017 = HS12_BACI_2017.sort_values(by='alpha', ascending=False)
HS12_sort_2018 = HS12_BACI_2018.sort_values(by='alpha', ascending=False)
HS12_sort_2019 = HS12_BACI_2019.sort_values(by='alpha', ascending=False)
HS12_sort_2020 = HS12_BACI_2020.sort_values(by='alpha', ascending=False)

#%%
# plot top 10 alpha value products per year
from textwrap import wrap

#2010 plot
fig = plt.figure(figsize=(18,10))
x = HS07_sort_2010['prod_name'].head(10)
y = HS07_sort_2010['alpha'].head(10)
labels = [ '\n'.join(wrap(l, 20)) for l in x ]
plt.style.use('seaborn-whitegrid')
plt.plot(labels, y, 'o', markerfacecolor='blue')

plt.savefig('./Plots/max_alpha/max_alpha2010.png', dpi=fig.dpi)

#2011 plot
fig = plt.figure(figsize=(18,10))
x = HS07_sort_2011['prod_name'].head(10)
y = HS07_sort_2011['alpha'].head(10)
labels = [ '\n'.join(wrap(l, 20)) for l in x ]
plt.style.use('seaborn-whitegrid')
plt.plot(labels, y, 'o', markerfacecolor='blue')
plt.savefig('./Plots/max_alpha/max_alpha2011.png', dpi=fig.dpi)

#2012 plot
fig = plt.figure(figsize=(18,10))
x = HS07_sort_2012['prod_name'].head(10)
y = HS07_sort_2012['alpha'].head(10)
x2 = HS12_sort_2012['prod_name'].head(10)
y2 = HS12_sort_2012['alpha'].head(10)
labels = [ '\n'.join(wrap(l, 20)) for l in x ]
labels2 = [ '\n'.join(wrap(l, 20)) for l in x2 ]
plt.style.use('seaborn-whitegrid')
plt.plot(labels, y, 'o', markerfacecolor='blue')
plt.plot(labels2, y2, 'o', markerfacecolor='red')
plt.savefig('./Plots/max_alpha/max_alpha2012.png', dpi=fig.dpi)

#2013 plot
fig = plt.figure(figsize=(18,10))
x = HS07_sort_2013['prod_name'].head(10)
y = HS07_sort_2013['alpha'].head(10)
x2 = HS12_sort_2013['prod_name'].head(10)
y2 = HS12_sort_2013['alpha'].head(10)
labels = [ '\n'.join(wrap(l, 20)) for l in x ]
labels2 = [ '\n'.join(wrap(l, 20)) for l in x2 ]
plt.style.use('seaborn-whitegrid')
plt.plot(labels, y, 'o', markerfacecolor='blue')
plt.plot(labels2, y2, 'o', markerfacecolor='red')
plt.savefig('./Plots/max_alpha/max_alpha2013.png', dpi=fig.dpi)

#2014 plot
fig = plt.figure(figsize=(18,10))
x = HS07_sort_2014['prod_name'].head(10)
y = HS07_sort_2014['alpha'].head(10)
x2 = HS12_sort_2014['prod_name'].head(10)
y2 = HS12_sort_2014['alpha'].head(10)
labels = [ '\n'.join(wrap(l, 20)) for l in x ]
labels2 = [ '\n'.join(wrap(l, 20)) for l in x2 ]
plt.style.use('seaborn-whitegrid')
plt.plot(labels, y, 'o', markerfacecolor='blue')
plt.plot(labels2, y2, 'o', markerfacecolor='red')
plt.savefig('./Plots/max_alpha/max_alpha2014.png', dpi=fig.dpi)

#2015 plot
fig = plt.figure(figsize=(18,10))
x = HS07_sort_2015['prod_name'].head(10)
y = HS07_sort_2015['alpha'].head(10)
x2 = HS12_sort_2015['prod_name'].head(10)
y2 = HS12_sort_2015['alpha'].head(10)
labels = [ '\n'.join(wrap(l, 20)) for l in x ]
labels2 = [ '\n'.join(wrap(l, 20)) for l in x2 ]
plt.style.use('seaborn-whitegrid')
plt.plot(labels, y, 'o', markerfacecolor='blue')
plt.plot(labels2, y2, 'o', markerfacecolor='red')
plt.savefig('./Plots/max_alpha/max_alpha2015.png', dpi=fig.dpi)

#2016 plot
fig = plt.figure(figsize=(18,10))
x = HS07_sort_2016['prod_name'].head(10)
y = HS07_sort_2016['alpha'].head(10)
x2 = HS12_sort_2016['prod_name'].head(10)
y2 = HS12_sort_2016['alpha'].head(10)
labels = [ '\n'.join(wrap(l, 20)) for l in x ]
labels2 = [ '\n'.join(wrap(l, 20)) for l in x2 ]
plt.style.use('seaborn-whitegrid')
plt.plot(labels, y, 'o', markerfacecolor='blue')
plt.plot(labels2, y2, 'o', markerfacecolor='red')
plt.savefig('./Plots/max_alpha/max_alpha2016.png', dpi=fig.dpi)

#2017 plot
fig = plt.figure(figsize=(18,10))
x = HS07_sort_2017['prod_name'].head(10)
y = HS07_sort_2017['alpha'].head(10)
x2 = HS12_sort_2017['prod_name'].head(10)
y2 = HS12_sort_2017['alpha'].head(10)
labels = [ '\n'.join(wrap(l, 20)) for l in x ]
labels2 = [ '\n'.join(wrap(l, 20)) for l in x2 ]
plt.style.use('seaborn-whitegrid')
plt.plot(labels, y, 'o', markerfacecolor='blue')
plt.plot(labels2, y2, 'o', markerfacecolor='red')
plt.savefig('./Plots/max_alpha/max_alpha2017.png', dpi=fig.dpi)

#2018 plot
fig = plt.figure(figsize=(18,10))
x = HS07_sort_2018['prod_name'].head(10)
y = HS07_sort_2018['alpha'].head(10)
x2 = HS12_sort_2018['prod_name'].head(10)
y2 = HS12_sort_2018['alpha'].head(10)
labels = [ '\n'.join(wrap(l, 20)) for l in x ]
labels2 = [ '\n'.join(wrap(l, 20)) for l in x2 ]
plt.style.use('seaborn-whitegrid')
plt.plot(labels, y, 'o', markerfacecolor='blue')
plt.plot(labels2, y2, 'o', markerfacecolor='red')
plt.savefig('./Plots/max_alpha/max_alpha2018.png', dpi=fig.dpi)

#2019 plot
fig = plt.figure(figsize=(18,10))
x = HS07_sort_2019['prod_name'].head(10)
y = HS07_sort_2019['alpha'].head(10)
x2 = HS12_sort_2019['prod_name'].head(10)
y2 = HS12_sort_2019['alpha'].head(10)
labels = [ '\n'.join(wrap(l, 20)) for l in x ]
labels2 = [ '\n'.join(wrap(l, 20)) for l in x2 ]
plt.style.use('seaborn-whitegrid')
plt.plot(labels, y, 'o', markerfacecolor='blue')
plt.plot(labels2, y2, 'o', markerfacecolor='red')
plt.savefig('./Plots/max_alpha/max_alpha2019.png', dpi=fig.dpi)

#2020 plot
fig = plt.figure(figsize=(18,10))
x = HS07_sort_2020['prod_name'].head(10)
y = HS07_sort_2020['alpha'].head(10)
x2 = HS12_sort_2020['prod_name'].head(10)
y2 = HS12_sort_2020['alpha'].head(10)
labels = [ '\n'.join(wrap(l, 20)) for l in x ]
labels2 = [ '\n'.join(wrap(l, 20)) for l in x2 ]
plt.style.use('seaborn-whitegrid')
plt.plot(labels, y, 'o', markerfacecolor='blue')
plt.plot(labels2, y2, 'o', markerfacecolor='red')
plt.savefig('./Plots/max_alpha/max_alpha2020.png', dpi=fig.dpi)

# Batteries overtime

battery_HS6 = [850650,854810,850690]

#create df
battery_df = HS07_BACI_2010[HS07_BACI_2010['product'].isin(battery_HS6)]
# battery_df = pd.DataFrame()

# #append HS07 years
to_append = HS07_BACI_2011[HS07_BACI_2011['product'].isin(battery_HS6)]   #2011
battery_df = battery_df.append(to_append)
to_append = HS07_BACI_2012[HS07_BACI_2012['product'].isin(battery_HS6)]   #2012
battery_df = battery_df.append(to_append)
to_append = HS07_BACI_2013[HS07_BACI_2013['product'].isin(battery_HS6)]   #2013
battery_df = battery_df.append(to_append)
to_append = HS07_BACI_2014[HS07_BACI_2014['product'].isin(battery_HS6)]   #2014
battery_df = battery_df.append(to_append)
to_append = HS07_BACI_2015[HS07_BACI_2015['product'].isin(battery_HS6)]   #2015
battery_df = battery_df.append(to_append)
to_append = HS07_BACI_2016[HS07_BACI_2016['product'].isin(battery_HS6)]   #2016
battery_df = battery_df.append(to_append)
to_append = HS07_BACI_2017[HS07_BACI_2017['product'].isin(battery_HS6)]   #2017
battery_df = battery_df.append(to_append)
to_append = HS07_BACI_2018[HS07_BACI_2018['product'].isin(battery_HS6)]   #2018
battery_df = battery_df.append(to_append)
to_append = HS07_BACI_2019[HS07_BACI_2019['product'].isin(battery_HS6)]   #2019
battery_df = battery_df.append(to_append)
to_append = HS07_BACI_2020[HS07_BACI_2020['product'].isin(battery_HS6)]   #2020
battery_df = battery_df.append(to_append)

#append HS12 years
# to_append = HS12_sort_2012[HS12_sort_2012['product'].isin(battery_HS6)]   #2012
# battery_df = battery_df.append(to_append)
# to_append = HS12_sort_2013[HS12_sort_2013['product'].isin(battery_HS6)]   #2013
# battery_df = battery_df.append(to_append)
# to_append = HS12_sort_2014[HS12_sort_2014['product'].isin(battery_HS6)]   #2014
# battery_df = battery_df.append(to_append)
# to_append = HS12_sort_2015[HS12_sort_2015['product'].isin(battery_HS6)]   #2015
# battery_df = battery_df.append(to_append)
# to_append = HS12_sort_2016[HS12_sort_2016['product'].isin(battery_HS6)]   #2016
# battery_df = battery_df.append(to_append)
# to_append = HS12_sort_2017[HS12_sort_2017['product'].isin(battery_HS6)]   #2017
# battery_df = battery_df.append(to_append)
# to_append = HS12_sort_2018[HS12_sort_2018['product'].isin(battery_HS6)]   #2018
# battery_df = battery_df.append(to_append)
# to_append = HS12_sort_2019[HS12_sort_2019['product'].isin(battery_HS6)]   #2019
# battery_df = battery_df.append(to_append)
# to_append = HS12_sort_2020[HS12_sort_2020['product'].isin(battery_HS6)]   #2020
# battery_df = battery_df.append(to_append)

# Plot battery

#seperate by product
battery_850650 = battery_df[battery_df['product']==850650]
battery_854810 = battery_df[battery_df['product']==854810]
battery_850690 = battery_df[battery_df['product']==850690]
battery_850760 = battery_df[battery_df['product']==850760]

fig = plt.figure(figsize=(20,10))

# plotting the points
plt.plot(battery_850650['Year'], battery_850650['alpha'], label = "Cells and batteries: primary, lithium") 
plt.plot(battery_854810['Year'], battery_854810['alpha'], label = "Waste and scrap of primary cells, primary batteries and electric accumulators..") 
plt.plot(battery_850690['Year'], battery_850690['alpha'], label = 'Cells and batteries: primary, parts thereof')
plt.plot(battery_850760['Year'], battery_850760['alpha'], label = 'Electric accumulators: lithium-ion, including separators, whether or not rectangular (including square)')
               
plt.xlabel('year')
plt.ylabel('alpha')
plt.legend( loc='best')
plt.savefig('./Plots/products_overtime/batteries_overtime_HS07.png', dpi=fig.dpi)

# Electrical Accumulators overtime

accumulators_HS6 = [850710,850720,850730,850740,850760,850780,850790]  #ONLY [850780, 850730] ARE PRESENT !!!!!

#create df
accumulators_df = HS07_BACI_2010[HS07_BACI_2010['product'].isin(accumulators_HS6)]
# accumulators_df = pd.DataFrame()

#append HS07 years
to_append = HS07_BACI_2011[HS07_BACI_2011['product'].isin(accumulators_HS6)]   #2011
accumulators_df = accumulators_df.append(to_append)
to_append = HS07_BACI_2012[HS07_BACI_2012['product'].isin(accumulators_HS6)]   #2012
accumulators_df = accumulators_df.append(to_append)
to_append = HS07_BACI_2013[HS07_BACI_2013['product'].isin(accumulators_HS6)]   #2013
accumulators_df = accumulators_df.append(to_append)
to_append = HS07_BACI_2014[HS07_BACI_2014['product'].isin(accumulators_HS6)]   #2014
accumulators_df = accumulators_df.append(to_append)
to_append = HS07_BACI_2015[HS07_BACI_2015['product'].isin(accumulators_HS6)]   #2015
accumulators_df = accumulators_df.append(to_append)
to_append = HS07_BACI_2016[HS07_BACI_2016['product'].isin(accumulators_HS6)]   #2016
accumulators_df = accumulators_df.append(to_append)
to_append = HS07_BACI_2017[HS07_BACI_2017['product'].isin(accumulators_HS6)]   #2017
accumulators_df = accumulators_df.append(to_append)
to_append = HS07_BACI_2018[HS07_BACI_2018['product'].isin(accumulators_HS6)]   #2018
accumulators_df = accumulators_df.append(to_append)
to_append = HS07_BACI_2019[HS07_BACI_2019['product'].isin(accumulators_HS6)]   #2019
accumulators_df = accumulators_df.append(to_append)
to_append = HS07_BACI_2020[HS07_BACI_2020['product'].isin(accumulators_HS6)]   #2020
accumulators_df = accumulators_df.append(to_append)

# #append HS12 years
# to_append = HS12_sort_2012[HS12_sort_2012['product'].isin(accumulators_HS6)]   #2012
# accumulators_df = accumulators_df.append(to_append)
# to_append = HS12_sort_2013[HS12_sort_2013['product'].isin(accumulators_HS6)]   #2013
# accumulators_df = accumulators_df.append(to_append)
# to_append = HS12_sort_2014[HS12_sort_2014['product'].isin(accumulators_HS6)]   #2014
# accumulators_df = accumulators_df.append(to_append)
# to_append = HS12_sort_2015[HS12_sort_2015['product'].isin(accumulators_HS6)]   #2015
# accumulators_df = accumulators_df.append(to_append)
# to_append = HS12_sort_2016[HS12_sort_2016['product'].isin(accumulators_HS6)]   #2016
# accumulators_df = accumulators_df.append(to_append)
# to_append = HS12_sort_2017[HS12_sort_2017['product'].isin(accumulators_HS6)]   #2017
# accumulators_df = accumulators_df.append(to_append)
# to_append = HS12_sort_2018[HS12_sort_2018['product'].isin(accumulators_HS6)]   #2018
# accumulators_df = accumulators_df.append(to_append)
# to_append = HS12_sort_2019[HS12_sort_2019['product'].isin(accumulators_HS6)]   #2019
# accumulators_df = accumulators_df.append(to_append)
# to_append = HS12_sort_2020[HS12_sort_2020['product'].isin(accumulators_HS6)]   #2020
# accumulators_df = accumulators_df.append(to_append)


# Plot accumulator

#seperate by product
accumulator_850710 = accumulators_df[accumulators_df['product']==850710]
accumulator_850720 = accumulators_df[accumulators_df['product']==850720]
accumulator_850730 = accumulators_df[accumulators_df['product']==850730]
accumulator_850740 = accumulators_df[accumulators_df['product']==850740]
accumulator_850780 = accumulators_df[accumulators_df['product']==850780]
accumulator_850790 = accumulators_df[accumulators_df['product']==850790]
accumulator_850760 = accumulators_df[accumulators_df['product']==850760]


fig = plt.figure(figsize=(20,10))

# plotting the points 
plt.plot(accumulator_850710['Year'], accumulator_850710['alpha'], label = "Electric accumulators: lead-acid, of a kind used for starting piston engines, including separators, whether or not rectangular (including square)") 
plt.plot(accumulator_850720['Year'], accumulator_850720['alpha'], label = "Electric accumulators: lead-acid, (other than for starting piston engines), including separators, whether or not rectangular (including square)") 
plt.plot(accumulator_850730['Year'], accumulator_850730['alpha'], label = "Electric accumulators: nickel-cadmium, including separators, whether or not rectangular (including square)") 
plt.plot(accumulator_850740['Year'], accumulator_850740['alpha'], label = "Electric accumulators: nickel-iron, including separators, whether or not rectangular (including square)") 
plt.plot(accumulator_850780['Year'], accumulator_850780['alpha'], label = "Electric accumulators: n.e.c. in heading no. 8507, including separators, whether or not rectangular (including square)") 
plt.plot(accumulator_850790['Year'], accumulator_850790['alpha'], label = "Electric accumulators: parts n.e.c. in heading no. 8507") 
plt.plot(accumulator_850760['Year'], accumulator_850760['alpha'], label = "Electric accumulators: lithium-ion, including separators, whether or not rectangular (including square)") 


plt.xlabel('year')
plt.ylabel('alpha')
plt.legend( loc='best')
plt.savefig('./Plots/products_overtime/accumulators_overtime_HS07.png', dpi=fig.dpi)

# Turbines overtime

turbines_HS6 = [840681,840682,840690,841011,841012,841013,841090,841181,841182,841199]  #ONLY [840681, 840682, 840690. 841199]  ARE PRESENT !!!!!

#create df
turbines_df = HS07_BACI_2010[HS07_BACI_2010['product'].isin(turbines_HS6)]
turbines_df = pd.DataFrame()

#append HS07 years
to_append = HS07_BACI_2011[HS07_BACI_2011['product'].isin(turbines_HS6)]   #2011
turbines_df = turbines_df.append(to_append)
to_append = HS07_BACI_2012[HS07_BACI_2012['product'].isin(turbines_HS6)]   #2012
turbines_df = turbines_df.append(to_append)
to_append = HS07_BACI_2013[HS07_BACI_2013['product'].isin(turbines_HS6)]   #2013
turbines_df = turbines_df.append(to_append)
to_append = HS07_BACI_2014[HS07_BACI_2014['product'].isin(turbines_HS6)]   #2014
turbines_df = turbines_df.append(to_append)
to_append = HS07_BACI_2015[HS07_BACI_2015['product'].isin(turbines_HS6)]   #2015
turbines_df = turbines_df.append(to_append)
to_append = HS07_BACI_2016[HS07_BACI_2016['product'].isin(turbines_HS6)]   #2016
turbines_df = turbines_df.append(to_append)
to_append = HS07_BACI_2017[HS07_BACI_2017['product'].isin(turbines_HS6)]   #2017
turbines_df = turbines_df.append(to_append)
to_append = HS07_BACI_2018[HS07_BACI_2018['product'].isin(turbines_HS6)]   #2018
turbines_df = turbines_df.append(to_append)
to_append = HS07_BACI_2019[HS07_BACI_2019['product'].isin(turbines_HS6)]   #2019
turbines_df = turbines_df.append(to_append)
to_append = HS07_BACI_2020[HS07_BACI_2020['product'].isin(turbines_HS6)]   #2020
turbines_df = turbines_df.append(to_append)

# #append HS12 years
# to_append = HS12_sort_2012[HS12_sort_2012['product'].isin(turbines_HS6)]   #2012
# turbines_df = turbines_df.append(to_append)
# to_append = HS12_sort_2013[HS12_sort_2013['product'].isin(turbines_HS6)]   #2013
# turbines_df = turbines_df.append(to_append)
# to_append = HS12_sort_2014[HS12_sort_2014['product'].isin(turbines_HS6)]   #2014
# turbines_df = turbines_df.append(to_append)
# to_append = HS12_sort_2015[HS12_sort_2015['product'].isin(turbines_HS6)]   #2015
# turbines_df = turbines_df.append(to_append)
# to_append = HS12_sort_2016[HS12_sort_2016['product'].isin(turbines_HS6)]   #2016
# turbines_df = turbines_df.append(to_append)
# to_append = HS12_sort_2017[HS12_sort_2017['product'].isin(turbines_HS6)]   #2017
# turbines_df = turbines_df.append(to_append)
# to_append = HS12_sort_2018[HS12_sort_2018['product'].isin(turbines_HS6)]   #2018
# turbines_df = turbines_df.append(to_append)
# to_append = HS12_sort_2019[HS12_sort_2019['product'].isin(turbines_HS6)]   #2019
# turbines_df = turbines_df.append(to_append)
# to_append = HS12_sort_2020[HS12_sort_2020['product'].isin(turbines_HS6)]   #2020
# turbines_df = turbines_df.append(to_append)


#seperate by product 
turbines_840681 = turbines_df[turbines_df['product']==840681]
turbines_840682 = turbines_df[turbines_df['product']==840682]
turbines_840690 = turbines_df[turbines_df['product']==840690]
turbines_841011 = turbines_df[turbines_df['product']==841011]
turbines_841012 = turbines_df[turbines_df['product']==841012]
turbines_841013 = turbines_df[turbines_df['product']==841013]
turbines_841090 = turbines_df[turbines_df['product']==841090]
turbines_841181 = turbines_df[turbines_df['product']==841181]
turbines_841182 = turbines_df[turbines_df['product']==841182]
turbines_841199 = turbines_df[turbines_df['product']==841199]

fig = plt.figure(figsize=(20,10))

# plotting the points
plt.plot(turbines_840681['Year'], turbines_840681['alpha'], label = "Turbines: steam and other vapour turbines, (for other than marine propulsion), of an output exceeding 40MW") 
plt.plot(turbines_840682['Year'], turbines_840682['alpha'], label = "Turbines: steam and other vapour turbines, (for other than marine propulsion), of an output not exceeding 40MW") 
plt.plot(turbines_840690['Year'], turbines_840690['alpha'], label = "Turbines: parts of steam and other vapour turbines") 
plt.plot(turbines_841011['Year'], turbines_841011['alpha'], label ='Turbines: hydraulic turbines and water wheels, of a power not exceeding 1000kW')
plt.plot(turbines_841012['Year'], turbines_841012['alpha'], label ='Turbines: hydraulic turbines and water wheels, of a power exceeding 1000kW but not exceeding 10000kW')
plt.plot(turbines_841013['Year'], turbines_841013['alpha'], label ='Turbines: hydraulic turbines and water wheels, of a power exceeding 10000kW')
plt.plot(turbines_841090['Year'], turbines_841090['alpha'], label ='Turbines: parts of hydraulic turbines and water wheels, including regulators')
plt.plot(turbines_841181['Year'], turbines_841181['alpha'], label ='Turbines: gas-turbines (excluding turbo-jets and turbo-propellers), of a power not exceeding 5000kW')
plt.plot(turbines_841182['Year'], turbines_841182['alpha'], label ='Turbines: gas-turbines (excluding turbo-jets and turbo-propellers), of a power exceeding 5000kW')
plt.plot(turbines_841199['Year'], turbines_841199['alpha'], label = "Turbines: parts of gas turbines (excluding turbo-jets and turbo-propellers)")   

plt.xlabel('year')
plt.ylabel('alpha')
plt.legend( loc='best')
plt.savefig('./Plots/products_overtime/turbines_overtime_HS07.png', dpi=fig.dpi)

#%% Electric Vehicles overtime ## USE FOR 2017 DATA
EV_HS6= [870911,0]

#create df
EV_df = HS12_BACI_2012[HS12_BACI_2012['product'].isin(EV_HS6)]

# append HS12 years
to_append = HS12_sort_2013[HS12_sort_2013['product'].isin(EV_HS6)]   #2013
EV_df = EV_df.append(to_append)
to_append = HS12_sort_2014[HS12_sort_2014['product'].isin(EV_HS6)]   #2014
EV_df = EV_df.append(to_append)
to_append = HS12_sort_2015[HS12_sort_2015['product'].isin(EV_HS6)]   #2015
EV_df = EV_df.append(to_append)
to_append = HS12_sort_2016[HS12_sort_2016['product'].isin(EV_HS6)]   #2016
EV_df = EV_df.append(to_append)
to_append = HS12_sort_2017[HS12_sort_2017['product'].isin(EV_HS6)]   #2017
EV_df = EV_df.append(to_append)
to_append = HS12_sort_2018[HS12_sort_2018['product'].isin(EV_HS6)]   #2018
EV_df = EV_df.append(to_append)
to_append = HS12_sort_2019[HS12_sort_2019['product'].isin(EV_HS6)]   #2019
EV_df = EV_df.append(to_append)
to_append = HS12_sort_2020[HS12_sort_2020['product'].isin(EV_HS6)]   #2020
EV_df = EV_df.append(to_append)

#seperate by product 
EV_870911= EV_df[EV_df['product']==870911]

fig = plt.figure(figsize=(20,10))

# plotting the points
plt.plot(EV_870911['Year'], EV_870911['alpha'], label = "Vehicles: electrical, self-propelled, (not fitted with lifting or handling equipment), of the type used for short distance transport of goods in factories, warehouses, dock areas or airports") 

plt.xlabel('year')
plt.ylabel('alpha')
plt.legend( loc='best')
plt.savefig('./Plots/products_overtime/EV_overtime_HS12.png', dpi=fig.dpi)

#%% Most 'important' cobalt products
# Primary/Refined/Recycling and Collection Cobalt overtime

cobalt_prod_HS6 = [260500,
750300,
810530,
810520,
750110,
282200,
282739,
283329
]  

#create df
cobalt_prod_df = HS07_BACI_2010[HS07_BACI_2010['product'].isin(cobalt_prod_HS6)]
# cobalt_prod_df = pd.DataFrame()

#append HS07 years
to_append = HS07_BACI_2011[HS07_BACI_2011['product'].isin(cobalt_prod_HS6)]   #2011
cobalt_prod_df = cobalt_prod_df.append(to_append)
to_append = HS07_BACI_2012[HS07_BACI_2012['product'].isin(cobalt_prod_HS6)]   #2012
cobalt_prod_df = cobalt_prod_df.append(to_append)
to_append = HS07_BACI_2013[HS07_BACI_2013['product'].isin(cobalt_prod_HS6)]   #2013
cobalt_prod_df = cobalt_prod_df.append(to_append)
to_append = HS07_BACI_2014[HS07_BACI_2014['product'].isin(cobalt_prod_HS6)]   #2014
cobalt_prod_df = cobalt_prod_df.append(to_append)
to_append = HS07_BACI_2015[HS07_BACI_2015['product'].isin(cobalt_prod_HS6)]   #2015
cobalt_prod_df = cobalt_prod_df.append(to_append)
to_append = HS07_BACI_2016[HS07_BACI_2016['product'].isin(cobalt_prod_HS6)]   #2016
cobalt_prod_df = cobalt_prod_df.append(to_append)
to_append = HS07_BACI_2017[HS07_BACI_2017['product'].isin(cobalt_prod_HS6)]   #2017
cobalt_prod_df = cobalt_prod_df.append(to_append)
to_append = HS07_BACI_2018[HS07_BACI_2018['product'].isin(cobalt_prod_HS6)]   #2018
cobalt_prod_df = cobalt_prod_df.append(to_append)
to_append = HS07_BACI_2019[HS07_BACI_2019['product'].isin(cobalt_prod_HS6)]   #2019
cobalt_prod_df = cobalt_prod_df.append(to_append)
to_append = HS07_BACI_2020[HS07_BACI_2020['product'].isin(cobalt_prod_HS6)]   #2020
cobalt_prod_df = cobalt_prod_df.append(to_append)

# #append HS12 years
# to_append = HS12_sort_2012[HS12_sort_2012['product'].isin(cobalt_prod_HS6)]   #2012
# cobalt_prod_df = cobalt_prod_df.append(to_append)
# to_append = HS12_sort_2013[HS12_sort_2013['product'].isin(cobalt_prod_HS6)]   #2013
# cobalt_prod_df = cobalt_prod_df.append(to_append)
# to_append = HS12_sort_2014[HS12_sort_2014['product'].isin(cobalt_prod_HS6)]   #2014
# cobalt_prod_df = cobalt_prod_df.append(to_append)
# to_append = HS12_sort_2015[HS12_sort_2015['product'].isin(cobalt_prod_HS6)]   #2015
# cobalt_prod_df = cobalt_prod_df.append(to_append)
# to_append = HS12_sort_2016[HS12_sort_2016['product'].isin(cobalt_prod_HS6)]   #2016
# cobalt_prod_df = cobalt_prod_df.append(to_append)
# to_append = HS12_sort_2017[HS12_sort_2017['product'].isin(cobalt_prod_HS6)]   #2017
# cobalt_prod_df = cobalt_prod_df.append(to_append)
# to_append = HS12_sort_2018[HS12_sort_2018['product'].isin(cobalt_prod_HS6)]   #2018
# cobalt_prod_df = cobalt_prod_df.append(to_append)
# to_append = HS12_sort_2019[HS12_sort_2019['product'].isin(cobalt_prod_HS6)]   #2019
# cobalt_prod_df = cobalt_prod_df.append(to_append)
# to_append = HS12_sort_2020[HS12_sort_2020['product'].isin(cobalt_prod_HS6)]   #2020
# cobalt_prod_df = cobalt_prod_df.append(to_append)

[260500,
750300,
810530,
810520,
750110,
282200,
282739,
283329
]  
# Plot cobaly products

#seperate by product
cobalt_prod_260500 = cobalt_prod_df[cobalt_prod_df['product']==260500]
cobalt_prod_750300 = cobalt_prod_df[cobalt_prod_df['product']==750300]
cobalt_prod_810530 = cobalt_prod_df[cobalt_prod_df['product']==810530]
cobalt_prod_810520 = cobalt_prod_df[cobalt_prod_df['product']==810520]
cobalt_prod_750110 = cobalt_prod_df[cobalt_prod_df['product']==750110]
cobalt_prod_282200 = cobalt_prod_df[cobalt_prod_df['product']==282200]
cobalt_prod_282739 = cobalt_prod_df[cobalt_prod_df['product']==282739]
cobalt_prod_283329 = cobalt_prod_df[cobalt_prod_df['product']==283329]

fig = plt.figure(figsize=(20,10))

# plotting the points 
plt.plot(cobalt_prod_260500['Year'], cobalt_prod_260500['alpha'], label = "Cobalt ores and concentrates (1988-2500)") 
plt.plot(cobalt_prod_750300['Year'], cobalt_prod_750300['alpha'], label = "Waste and scrap, of nickel alloys (excl. ingots or other similar unwrought shapes, of remelted nickel alloys waste and scrap, ashes and residues containing nickel alloys)") 
plt.plot(cobalt_prod_810530['Year'], cobalt_prod_810530['alpha'], label = "Cobalt waste and scrap (excl. ash and residues containingcobalt)(2002-2500)") 
plt.plot(cobalt_prod_810520['Year'], cobalt_prod_810520['alpha'], label = "Cobalt mattes and other intermediate products of cobalt metallurgy; unwrought cobalt; cobalt powders(2002-2500)") 
plt.plot(cobalt_prod_750110['Year'], cobalt_prod_750110['alpha'], label = "Nickel mattes") 
plt.plot(cobalt_prod_282200['Year'], cobalt_prod_282200['alpha'], label = "Cobalt oxides and hydroxides; commercial cobalt oxides(1988-2500)") 
plt.plot(cobalt_prod_283329['Year'], cobalt_prod_283329['alpha'], label = "Cobalt chlorides(2007-2500)") 
plt.plot(cobalt_prod_283329['Year'], cobalt_prod_283329['alpha'], label = "Sulphates of cobalt and of titanium(1988-2500)") 


plt.xlabel('year')
plt.ylabel('alpha')
plt.legend( loc='best')
plt.savefig('./Plots/products_overtime/cobalt_prod_overtime_HS07.png', dpi=fig.dpi)


#%% 
# Biomass overtime

biomass_HS6 = [840610,
840681,
840682,
840690,
841191,
841199,
842112
]  

#create df
biomass_df = HS07_BACI_2010[HS07_BACI_2010['product'].isin(biomass_HS6)]
# biomass_df = pd.DataFrame()

#append HS07 years
to_append = HS07_BACI_2011[HS07_BACI_2011['product'].isin(biomass_HS6)]   #2011
biomass_df = biomass_df.append(to_append)
to_append = HS07_BACI_2012[HS07_BACI_2012['product'].isin(biomass_HS6)]   #2012
biomass_df = biomass_df.append(to_append)
to_append = HS07_BACI_2013[HS07_BACI_2013['product'].isin(biomass_HS6)]   #2013
biomass_df = biomass_df.append(to_append)
to_append = HS07_BACI_2014[HS07_BACI_2014['product'].isin(biomass_HS6)]   #2014
biomass_df = biomass_df.append(to_append)
to_append = HS07_BACI_2015[HS07_BACI_2015['product'].isin(biomass_HS6)]   #2015
biomass_df = biomass_df.append(to_append)
to_append = HS07_BACI_2016[HS07_BACI_2016['product'].isin(biomass_HS6)]   #2016
biomass_df = biomass_df.append(to_append)
to_append = HS07_BACI_2017[HS07_BACI_2017['product'].isin(biomass_HS6)]   #2017
biomass_df = biomass_df.append(to_append)
to_append = HS07_BACI_2018[HS07_BACI_2018['product'].isin(biomass_HS6)]   #2018
biomass_df = biomass_df.append(to_append)
to_append = HS07_BACI_2019[HS07_BACI_2019['product'].isin(biomass_HS6)]   #2019
biomass_df = biomass_df.append(to_append)
to_append = HS07_BACI_2020[HS07_BACI_2020['product'].isin(biomass_HS6)]   #2020
biomass_df = biomass_df.append(to_append)

# #append HS12 years
# to_append = HS12_sort_2012[HS12_sort_2012['product'].isin(biomass_HS6)]   #2012
# biomass_df = biomass_df.append(to_append)
# to_append = HS12_sort_2013[HS12_sort_2013['product'].isin(biomass_HS6)]   #2013
# biomass_df = biomass_df.append(to_append)
# to_append = HS12_sort_2014[HS12_sort_2014['product'].isin(biomass_HS6)]   #2014
# biomass_df = biomass_df.append(to_append)
# to_append = HS12_sort_2015[HS12_sort_2015['product'].isin(biomass_HS6)]   #2015
# biomass_df = biomass_df.append(to_append)
# to_append = HS12_sort_2016[HS12_sort_2016['product'].isin(biomass_HS6)]   #2016
# biomass_df = biomass_df.append(to_append)
# to_append = HS12_sort_2017[HS12_sort_2017['product'].isin(biomass_HS6)]   #2017
# biomass_df = biomass_df.append(to_append)
# to_append = HS12_sort_2018[HS12_sort_2018['product'].isin(biomass_HS6)]   #2018
# biomass_df = biomass_df.append(to_append)
# to_append = HS12_sort_2019[HS12_sort_2019['product'].isin(biomass_HS6)]   #2019
# biomass_df = biomass_df.append(to_append)
# to_append = HS12_sort_2020[HS12_sort_2020['product'].isin(biomass_HS6)]   #2020
# biomass_df = biomass_df.append(to_append)

  
# Plot biomass

#seperate by product
biomass_840610 = biomass_df[biomass_df['product']==840610]
biomass_840681 = biomass_df[biomass_df['product']==840681]
biomass_840682 = biomass_df[biomass_df['product']==840682]
biomass_840690 = biomass_df[biomass_df['product']==840690]
biomass_841191 = biomass_df[biomass_df['product']==841191]
biomass_841199 = biomass_df[biomass_df['product']==841199]
biomass_842112 = biomass_df[biomass_df['product']==842112]

fig = plt.figure(figsize=(20,10))

# plotting the points 
plt.plot(biomass_840610['Year'], biomass_840610['alpha'], label = "Turbines: steam and other vapour turbines, for marine propulsion") 
plt.plot(biomass_840681['Year'], biomass_840681['alpha'], label = "Turbines: steam and other vapour turbines, (for other than marine propulsion), of an output exceeding 40MW") 
plt.plot(biomass_840682['Year'], biomass_840682['alpha'], label = "Turbines: steam and other vapour turbines, (for other than marine propulsion), of an output not exceeding 40MW") 
plt.plot(biomass_840690['Year'], biomass_840690['alpha'], label = "Turbines: parts of steam and other vapour turbines") 
plt.plot(biomass_841191['Year'], biomass_841191['alpha'], label = "Turbines: parts of turbo-jets and turbo-propellers") 
plt.plot(biomass_841199['Year'], biomass_841199['alpha'], label = "Turbines: parts of gas turbines (excluding turbo-jets and turbo-propellers)") 
plt.plot(biomass_842112['Year'], biomass_842112['alpha'], label = "Centrifuges: clothes-dryers") 


plt.xlabel('year')
plt.ylabel('alpha')
plt.legend( loc='best')
plt.savefig('./Plots/products_overtime/biomass_overtime_HS07.png', dpi=fig.dpi)


#%%
# Geothermal overtime

geothermal_HS6 = [841810,
841821,
841829,
841830,
841840,
841850,
841861,
841869,
841891,
841899
]  

#create df
# geothermal_df = HS07_BACI_2010[HS07_BACI_2010['product'].isin(geothermal_HS6)]
geothermal_df = pd.DataFrame()

#append HS07 years
# to_append = HS07_BACI_2011[HS07_BACI_2011['product'].isin(geothermal_HS6)]   #2011
# geothermal_df = geothermal_df.append(to_append)
# to_append = HS07_BACI_2012[HS07_BACI_2012['product'].isin(geothermal_HS6)]   #2012
# geothermal_df = geothermal_df.append(to_append)
# to_append = HS07_BACI_2013[HS07_BACI_2013['product'].isin(geothermal_HS6)]   #2013
# geothermal_df = geothermal_df.append(to_append)
# to_append = HS07_BACI_2014[HS07_BACI_2014['product'].isin(geothermal_HS6)]   #2014
# geothermal_df = geothermal_df.append(to_append)
# to_append = HS07_BACI_2015[HS07_BACI_2015['product'].isin(geothermal_HS6)]   #2015
# geothermal_df = geothermal_df.append(to_append)
# to_append = HS07_BACI_2016[HS07_BACI_2016['product'].isin(geothermal_HS6)]   #2016
# geothermal_df = geothermal_df.append(to_append)
# to_append = HS07_BACI_2017[HS07_BACI_2017['product'].isin(geothermal_HS6)]   #2017
# geothermal_df = geothermal_df.append(to_append)
# to_append = HS07_BACI_2018[HS07_BACI_2018['product'].isin(geothermal_HS6)]   #2018
# geothermal_df = geothermal_df.append(to_append)
# to_append = HS07_BACI_2019[HS07_BACI_2019['product'].isin(geothermal_HS6)]   #2019
# geothermal_df = geothermal_df.append(to_append)
# to_append = HS07_BACI_2020[HS07_BACI_2020['product'].isin(geothermal_HS6)]   #2020
# geothermal_df = geothermal_df.append(to_append)

#append HS12 years
to_append = HS12_sort_2012[HS12_sort_2012['product'].isin(geothermal_HS6)]   #2012
geothermal_df = geothermal_df.append(to_append)
to_append = HS12_sort_2013[HS12_sort_2013['product'].isin(geothermal_HS6)]   #2013
geothermal_df = geothermal_df.append(to_append)
to_append = HS12_sort_2014[HS12_sort_2014['product'].isin(geothermal_HS6)]   #2014
geothermal_df = geothermal_df.append(to_append)
to_append = HS12_sort_2015[HS12_sort_2015['product'].isin(geothermal_HS6)]   #2015
geothermal_df = geothermal_df.append(to_append)
to_append = HS12_sort_2016[HS12_sort_2016['product'].isin(geothermal_HS6)]   #2016
geothermal_df = geothermal_df.append(to_append)
to_append = HS12_sort_2017[HS12_sort_2017['product'].isin(geothermal_HS6)]   #2017
geothermal_df = geothermal_df.append(to_append)
to_append = HS12_sort_2018[HS12_sort_2018['product'].isin(geothermal_HS6)]   #2018
geothermal_df = geothermal_df.append(to_append)
to_append = HS12_sort_2019[HS12_sort_2019['product'].isin(geothermal_HS6)]   #2019
geothermal_df = geothermal_df.append(to_append)
to_append = HS12_sort_2020[HS12_sort_2020['product'].isin(geothermal_HS6)]   #2020
geothermal_df = geothermal_df.append(to_append)

  
# Plot geothermal

#seperate by product
geothermal_841810 = geothermal_df[geothermal_df['product']==841810]
geothermal_841821 = geothermal_df[geothermal_df['product']==841821]
geothermal_841829 = geothermal_df[geothermal_df['product']==841829]
geothermal_841830 = geothermal_df[geothermal_df['product']==841830]
geothermal_841840 = geothermal_df[geothermal_df['product']==841840]
geothermal_841850 = geothermal_df[geothermal_df['product']==841850]
geothermal_841861 = geothermal_df[geothermal_df['product']==841861]
geothermal_841869 = geothermal_df[geothermal_df['product']==841869]
geothermal_841891 = geothermal_df[geothermal_df['product']==841891]
geothermal_841899 = geothermal_df[geothermal_df['product']==841899]

fig = plt.figure(figsize=(20,10))

# plotting the points 
plt.plot(geothermal_841810['Year'], geothermal_841810['alpha'], label = "Refrigerators and freezers: combined refrigerator-freezers, fitted with separate external doors, electric or other") 
plt.plot(geothermal_841821['Year'], geothermal_841821['alpha'], label = "Refrigerators: for household use, compression-type, electric or other") 
plt.plot(geothermal_841829['Year'], geothermal_841829['alpha'], label = "Refrigerators: household, electric or not, other than compression-type") 
plt.plot(geothermal_841830['Year'], geothermal_841830['alpha'], label = "Freezers: of the chest type, not exceeding 800l capacity") 
plt.plot(geothermal_841840['Year'], geothermal_841840['alpha'], label = "Freezers: of the upright type, not exceeding 900l capacity") 
plt.plot(geothermal_841850['Year'], geothermal_841850['alpha'], label = "Furniture incorporating refrigerating or freezing equipment: for storage and display, n.e.c. in item no. 8418.1, 8418.2, 8418.3 or 8418.4 (chests, cabinets, display counters, show-cases and the like)") 
plt.plot(geothermal_841861['Year'], geothermal_841861['alpha'], label = "Heat pumps: other than air conditioning machines of heading no. 8415") 
plt.plot(geothermal_841869['Year'], geothermal_841869['alpha'], label = "Refrigerating or freezing equipment: n.e.c. in heading no. 8418") 
plt.plot(geothermal_841891['Year'], geothermal_841891['alpha'], label = "Refrigerating or freezing equipment: parts, furniture designed to receive refrigerating or freezing equipment") 
plt.plot(geothermal_841899['Year'], geothermal_841899['alpha'], label = "Refrigerating or freezing equipment: parts thereof, other than furniture") 


plt.xlabel('year')
plt.ylabel('alpha')
plt.legend( loc='best')
plt.savefig('./Plots/products_overtime/geothermal_overtime_HS12.png', dpi=fig.dpi)

#%%
# Solar overtime

solar_HS6 = [711510,
850440,
854140
]  

#create df
# solar_df = HS07_BACI_2010[HS07_BACI_2010['product'].isin(solar_HS6)]
solar_df = pd.DataFrame()

#append HS07 years
# to_append = HS07_BACI_2011[HS07_BACI_2011['product'].isin(solar_HS6)]   #2011
# solar_df = solar_df.append(to_append)
# to_append = HS07_BACI_2012[HS07_BACI_2012['product'].isin(solar_HS6)]   #2012
# solar_df = solar_df.append(to_append)
# to_append = HS07_BACI_2013[HS07_BACI_2013['product'].isin(solar_HS6)]   #2013
# solar_df = solar_df.append(to_append)
# to_append = HS07_BACI_2014[HS07_BACI_2014['product'].isin(solar_HS6)]   #2014
# solar_df = solar_df.append(to_append)
# to_append = HS07_BACI_2015[HS07_BACI_2015['product'].isin(solar_HS6)]   #2015
# solar_df = solar_df.append(to_append)
# to_append = HS07_BACI_2016[HS07_BACI_2016['product'].isin(solar_HS6)]   #2016
# solar_df = solar_df.append(to_append)
# to_append = HS07_BACI_2017[HS07_BACI_2017['product'].isin(solar_HS6)]   #2017
# solar_df = solar_df.append(to_append)
# to_append = HS07_BACI_2018[HS07_BACI_2018['product'].isin(solar_HS6)]   #2018
# solar_df = solar_df.append(to_append)
# to_append = HS07_BACI_2019[HS07_BACI_2019['product'].isin(solar_HS6)]   #2019
# solar_df = solar_df.append(to_append)
# to_append = HS07_BACI_2020[HS07_BACI_2020['product'].isin(solar_HS6)]   #2020
# solar_df = solar_df.append(to_append)

#append HS12 years
to_append = HS12_sort_2012[HS12_sort_2012['product'].isin(solar_HS6)]   #2012
solar_df = solar_df.append(to_append)
to_append = HS12_sort_2013[HS12_sort_2013['product'].isin(solar_HS6)]   #2013
solar_df = solar_df.append(to_append)
to_append = HS12_sort_2014[HS12_sort_2014['product'].isin(solar_HS6)]   #2014
solar_df = solar_df.append(to_append)
to_append = HS12_sort_2015[HS12_sort_2015['product'].isin(solar_HS6)]   #2015
solar_df = solar_df.append(to_append)
to_append = HS12_sort_2016[HS12_sort_2016['product'].isin(solar_HS6)]   #2016
solar_df = solar_df.append(to_append)
to_append = HS12_sort_2017[HS12_sort_2017['product'].isin(solar_HS6)]   #2017
solar_df = solar_df.append(to_append)
to_append = HS12_sort_2018[HS12_sort_2018['product'].isin(solar_HS6)]   #2018
solar_df = solar_df.append(to_append)
to_append = HS12_sort_2019[HS12_sort_2019['product'].isin(solar_HS6)]   #2019
solar_df = solar_df.append(to_append)
to_append = HS12_sort_2020[HS12_sort_2020['product'].isin(solar_HS6)]   #2020
solar_df = solar_df.append(to_append)

  
# Plot geothermal

#seperate by product
solar_711510 = solar_df[solar_df['product']==711510]
solar_850440 = solar_df[solar_df['product']==850440]
solar_854140 = solar_df[solar_df['product']==854140]


fig = plt.figure(figsize=(20,10))

# plotting the points 
plt.plot(solar_711510['Year'], solar_711510['alpha'], label = "Metal: catalysts in the form of wire cloth or grill, of platinum") 
plt.plot(solar_850440['Year'], solar_850440['alpha'], label = "Electrical static converters") 
plt.plot(solar_854140['Year'], solar_854140['alpha'], label = "Electrical apparatus: photosensitive, including photovoltaic cells, whether or not assembled in modules or made up into panels, light emitting diodes") 


plt.xlabel('year')
plt.ylabel('alpha')
plt.legend( loc='best')
plt.savefig('./Plots/products_overtime/solar_overtime_HS12.png', dpi=fig.dpi)
