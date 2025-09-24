



# b) Use streamlit and create an interactive web graph where you can select the countries to be included in the population plot
#first read data
import pandas as pd
df_visu = pd.read_csv('https://raw.githubusercontent.com/LauriHermas/streamlit_pop_2025/refs/heads/main/population_country_columns.csv')

import streamlit as st
st.title('Population plot')
#select teh columns we wish to plot
columns = st.multiselect('Countries', (df_visu.drop(columns = ['year'])).columns, key = 'line_selector')


#plot the line chart
st.line_chart(df_visu, x = 'year', y = columns, y_label = 'Population', x_label= 'Year')


#Extra task:
#stacked bar plot with streamlit and matplotlib
#streamlit can handle matplotlib and plotly graphics

columns = st.multiselect('Countries', (df_visu.drop(columns = ['year'])), key = 'bar_selector')
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize = (10,6))

for country_name in columns:
     plt.bar(df_visu['year'],df_visu[country_name]/1000000, bottom = bottom_line, width = 4,label = country_name) # dont define the color    
     bottom_line = bottom_line + (df_visu[country_name].values)/1000000
plt.title('Population of Nordics')
plt.ylabel('Population [millions]')
plt.xlabel('Year')
plt.legend()
plt.grid()
st.pyplot(fig)




