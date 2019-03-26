from pandas_datareader import wb
import numpy as np
origin_refugee=wb.download(indicator='SM.POP.REFG.OR', start=1990, end=2017)
origin_refugee = origin_refugee.reset_index()
origin_refugee = origin_refugee.rename(columns = {'country':'Country', 'year':'Year', 'SM.POP.REFG.ORG':'Country of Origin'})
origin_refugee.head(50)
origin_refugee.info()