# Section 9 - Data Analysis with Pandas
# 71 - Pandas Introduction
# 72 - Note on IPython
# 73 - Getting Started with Pandas
# 74 - Getting Started with Jupyter Notebooks
# it is a interactive shell where we can also save scripts and having multiple
# blocks for testing differente snippets of code
# It is good for working with Data
# You can open a notebook in a specific folder by running jupyter notebook command
# usinf the cmd terminal from that folder
# content in the notebook
# to sum it up:

import pandas as pd
import os
os.listdir()

df1 = pd.read_csv('supermarkets.csv')
# set the index as the column called 'ID'
df1.set_index('ID')

df2=pd.read_json('supermarkets.json')

df5=pd.read_csv('supermarkets-semi-colons.txt', sep=';')
print(df5)
# you can read data directly from URLs if the URL points to a file
# just input the URL directly as an input to the read_csv method and the dataframe will be loaded

# indexing of dataframes
# how to slice data from a dataframe
# label base indexing or position base indexing are the two ways of accessing specific portions of
# information in a dataframe
# you have column lables and index labels
# the comand set_index returns a new dataframe with a new label for the index
df_ch = df5.set_index('Address')
# but we can change to True the inplace parameter for altering the object df5 directly.
df_ch.loc['735 Dolores St':'1056 Sanchez St', 'Country':'Name']

# normally we would use indexes to refer to rows, and labels to refer to columns
# we can access elements with indexes that with the iloc method
df_ch.iloc[1:3,1:3]
# note that the slicing ins upper bound exclusive

# another way is to use index for rows and labels for columns
df_ch.iloc[:4,:].loc[:,'Employees']

# how to delete columns and rows
# use the drop method
# it is an inplace operation, so you have to pass the result to a variable
# 0 for rows and 1 for columns
df_ch.drop('Country', 1)
# we can use indexing:
df_ch.drop(df_ch.index[0:3],0)
df_ch.drop(df_ch.columns[0:3],1)

# how to add columns and rows to a dataframe
# the number of rows must match the length of the rows in the dataframe
df_ch['Continent']=df_ch.shape[0]*["North America"]
# to add new rows is not so easy, we have to pass the transposed version of the df to a new temp variable
df_ch_temp = df_ch.T
df_ch_temp['My Address']=[7, 'My City', 'My State', 'My Country', ' My Name', 5, 'My Continent']
df_ch=df_ch_temp.T

# to close the pandas tutorial we will do an interesting example
# The goal is to convert each address in the dafaframe to its corresponding geographical
# location, in latitude and longitude
# This process is called GeoCoding
# We will add the Latitude and Longitude columns
# but we will need a external package called geopy
import geopy
dir(geopy)

from geopy.geocoders import Nominatim

nom=Nominatim()
location=nom.geocode('Rua Sebastião Antônio Carlos, 260, Belo Horizonte, Minas Gerais, Brasil')
location
# 0.o, uau!! haha
# sometimes iit miight pass a  None object, because it was not able to find the specified address

print(location.latitude, location.longitude)

df = pd.read_csv('supermarkets.csv')
# update the address column to have the string addres representation accepted by the geocoder
df['Address']=df['Address']+', '+df['City']+', '+df['State']+', '+df['Country']

# pandas makes it easy to apply functions and methods to the dataframe, without havint to
# iterate through columns and rows
df['Coordinates Location']=df['Address'].apply(nom.geocode)

df['Latitude']=df['Coordinates Location'].apply(lambda x: x.latitude if x != None else None)
df['Longitude']=df['Coordinates Location'].apply(lambda x: x.longitude if x != None else None)
print(df)
