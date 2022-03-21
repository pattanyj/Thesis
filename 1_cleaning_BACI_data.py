# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 16:06:28 2022

@author: patta
"""
import pandas as pd

#%% HS07 DATA

#import files
BACI_2010 = pd.read_csv("./BACI_HS07/BACI_HS07_Y2010_V202201.csv")
BACI_2011 = pd.read_csv("./BACI_HS07/BACI_HS07_Y2011_V202201.csv")
BACI_2012 = pd.read_csv("./BACI_HS07/BACI_HS07_Y2012_V202201.csv")
BACI_2013 = pd.read_csv("./BACI_HS07/BACI_HS07_Y2013_V202201.csv")
BACI_2014 = pd.read_csv("./BACI_HS07/BACI_HS07_Y2014_V202201.csv")
BACI_2015 = pd.read_csv("./BACI_HS07/BACI_HS07_Y2015_V202201.csv")
BACI_2016 = pd.read_csv("./BACI_HS07/BACI_HS07_Y2016_V202201.csv")
BACI_2017 = pd.read_csv("./BACI_HS07/BACI_HS07_Y2017_V202201.csv")
BACI_2018 = pd.read_csv("./BACI_HS07/BACI_HS07_Y2018_V202201.csv")
BACI_2019 = pd.read_csv("./BACI_HS07/BACI_HS07_Y2019_V202201.csv")
BACI_2020 = pd.read_csv("./BACI_HS07/BACI_HS07_Y2020_V202201.csv")

#remove NA
BACI_2010_clean = BACI_2010[BACI_2010['q'].str.contains('NA')==False]
BACI_2011_clean = BACI_2011[BACI_2011['q'].str.contains('NA')==False]
BACI_2012_clean = BACI_2012[BACI_2012['q'].str.contains('NA')==False]
BACI_2013_clean = BACI_2013[BACI_2013['q'].str.contains('NA')==False]
BACI_2014_clean = BACI_2014[BACI_2014['q'].str.contains('NA')==False]
BACI_2015_clean = BACI_2015[BACI_2015['q'].str.contains('NA')==False]
BACI_2016_clean = BACI_2016[BACI_2016['q'].str.contains('NA')==False]
BACI_2017_clean = BACI_2017[BACI_2017['q'].str.contains('NA')==False]
BACI_2018_clean = BACI_2018[BACI_2018['q'].str.contains('NA')==False]
BACI_2019_clean = BACI_2019[BACI_2019['q'].str.contains('NA')==False]
BACI_2020_clean = BACI_2020[BACI_2020['q'].str.contains('NA')==False]

#save files
BACI_2010_clean.to_csv('./clean_BACI/HS07/clean_BACI_HS07_Y2010_V202201.csv')
BACI_2011_clean.to_csv('./clean_BACI/HS07/clean_BACI_HS07_Y2011_V202201.csv')
BACI_2012_clean.to_csv('./clean_BACI/HS07/clean_BACI_HS07_Y2012_V202201.csv')
BACI_2013_clean.to_csv('./clean_BACI/HS07/clean_BACI_HS07_Y2013_V202201.csv')
BACI_2014_clean.to_csv('./clean_BACI/HS07/clean_BACI_HS07_Y2014_V202201.csv')
BACI_2015_clean.to_csv('./clean_BACI/HS07/clean_BACI_HS07_Y2015_V202201.csv')
BACI_2016_clean.to_csv('./clean_BACI/HS07/clean_BACI_HS07_Y2016_V202201.csv')
BACI_2017_clean.to_csv('./clean_BACI/HS07/clean_BACI_HS07_Y2017_V202201.csv')
BACI_2018_clean.to_csv('./clean_BACI/HS07/clean_BACI_HS07_Y2018_V202201.csv')
BACI_2020_clean.to_csv('./clean_BACI/HS07/clean_BACI_HS07_Y2020_V202201.csv')

#%% HS12 DATA

#import files
BACI_2012 = pd.read_csv("./BACI_HS12/BACI_HS12_Y2012_V202201.csv")
BACI_2013 = pd.read_csv("./BACI_HS12/BACI_HS12_Y2013_V202201.csv")
BACI_2014 = pd.read_csv("./BACI_HS12/BACI_HS12_Y2014_V202201.csv")
BACI_2015 = pd.read_csv("./BACI_HS12/BACI_HS12_Y2015_V202201.csv")
BACI_2016 = pd.read_csv("./BACI_HS12/BACI_HS12_Y2016_V202201.csv")
BACI_2017 = pd.read_csv("./BACI_HS12/BACI_HS12_Y2017_V202201.csv")
BACI_2018 = pd.read_csv("./BACI_HS12/BACI_HS12_Y2018_V202201.csv")
BACI_2019 = pd.read_csv("./BACI_HS12/BACI_HS12_Y2019_V202201.csv")
BACI_2020 = pd.read_csv("./BACI_HS12/BACI_HS12_Y2020_V202201.csv")

#remove NA
BACI_2012_clean = BACI_2012[BACI_2012['q'].str.contains('NA')==False]
BACI_2013_clean = BACI_2013[BACI_2013['q'].str.contains('NA')==False]
BACI_2014_clean = BACI_2014[BACI_2014['q'].str.contains('NA')==False]
BACI_2015_clean = BACI_2015[BACI_2015['q'].str.contains('NA')==False]
BACI_2016_clean = BACI_2016[BACI_2016['q'].str.contains('NA')==False]
BACI_2017_clean = BACI_2017[BACI_2017['q'].str.contains('NA')==False]
BACI_2018_clean = BACI_2018[BACI_2018['q'].str.contains('NA')==False]
BACI_2019_clean = BACI_2019[BACI_2019['q'].str.contains('NA')==False]
BACI_2020_clean = BACI_2020[BACI_2020['q'].str.contains('NA')==False]

#save files
BACI_2012_clean.to_csv('./clean_BACI/HS12/clean_BACI_HS12_Y2012_V202201.csv')
BACI_2013_clean.to_csv('./clean_BACI/HS12/clean_BACI_HS12_Y2013_V202201.csv')
BACI_2014_clean.to_csv('./clean_BACI/HS12/clean_BACI_HS12_Y2014_V202201.csv')
BACI_2015_clean.to_csv('./clean_BACI/HS12/clean_BACI_HS12_Y2015_V202201.csv')
BACI_2016_clean.to_csv('./clean_BACI/HS12/clean_BACI_HS12_Y2016_V202201.csv')
BACI_2017_clean.to_csv('./clean_BACI/HS12/clean_BACI_HS12_Y2017_V202201.csv')
BACI_2018_clean.to_csv('./clean_BACI/HS12/clean_BACI_HS12_Y2018_V202201.csv')
BACI_2019_clean.to_csv('./clean_BACI/HS12/clean_BACI_HS12_Y2019_V202201.csv')
BACI_2020_clean.to_csv('./clean_BACI/HS12/clean_BACI_HS12_Y2020_V202201.csv')