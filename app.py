import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np
df = pd.read_csv('vehicles_us.csv')
st.header('Vehicule types by manufacturer')
st.write('we will provide you with the dataset on car sales advertisements')

# Extract the manufacturer from the model and store it in a new column
df["manufacturer"] = df["model"].str.split(" ", n = 1, expand = True)[0]

manufacturer_choice=df['manufacturer'].unique()
selected_manufacturer = st.selectbox('Select manufacturer:', manufacturer_choice)

min_year,max_year=int(df['model_year'].min()),int(df['model_year'].max())
year_range = st.slider(
     "Choose years",
     value=(min_year,max_year),min_value=min_year,max_value=max_year )

actual_range=list(range(year_range[0],year_range[1]+1))

#st.slider("choose years",value=(min_year,max_year),min_value=min_year,max_value=max_year )

filtered_type=df[(df.manufacturer==selected_manufacturer)&(df.model_year.isin(list(actual_range)))]

st.table(filtered_type)


#df = pd.read_csv('vehicles_us.csv')
df['manufacturer'] = df['manufacturer'].apply(lambda x: x.split()[0])

fig = px.histogram(df, x= 'manufacturer', color='type')
st.write(fig)

st.header('Histogram of `condition` vs `model_year`')
fig = px.histogram(df, x='model_year', color='condition')
st.write(fig)


st.header('Compare price distribution between manufacturers')
# get a list of car manufacturers
manufac_list = sorted(df['manufacturer'].unique())
# get user's inputs from a dropdown menu
manufacturer_1 = st.selectbox(
                              label='Select manufacturer 1', # title of the select box
                              options=manufac_list, # options listed in the select box
                              index=manufac_list.index('chevrolet') # default pre-selected option
                              )
# repeat for the second dropdown menu
manufacturer_2 = st.selectbox(
                              label='Select manufacturer 2',
                              options=manufac_list, 
                              index=manufac_list.index('hyundai')
                              )
# filter the dataframe 
mask_filter = (df['manufacturer'] == manufacturer_1) | (df['manufacturer'] == manufacturer_2)
df_filtered = df[mask_filter]

# add a checkbox if a user wants to normalize the histogram
normalize = st.checkbox('Normalize histogram', value=True)
if normalize:
    histnorm = 'percent'
else:
    histnorm = None

# create a plotly histogram figure
fig = px.histogram(df_filtered,
                      x='price',
                      nbins=30,
                      color='manufacturer',
                      histnorm=histnorm,
                      barmode='overlay')
# display the figure with streamlit
st.write(fig)