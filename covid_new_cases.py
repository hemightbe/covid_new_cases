#!/usr/bin/env python
# coding: utf-8

# In[32]:


from IPython.core.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))

import pandas as pd
import numpy as np

import plotly.graph_objs as go

from plotly.subplots import make_subplots


# In[33]:


# read owid-covid-data.csv into dataframe
df_all_world = pd.read_csv('owid-covid-data.csv', sep=',')

# replace spaces with _ in column names
df_all_world.columns = [c.lower().replace(' ', '_') for c in df_all_world.columns]


# In[34]:


usFilter = ['United States']

# list of countries with socilaized medicine 
socialFilter = ['Australia','Austria','Bahrain','Belgium','Brunei','Canada','Cyprus','Denmark','Finland','France','Germany','Greece','Hong Kong','Iceland','Ireland','Israel','Italy','Japan','Kuwait','Luxembourg','Netherlands','New Zealand','Norway','Portugal','Singapore','Slovenia','South Korea','Spain','Sweden','Switzerland','the United Arab Emirates','United Kingdom']

# convert time columns to datetime
df_all_world['start_week'] = pd.to_datetime(df_all_world.date)

# filter date
df_all_world = df_all_world[(df_all_world['start_week'] >= '2020-04-01')]

#select only require columns
df_all_world = df_all_world[['location','date','total_cases','new_cases','total_deaths','total_cases_per_million','new_cases_per_million','cvd_death_rate']]

# create dataframe for United States data
df_us = df_all_world[df_all_world['location'].isin(usFilter)]

# create dataframe for socialized medicine countries
df_all_world = df_all_world[df_all_world['location'].isin(socialFilter)]


# In[28]:


# create dataframe with columns grouped and summed for social medicine countries
df_all_world_sum = df_all_world.groupby(['date'], as_index=False, sort=True).sum().sort_values(['date'], ascending=False)

# create dataframe with columns grouped and summed for United States
df_us_sum = df_us.groupby(['date','total_cases','new_cases','total_deaths'], as_index=False, sort=True).sum().sort_values(['date'], ascending=False)


# In[29]:


# merge summed dataframes into a new one 
df_cd = pd.merge(df_us_sum, df_all_world_sum, how='inner', on='date')


# In[30]:


# ensure datetime format in date column
df_cd['date'] = pd.to_datetime(df_cd['date'])

fig = go.Figure()
fig = make_subplots(specs=[[{"secondary_y": True}]])

# add line / trace 1 to figure
fig.add_trace(go.Scatter(
    x=df_cd['date'],
    y=df_cd['new_cases_x'],
    hovertext=df_cd['new_cases_x'],
    hoverinfo="text",
    name="New Cases US",
    marker=dict(
        color="blue"
    ),
    showlegend=True
),
    secondary_y=False,
)

# add line / trace 2 to figure
fig.add_trace(go.Scatter(
    x=df_cd['date'],
    y=df_cd['new_cases_y'],
    hovertext=df_cd['new_cases_y'],
    hoverinfo="text",
    name="New Cases in Countries w/ Socialized Medicine",
    marker=dict(
        color="green"
    ),
    showlegend=True
),
secondary_y=False,          
)

# Set x-axis title
fig.update_xaxes(title_text="@date")

# Set y-axes titles
fig.update_yaxes(title_text="New Cases US", secondary_y=False)
fig.update_yaxes(title_text="New Cases of COVID-19", secondary_y=False)

fig.update_layout(
    autosize=False,
    width=1500,  # adjust these to scale graph size
    height=700
)

fig.show('notebook')


# In[31]:


df_cd['date'] = pd.to_datetime(df_cd['date'])

fig = go.Figure()
fig = make_subplots(specs=[[{"secondary_y": True}]])

# add line / trace 1 to figure
fig.add_trace(go.Scatter(
    x=df_cd['date'],
    y=df_cd['new_cases_x'],
    hovertext=df_cd['new_cases_x'],
    hoverinfo="text",
    name="New Cases US",
    marker=dict(
        color="blue"
    ),
    showlegend=True
),
    secondary_y=False,
)

# add line / trace 2 to figure
fig.add_trace(go.Scatter(
    x=df_cd['date'],
    y=df_cd['new_cases_y'],
    hovertext=df_cd['new_cases_y'],
    hoverinfo="text",
    name="New Cases in Countries w/ Socialized Medicine",
    marker=dict(
        color="green"
    ),
    showlegend=True
),
secondary_y=True,          
)

# Set x-axis title
fig.update_xaxes(title_text="@date")

# Set y-axes titles
fig.update_yaxes(title_text="New Cases US", secondary_y=False)
fig.update_yaxes(title_text="New Cases in Countries w/ Socialized Medicine", secondary_y=True)

fig.update_layout(
    autosize=False,
    width=3000,  # adjust these to scale graph size
    height=1700
)

fig.show('notebook')
