# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 17:22:39 2022

@author: patta
"""

import pandas as pd
import matplotlib.pyplot as plt
#
#import resilience files
BACI_2010 = pd.read_csv('./Resilience/HS07/resilience_2010.csv')
BACI_2011 = pd.read_csv('./Resilience/HS07/resilience_2011.csv')
BACI_2012 = pd.read_csv('./Resilience/HS07/resilience_2012.csv')
BACI_2013 = pd.read_csv('./Resilience/HS07/resilience_2013.csv')
BACI_2014 = pd.read_csv('./Resilience/HS07/resilience_2014.csv')
BACI_2015 = pd.read_csv('./Resilience/HS07/resilience_2015.csv')
BACI_2016 = pd.read_csv('./Resilience/HS07/resilience_2016.csv')
BACI_2017 = pd.read_csv('./Resilience/HS07/resilience_2017.csv')
BACI_2018 = pd.read_csv('./Resilience/HS07/resilience_2018.csv')
BACI_2019 = pd.read_csv('./Resilience/HS07/resilience_2019.csv')
BACI_2020 = pd.read_csv('./Resilience/HS07/resilience_2020.csv')

#%% sort descending or select max 10 (q)
sort_2010 = BACI_2010.sort_values(by='alpha', ascending=False)
sort_2011 = BACI_2011.sort_values(by='alpha', ascending=False)
sort_2012 = BACI_2012.sort_values(by='alpha', ascending=False)
sort_2013 = BACI_2013.sort_values(by='alpha', ascending=False)
sort_2014 = BACI_2014.sort_values(by='alpha', ascending=False)
sort_2015 = BACI_2015.sort_values(by='alpha', ascending=False)
sort_2016 = BACI_2016.sort_values(by='alpha', ascending=False)
sort_2017 = BACI_2017.sort_values(by='alpha', ascending=False)
sort_2018 = BACI_2018.sort_values(by='alpha', ascending=False)
sort_2019 = BACI_2019.sort_values(by='alpha', ascending=False)
sort_2020 = BACI_2020.sort_values(by='alpha', ascending=False)

#%% plot top 10 alpha value products per year
from textwrap import wrap

#2010 plot
fig = plt.figure(figsize=(18,10))
x = sort_2010['prod_name'].head(10)
y = sort_2010['alpha'].head(10)
labels = [ '\n'.join(wrap(l, 20)) for l in x ]
plt.style.use('seaborn-whitegrid')
plt.plot(labels, y, 'o')
plt.savefig('./Plots/max_alpha/max_alpha2010.png', dpi=fig.dpi)

#2011 plot
fig = plt.figure(figsize=(18,10))
x = sort_2011['prod_name'].head(10)
y = sort_2011['alpha'].head(10)
labels = [ '\n'.join(wrap(l, 20)) for l in x ]
plt.style.use('seaborn-whitegrid')
plt.plot(labels, y, 'o')
plt.savefig('./Plots/max_alpha/max_alpha2011.png', dpi=fig.dpi)

#2012 plot
fig = plt.figure(figsize=(18,10))
x = sort_2012['prod_name'].head(10)
y = sort_2012['alpha'].head(10)
labels = [ '\n'.join(wrap(l, 20)) for l in x ]
plt.style.use('seaborn-whitegrid')
plt.plot(labels, y, 'o')
plt.savefig('./Plots/max_alpha/max_alpha2012.png', dpi=fig.dpi)

#2013 plot
fig = plt.figure(figsize=(18,10))
x = sort_2013['prod_name'].head(10)
y = sort_2013['alpha'].head(10)
labels = [ '\n'.join(wrap(l, 20)) for l in x ]
plt.style.use('seaborn-whitegrid')
plt.plot(labels, y, 'o')
plt.savefig('./Plots/max_alpha/max_alpha2013.png', dpi=fig.dpi)

#2014 plot
fig = plt.figure(figsize=(18,10))
x = sort_2014['prod_name'].head(10)
y = sort_2014['alpha'].head(10)
labels = [ '\n'.join(wrap(l, 20)) for l in x ]
plt.style.use('seaborn-whitegrid')
plt.plot(labels, y, 'o')
plt.savefig('./Plots/max_alpha/max_alpha2014.png', dpi=fig.dpi)

#2015 plot
fig = plt.figure(figsize=(18,10))
x = sort_2015['prod_name'].head(10)
y = sort_2015['alpha'].head(10)
labels = [ '\n'.join(wrap(l, 20)) for l in x ]
plt.style.use('seaborn-whitegrid')
plt.plot(labels, y, 'o')
plt.savefig('./Plots/max_alpha/max_alpha2015.png', dpi=fig.dpi)

#2016 plot
fig = plt.figure(figsize=(18,10))
x = sort_2016['prod_name'].head(10)
y = sort_2016['alpha'].head(10)
labels = [ '\n'.join(wrap(l, 20)) for l in x ]
plt.style.use('seaborn-whitegrid')
plt.plot(labels, y, 'o')
plt.savefig('./Plots/max_alpha/max_alpha2016.png', dpi=fig.dpi)

#2017 plot
fig = plt.figure(figsize=(18,10))
x = sort_2017['prod_name'].head(10)
y = sort_2017['alpha'].head(10)
labels = [ '\n'.join(wrap(l, 20)) for l in x ]
plt.style.use('seaborn-whitegrid')
plt.plot(labels, y, 'o')
plt.savefig('./Plots/max_alpha/max_alpha2017.png', dpi=fig.dpi)

#2018 plot
fig = plt.figure(figsize=(18,10))
x = sort_2018['prod_name'].head(10)
y = sort_2018['alpha'].head(10)
labels = [ '\n'.join(wrap(l, 20)) for l in x ]
plt.style.use('seaborn-whitegrid')
plt.plot(labels, y, 'o')
plt.savefig('./Plots/max_alpha/max_alpha2018.png', dpi=fig.dpi)

#2019 plot
fig = plt.figure(figsize=(18,10))
x = sort_2019['prod_name'].head(10)
y = sort_2019['alpha'].head(10)
labels = [ '\n'.join(wrap(l, 20)) for l in x ]
plt.style.use('seaborn-whitegrid')
plt.plot(labels, y, 'o')
plt.savefig('./Plots/max_alpha/max_alpha2019.png', dpi=fig.dpi)

#2020 plot
fig = plt.figure(figsize=(18,10))
x = sort_2020['prod_name'].head(10)
y = sort_2020['alpha'].head(10)
labels = [ '\n'.join(wrap(l, 20)) for l in x ]
plt.style.use('seaborn-whitegrid')
plt.plot(labels, y, 'o')
plt.savefig('./Plots/max_alpha/max_alpha2020.png', dpi=fig.dpi)

#%% Batteries overtime

battery_HS6 = [850650,854810,850690]

#create df
battery_df = BACI_2010[BACI_2010['product'].isin(battery_HS6)]

#append years
to_append = BACI_2011[BACI_2011['product'].isin(battery_HS6)]   #2011
battery_df = battery_df.append(to_append)
to_append = BACI_2012[BACI_2012['product'].isin(battery_HS6)]   #2012
battery_df = battery_df.append(to_append)
to_append = BACI_2013[BACI_2013['product'].isin(battery_HS6)]   #2013
battery_df = battery_df.append(to_append)
to_append = BACI_2014[BACI_2014['product'].isin(battery_HS6)]   #2014
battery_df = battery_df.append(to_append)
to_append = BACI_2015[BACI_2015['product'].isin(battery_HS6)]   #2015
battery_df = battery_df.append(to_append)
to_append = BACI_2016[BACI_2016['product'].isin(battery_HS6)]   #2016
battery_df = battery_df.append(to_append)
to_append = BACI_2017[BACI_2017['product'].isin(battery_HS6)]   #2017
battery_df = battery_df.append(to_append)
to_append = BACI_2018[BACI_2018['product'].isin(battery_HS6)]   #2018
battery_df = battery_df.append(to_append)
to_append = BACI_2019[BACI_2019['product'].isin(battery_HS6)]   #2019
battery_df = battery_df.append(to_append)
to_append = BACI_2020[BACI_2020['product'].isin(battery_HS6)]   #2020
battery_df = battery_df.append(to_append)

battery_df['Year'] = [2010,2010,2010,2011,2011,2011,2012,2012,2012,2013,2013,2013,2014,2014,2014,2015,2015,2015,
                      2016,2016,2016,2017,2017,2017,2018,2018,2018,2019,2019,2019,2020,2020,2020]
# battery_df = battery_df.iloc[: , 1:]

# Plot battery

#seperate by product
battery_850650 = battery_df[battery_df['product']==850650]
battery_854810 = battery_df[battery_df['product']==854810]
battery_850690 = battery_df[battery_df['product']==850690]

fig = plt.figure(figsize=(20,10))

# plotting the points
plt.plot(battery_850650['Year'], battery_850650['alpha'], label = "Cells and batteries: primary, lithium") 
plt.plot(battery_854810['Year'], battery_854810['alpha'], label = "Waste and scrap of primary cells, primary batteries and electric accumulators..") 
plt.plot(battery_850690['Year'], battery_850690['alpha'], label = 'Cells and batteries: primary, parts thereof')
         
plt.xlabel('year')
plt.ylabel('alpha')
plt.legend( loc='best')
plt.savefig('./Plots/products_overtime/batteries_overtime.png', dpi=fig.dpi)

#%% Electrical Accumulators overtime

accumulators_HS6 = [850710,850720,850730,850740,850780,850790]  #ONLY [850780, 850730] ARE PRESENT !!!!!

#create df
accumulators_df = BACI_2010[BACI_2010['product'].isin(accumulators_HS6)]

#append years
to_append = BACI_2011[BACI_2011['product'].isin(accumulators_HS6)]   #2011
accumulators_df = accumulators_df.append(to_append)
to_append = BACI_2012[BACI_2012['product'].isin(accumulators_HS6)]   #2012
accumulators_df = accumulators_df.append(to_append)
to_append = BACI_2013[BACI_2013['product'].isin(accumulators_HS6)]   #2013
accumulators_df = accumulators_df.append(to_append)
to_append = BACI_2014[BACI_2014['product'].isin(accumulators_HS6)]   #2014
accumulators_df = accumulators_df.append(to_append)
to_append = BACI_2015[BACI_2015['product'].isin(accumulators_HS6)]   #2015
accumulators_df = accumulators_df.append(to_append)
to_append = BACI_2016[BACI_2016['product'].isin(accumulators_HS6)]   #2016
accumulators_df = accumulators_df.append(to_append)
to_append = BACI_2017[BACI_2017['product'].isin(accumulators_HS6)]   #2017
accumulators_df = accumulators_df.append(to_append)
to_append = BACI_2018[BACI_2018['product'].isin(accumulators_HS6)]   #2018
accumulators_df = accumulators_df.append(to_append)
to_append = BACI_2019[BACI_2019['product'].isin(accumulators_HS6)]   #2019
accumulators_df = accumulators_df.append(to_append)
to_append = BACI_2020[BACI_2020['product'].isin(accumulators_HS6)]   #2020
accumulators_df = accumulators_df.append(to_append)

accumulators_df['Year'] = [2010,2010,2011,2011,2012,2012,2013,2013,2014,2014,2015,2015,2016,2016,2017,2017,
                           2018,2018,2019,2019,2020,2020]
# accumulators_df = accumulators_df.iloc[: , 1:]

# Plot accumulator

#seperate by product
accumulator_850780 = accumulators_df[accumulators_df['product']==850780]
accumulator_850730 = accumulators_df[accumulators_df['product']==850730]

fig = plt.figure(figsize=(20,10))

# plotting the points
plt.plot(accumulator_850780['Year'], accumulator_850780['alpha'], label = "Electric accumulators: n.e.c. in heading no. 8507, including separators, whether or not rectangular (including square)") 
plt.plot(accumulator_850730['Year'], accumulator_850730['alpha'], label = "Electric accumulators: nickel-cadmium, including separators, whether or not rectangular (including square)") 
  
plt.xlabel('year')
plt.ylabel('alpha')
plt.legend( loc='best')
plt.savefig('./Plots/products_overtime/accumulators_overtime.png', dpi=fig.dpi)

#%%

turbines_HS6 = [840681,840682,840690,841011,841012,841013,841090,841181,841182,841199]  #ONLY [840681, 840682, 840690. 841199]  ARE PRESENT !!!!!

#create df
turbines_df = BACI_2010[BACI_2010['product'].isin(turbines_HS6)]

#append years
to_append = BACI_2011[BACI_2011['product'].isin(turbines_HS6)]   #2011
turbines_df = turbines_df.append(to_append)
to_append = BACI_2012[BACI_2012['product'].isin(turbines_HS6)]   #2012
turbines_df = turbines_df.append(to_append)
to_append = BACI_2013[BACI_2013['product'].isin(turbines_HS6)]   #2013
turbines_df = turbines_df.append(to_append)
to_append = BACI_2014[BACI_2014['product'].isin(turbines_HS6)]   #2014
turbines_df = turbines_df.append(to_append)
to_append = BACI_2015[BACI_2015['product'].isin(turbines_HS6)]   #2015
turbines_df = turbines_df.append(to_append)
to_append = BACI_2016[BACI_2016['product'].isin(turbines_HS6)]   #2016
turbines_df = turbines_df.append(to_append)
to_append = BACI_2017[BACI_2017['product'].isin(turbines_HS6)]   #2017
turbines_df = turbines_df.append(to_append)
to_append = BACI_2018[BACI_2018['product'].isin(turbines_HS6)]   #2018
turbines_df = turbines_df.append(to_append)
to_append = BACI_2019[BACI_2019['product'].isin(turbines_HS6)]   #2019
turbines_df = turbines_df.append(to_append)
to_append = BACI_2020[BACI_2020['product'].isin(turbines_HS6)]   #2020
turbines_df = turbines_df.append(to_append)

turbines_df['Year'] = [2010,2010,2010,2010,2011,2011,2011,2011,2012,2012,2012,2012,2013,2013,2013,2013,
                       2014,2014,2014,2014,2015,2015,2015,2015,2016,2016,2016,2016,2017,2017,2017,2017,
                       2018,2018,2018,2018,2019,2019,2019,2019,2020,2020,2020,2020]
# turbines_df = battery_df.iloc[: , 1:]

# Plot turbines

#seperate by product
turbines_840681 = turbines_df[turbines_df['product']==840681]
turbines_840682 = turbines_df[turbines_df['product']==840682]
turbines_840690 = turbines_df[turbines_df['product']==840690]
turbines_841199 = turbines_df[turbines_df['product']==841199]

fig = plt.figure(figsize=(20,10))

# plotting the points
plt.plot(turbines_840681['Year'], turbines_840681['alpha'], label = "Turbines: steam and other vapour turbines, (for other than marine propulsion), of an output exceeding 40MW") 
plt.plot(turbines_840682['Year'], turbines_840682['alpha'], label = "Turbines: steam and other vapour turbines, (for other than marine propulsion), of an output not exceeding 40MW") 
plt.plot(turbines_840690['Year'], turbines_840690['alpha'], label = "Turbines: parts of steam and other vapour turbines") 
plt.plot(turbines_841199['Year'], turbines_841199['alpha'], label = "Turbines: parts of gas turbines (excluding turbo-jets and turbo-propellers)")   

plt.xlabel('year')
plt.ylabel('alpha')
plt.legend( loc='best')
plt.savefig('./Plots/products_overtime/turbines_overtime.png', dpi=fig.dpi)

#%%
EV_HS6=870911
lithium ion batteries = 850760
