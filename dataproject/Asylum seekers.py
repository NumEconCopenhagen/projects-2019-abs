#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'dataproject'))
	print(os.getcwd())
except:
	pass

#%%
import pandas as pd


#%%
import os 
os.listdir('./dataproject/')


#%%
filename = "./dataproject/Refugees.csv"


#%%
pd.read_csv("./dataproject/Refugees.csv", low_memory=False, skipinitialspace=True).head(10)


#%%
#Remove whitespaces and first 3 rows
refug = pd.read_csv("./dataproject/Refugees.csv", low_memory=False, skiprows = 3, skipinitialspace=True)


#%%
refug.head(10)


#%%
refug.rename(columns = {'Country / territory of asylum/residence' : 'End_Country', 'Value' : 'Asylum_seekers'}, inplace=True)


#%%
refug.dtypes


#%%
#Remove all non-numeric values from "Value" column
refug['Asylum_seekers'] = pd.to_numeric(refug['Asylum_seekers'], errors='coerce')
#Drop all rows with Null values 
refug = refug.dropna(subset=['Asylum_seekers'])
#Convert "Value" varible to integer
refug['Asylum_seekers'] = refug['Asylum_seekers'].astype(int)
refug['Year'] = refug['Year'].astype(int)
refug.head(10)


#%%
refug.dtypes


#%%
import ipywidgets as widgets
import matplotlib.ticker as ticker
#Graph depicting number of refugees over years by orgin
def plot_Asylum_seekers(dataframe, Origin): 
    I = dataframe['Origin'] == Origin
    
    ax=dataframe.loc[I,:].groupby(['Year'])['Asylum_seekers'].sum().plot(x='Year', y='Value', style='-o', legend='False') #Aggregate on yearly level to get total refugees per year. 
    ax.xaxis.set_major_formatter(ticker.FormatStrFormatter("%d"))
    ax.get_yaxis().get_major_formatter().set_scientific(False)
    ax.set_title("Total number of Asylum Seekers by Origin Country")
    ax.set_ylabel("Number of Asylum Seekers")


#%%
widgets.interact(plot_Asylum_seekers, 
dataframe = widgets.fixed(refug),
Origin = widgets.Dropdown(description='Origin', options=refug.Origin.unique(), value='Afghanistan')
)


#%%
#Graph depicting number of refugees over years by End_Country
def plot_Asylum_seekersEND(dataframe, End_Country): 
    L = dataframe['End_Country'] == End_Country
    
    ax2=dataframe.loc[L,:].groupby(['Year'])['Asylum_seekers'].sum().plot(x='Year', y='Asylum_seekers', style='-o', legend='False') #Aggregate on yearly level to get total refugees per year. 
    ax2.get_yaxis().get_major_formatter().set_scientific(False)
    ax2.xaxis.set_major_formatter(ticker.FormatStrFormatter("%d"))
    ax2.set_title("Total number of Asylum Seekers by End Country")
    ax2.set_ylabel("Number of Asylum Seekers")


#%%
widgets.interact(plot_Asylum_seekersEND, 
  dataframe = widgets.fixed(refug),
  End_Country = widgets.Dropdown(description='End_Country', options=refug.End_Country.unique(), value='Australia')
)


