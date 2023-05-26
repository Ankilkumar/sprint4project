import streamlit as st
import pandas as pd
import plotly_express as px

df_data = pd.read_csv('Real_Estate_Sales_2001_2020.csv')

st.header('Real estate sales data of residential properties in Connecticut (2001 - 2020)')

#only interested in residential properties
df_data = df_data[df_data['Property Type'] != 'Commercial']
df_data = df_data[['List Year', 'Date Recorded', 'Assessed Value', 'Town', 'Sale Amount', 'Residential Type', 'Property Type']]

#removing all null data because we cannot determine what type of properties they were
df_data = df_data.dropna()
df_data = df_data.rename(columns={
                 'List Year': 'list_year',
                 'Date Recorded': 'date_recorded',
                 'Assessed Value': 'assessed_value',
                 'Town': 'town',
                 'Sale Amount': 'sale_amount',
                 'Residential Type': 'residential_type',
                 'Property Type': 'property_type'
                 })
df_data['date_recorded'] = pd.to_datetime(df_data['date_recorded'], format = "%m/%d/%Y")

st.dataframe(df_data)

st.header('Amount of different types of residential properties sold by year')
graph = px.histogram(df_data, x = 'list_year', color = 'residential_type')
st.write(graph)

df_data['year'] = df_data['date_recorded'].dt.year
df_data['month'] = df_data['date_recorded'].dt.month

st.header('Average price of properties sold per month each year')

low_value_sales = st.checkbox('Average sale amount below 500,000 USD', value = False)

if low_value_sales:
    df1_low_value = df_data[df_data['sale_amount'] < 500000]
else:
    df1_low_value = df_data

df1_low_value = df1_low_value.groupby(['year', 'month'], as_index=False).mean()
df1_low_value['monthly'] = pd.to_datetime(df1_low_value[['year', 'month']].assign(DAY = 1))

fig = px.scatter(df1_low_value, x = 'monthly', y = 'sale_amount')