#!/usr/bin/env python
# coding: utf-8

# In[2]:

from IPython.core.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))

import pandas as pd
import numpy as np

import plotly.graph_objs as go
from plotly.subplots import make_subplots


# In[3]:


df_all_world = pd.read_csv('owid-covid-data.csv', sep=',')
df_all_world.columns = [c.lower().replace(' ', '_') for c in df_all_world.columns]


# In[4]:


dropdownLocationVals = ['United States']
dropdownOtherVals = ['Australia','Austria','Bahrain','Belgium','Brunei','Canada','Cyprus','Denmark','Finland','France','Germany','Greece','Hong Kong','Iceland','Ireland','Israel','Italy','Japan','Kuwait','Luxembourg','Netherlands','New Zealand','Norway','Portugal','Singapore','Slovenia','South Korea','Spain','Sweden','Switzerland','the United Arab Emirates','United Kingdom']

df_all_world['start_week'] = pd.to_datetime(df_all_world.date)
df_all_world = df_all_world[(df_all_world['start_week'] >= '2020-04-01')]
df_all_world = df_all_world[['location','date','total_cases','new_cases','total_deaths','total_cases_per_million','new_cases_per_million','cvd_death_rate']]

df_us = df_all_world[df_all_world['location'].isin(dropdownLocationVals)]
df_all_world = df_all_world[df_all_world['location'].isin(dropdownOtherVals)]


# In[5]:


df_all_world_sum = df_all_world.groupby(['date'], as_index=False, sort=True).sum().sort_values(['date'], ascending=False)
df_us_sum = df_us.groupby(['date','total_cases','new_cases','total_deaths'], as_index=False, sort=True).sum().sort_values(['date'], ascending=False)


# In[6]:


df_cd = pd.merge(df_us_sum, df_all_world_sum, how='inner', on='date')


# In[7]:


df_cd['date'] = pd.to_datetime(df_cd['date'])

fig = go.Figure()
fig = make_subplots(specs=[[{"secondary_y": True}]])

#add line / trace 1 to figure
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

#add line / trace 2 to figure
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
    width=1500,
    height=700
)

fig.show('notebook')


# In[8]:


df_cd['date'] = pd.to_datetime(df_cd['date'])

fig = go.Figure()
fig = make_subplots(specs=[[{"secondary_y": True}]])

#add line / trace 1 to figure
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

#add line / trace 2 to figure
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
    width=1500,
    height=700
)

fig.show('notebook')
