# Dataproject

A graphical analysis of the relationship between unemployment and number of refugees within different countries. 

## Getting Started

Download the entire folder "Dataproject" to get started. 
The extension **"ipywidgets"** used to make an interactive graph with a drop down menu, does not work in all environments. Therefore, we recommend you run the code with **Jupyter**. 


### Installing

All the extensions you need to install are already included in the code, just run the entire code, and you will not need any other installations. 


## Deployment

Works best if runned in Jupyter, as the extension "ipywidgets" does not work in all environments.

Execute the code for all new sections. The start of a section is indicated by a dropdown and a comment. 
E.g.
/# Download data on refugee population in a country from the World Bank database
refugeesin_wb = wb.download(indicator='SM.POP.REFG', country = 'all', start=1990, end=2017)
refugeesin_wb = refugeesin_wb.reset_index()

RUN ABOVE SECTION CODE 
AND PLUG IN NEXT SECTION AFTERWARDS

/# Clean data (deleting regions, keeping countries)
refugeesin_wb.loc[refugeesin_wb.country == 'Afghanistan']
refugeesin_wb = refugeesin_wb.iloc[1316:,]
refugeesin_wb = refugeesin_wb.reset_index()
refugeesin_wb = refugeesin_wb.drop('index', axis = 1)

RUN ABOVE SECTION CODE 
AND PLUG IN NEXT SECTION AFTERWARDS

/# Check unique countries to compare with other data set, rename columns
len(refugeesin_wb.country.unique())
refugeesin_wb = refugeesin_wb.rename(columns = {'country':'Country','year':'Year','SM.POP.REFG':'Refugee population in country'})
refugeesin_wb.head(3)


## Sources
Worldbank: https://data.worldbank.org/
The UN Refugee Agency: http://popstats.unhcr.org

## Authors

**Anna Falk Jensen, Bella Vinzents & Sarah Schannong **

