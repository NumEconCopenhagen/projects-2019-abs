from pandas_datareader import wb
import numpy as np
#Download data
origin_refugee=wb.download(indicator='SM.POP.REFG.OR', country='all', start=1990, end=2017)
origin_refugee = origin_refugee.reset_index()
#Locate first country
origin_refugee.loc[origin_refugee.country == 'Afghanistan']
len(origin_refugee.country.unique())
origin_refugee = origin_refugee.reset_index()
origin_refugee = origin_refugee.rename(columns = {'country':'Country', 'year':'Year', 'SM.POP.REFG.OR':'Country of Origin'})
origin_refugee.head(30)
#Drop all observations prior to Afghanistan
origin_refugee = origin_refugee.iloc[1316:,]
origin_refugee.head(10)