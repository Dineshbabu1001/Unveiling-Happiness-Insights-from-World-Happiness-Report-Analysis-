#!/usr/bin/env python
# coding: utf-8

# # Data Preparation and Exploration

# Importing Libraries

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objs as go


# Loading the Dataset

# In[2]:


df=pd.read_csv('WHR.csv')


# Sampling the Data

# In[3]:


df.sample(10)


# Checking for Missing Values

# In[4]:


df.isnull().sum()


# Unique Country Names

# In[5]:


df["Country name"].unique()


# Unique Regional Indicators

# In[6]:


df["Regional indicator"].unique()


# # Data Visualization and Analysis

# Missing Values Heatmap

# In[7]:


sns.heatmap(df.isna())


# Correlation Heatmap

# In[8]:


sns.heatmap(df.corr(),annot=True)


# Data Overview

# In[9]:


df.info()


# Descriptive Statistics

# In[10]:


df.describe()


# Descriptive Statistics for Categorical Features

# In[11]:


df.describe(include=object)


# # Exploring Happiness Factors

# Scatter Plot: Ladder Score vs. Logged GDP per Capita

# In[12]:


fig=go.Figure(data=go.Scatter(
    x=df['Logged GDP per capita'],
    y=df['Ladder score'],
    mode='markers',
    text=df['Country name'],
    marker=dict(
        size=10,
        color=df['Ladder score'],
        colorscale='viridis',
        showscale=True
    )
))


# In[13]:


fig.update_layout(
    title="Ladder Score VS Logged GDP per Capita",
    xaxis=dict(title="Logged GDP per capita"),
    yaxis=dict(title="Ladder score")
)


# Scatter Plot: Country vs. Social Support

# In[15]:


fig_1=go.Figure(data=go.Scatter(
    x=df['Country name'],
    y=df['Social support']

))


# In[16]:


fig_1.update_layout(
    title="Country VS Social Support",
    xaxis=dict(title="Country name"),
    yaxis=dict(title="Social support")
)


# Top 10 Countries: Bar plot showcasing the countries with the highest ladder scores

# In[17]:


top_10=df.nlargest(10,'Ladder score')


# In[18]:


bar_plot=px.bar(top_10,x='Country name',y='Ladder score')
bar_plot.show()


# Bottom 10 Countries: Bar plot showcasing the countries with the lowest ladder scores

# In[19]:


small_10=df.nsmallest(10,'Ladder score')


# In[20]:


bar_plot=px.bar(small_10,x='Country name',y='Ladder score')
bar_plot.show()


# Regional Analysis: Bar plots comparing ladder scores across regional indicators

# In[21]:


bar_plot=px.bar(top_10,x='Regional indicator',y='Ladder score')
bar_plot.show()


# In[22]:


bar_plot=px.bar(small_10,x='Regional indicator',y='Ladder score')
bar_plot.show()


# Perceptions of Corruption: Bar plot showcasing countries with high and low perceptions of corruption

# In[23]:


fig_2=go.Figure(data=go.Bar(
    x=df['Country name'],
    y=df['Perceptions of corruption']

))


# In[36]:


fig_2.update_layout(
    title="Country VS Perceptions of corruption",
    xaxis=dict(title="Country name"),
    yaxis=dict(title="Perceptions of corruption")
)


# In[24]:


top_10=df.nlargest(10,'Perceptions of corruption')
bar_plot=px.bar(top_10,x='Country name',y='Perceptions of corruption')
bar_plot.show()


# In[25]:


smal_10=df.nsmallest(10,'Perceptions of corruption')
bar_plot=px.bar(smal_10,x='Country name',y='Perceptions of corruption')
bar_plot.show()


# Freedom to Make Life Choices: Bar plot comparing countries based on freedom to make life choices

# In[26]:


fig_3=go.Figure(data=go.Bar(
    x=df['Country name'],
    y=df['Freedom to make life choices']

))


# In[27]:


fig_3.update_layout(
    title="Country VS Freedom to make life choices",
    xaxis=dict(title="Country name"),
    yaxis=dict(title="Freedom to make life choices")
)


# In[28]:


tp_10=df.nlargest(10,'Freedom to make life choices')
bar_plot=px.bar(tp_10,x='Country name',y='Freedom to make life choices')
bar_plot.show()


# In[29]:


smll_10=df.nsmallest(10,'Freedom to make life choices')
bar_plot=px.bar(smll_10,x='Country name',y='Freedom to make life choices')
bar_plot.show()


# Ladder Score in Dystopia: Bar plots showcasing ladder scores in dystopia for top and bottom countries

# In[30]:


fig_4=go.Figure(data=go.Bar(
    x=df['Country name'],
    y=df['Ladder score in Dystopia']

))


# In[31]:


fig_4.update_layout(
    title="Country VS Ladder score in Dystopia",
    xaxis=dict(title="Country name"),
    yaxis=dict(title="Ladder score in Dystopia")
)


# In[32]:


t_10=df.nlargest(10,'Freedom to make life choices')
bar_plot=px.bar(t_10,x='Country name',y='Ladder score in Dystopia')
bar_plot.show()


# In[33]:


s_10=df.nsmallest(10,'Freedom to make life choices')
bar_plot=px.bar(s_10,x='Country name',y='Ladder score in Dystopia')
bar_plot.show()


# # Global Happiness Map

# Choropleth Map: Visualizing the ladder scores across countries using a choropleth map

# In[34]:


fig_5 = px.choropleth(df, 
                    locations='Country name', 
                    color='Ladder score',
                    locationmode='country names',
                    color_continuous_scale='Blues')


# In[35]:


fig_5.update_layout(title='Choropleth Map of Ladder Score',
                  geo=dict(showframe=False,
                           showcoastlines=False,
                           projection_type='equirectangular'))
fig_5.show()


# # Conclusion

# The analysis of the World Happiness Report dataset provided insights into global happiness and well-being. Finland emerged as the happiest country, showcasing the importance of social support, low corruption, and freedom. The findings highlight the significance of creating supportive environments that prioritize social well-being, economic stability, and personal freedom. Policymakers, organizations, and individuals can leverage these insights to promote happiness and enhance overall quality of life. Further exploration of the dataset can contribute to a deeper understanding of the complex factors influencing happiness worldwide.
