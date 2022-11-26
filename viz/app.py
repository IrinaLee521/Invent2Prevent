import pandas as pd
import geojson
import numpy as np
import requests
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import dash
from dash import dcc #dcc to embed graphs in the dashboard
import dash_bootstrap_components as dbc
from dash import html # html to set up the layout
from dash.dependencies import Input, Output


# Read CSV files into Pandas data frames
victims = pd.read_csv("../data/victims.csv")
incidents = pd.read_csv("../data/incidents.csv")
offenders = pd.read_csv("../data/offenders.csv")
offenses = pd.read_csv("../data/offenses.csv")
comparison = pd.read_csv("../data/comparison.csv")
comparison2 = pd.read_csv("../data/comparison2.csv")
disability = pd.read_csv("../data//disability.csv", dtype={'VICTIM_COUNT': 'int', 'STATE_ABBR': 'str'})
physical = pd.read_csv("../data/physical.csv", dtype={'VICTIM_COUNT': 'int', 'STATE_ABBR': 'str'})
mental = pd.read_csv("../data/mental.csv", dtype={'VICTIM_COUNT': 'int', 'STATE_ABBR': 'str'})

with open("../data/us-state-boundaries.geojson") as f:
    us_map = geojson.load(f)


# hate_crime['VICTIM_COUNT'] = hate_crime['VICTIM_COUNT'].astype(int)
# disability.VICTIM_COUNT.dtype # Check that it's a string
# disability.STATE_ABBR.dtype

# Aggregate sums of total victims by state
disability_vcounts = disability.groupby(['STATE_ABBR', 'STATE_NAME'])['VICTIM_COUNT'].agg('count').reset_index()
physical = physical.groupby(['STATE_ABBR', 'STATE_NAME'])['VICTIM_COUNT'].agg('count').reset_index()
mental = mental.groupby(['STATE_ABBR', 'STATE_NAME'])['VICTIM_COUNT'].agg('count').reset_index()

# Check total counts
disability['VICTIM_COUNT'].sum()
physical['VICTIM_COUNT'].sum()
mental['VICTIM_COUNT'].sum()

# Aggregate victim counts by type of offense
offense_type = disability.groupby(['OFFENSE_NAME'])['VICTIM_COUNT'].agg('count').reset_index()

# Aggregate victim counts by type of location
location = disability.groupby(['LOCATION_NAME'])['VICTIM_COUNT'].agg('count').reset_index()

# Aggregate victim counts by type of victims
victim_types = disability.groupby(['VICTIM_TYPES'])['VICTIM_COUNT'].agg('count').reset_index()

# Create charts

# (1) Victims
chart1 = px.line(victims, x="Year", y= victims.columns, markers=True,
                title = "Number of Disabled Victims, <br>by Disability Bias (2004-2019)", height=600,)
chart1.update_layout(xaxis = dict(
        tickmode = 'linear',))
chart1.update_traces(marker_size=8)
chart1.update_layout(
    plot_bgcolor='rgba(0, 0, 0, 0)',
                     paper_bgcolor='rgba(0, 0, 0, 0)',
                     yaxis_title="Number of Victims")
chart1.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey')
chart1.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey')
chart1.update_layout(title_x=0.5, legend_title_text='Disability Bias')
chart1.update_traces(marker=dict(size=10),
                               hovertemplate= '<b>%{x}</b><br><br>' +
                                              "Number of victims: %{y:,.0f}<br>")

# (2) Incidents
chart2 = px.line(incidents, x="Year", y= incidents.columns, markers=True,
                title = "Number of Incidents, <br>by Disability Bias (2004-2019)", height=600,)
chart2.update_layout(xaxis = dict(
        tickmode = 'linear',))
chart2.update_traces(marker_size=8)
chart2.update_layout(
    plot_bgcolor='rgba(0, 0, 0, 0)',
                     paper_bgcolor='rgba(0, 0, 0, 0)',
                     yaxis_title="Number of Incidents")
chart2.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey')
chart2.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey')
chart2.update_layout(title_x=0.5, legend_title_text='Disability Bias')
chart2.update_traces(marker=dict(size=10),
                               hovertemplate= '<b>%{x}</b><br><br>' +
                                              "Number of Incidents: %{y:,.0f}<br>")

# (3) Offenders

chart3 = px.line(offenders, x="Year", y= offenders.columns, markers=True,
                title = "Number of Offenders, <br>by Disability Bias (2004-2019)", height=600,)
chart3.update_layout(xaxis = dict(
        tickmode = 'linear',))
chart3.update_traces(marker_size=8)
chart3.update_layout(
    plot_bgcolor='rgba(0, 0, 0, 0)',
                     paper_bgcolor='rgba(0, 0, 0, 0)',
                     yaxis_title="Number of Offenders")
chart3.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey')
chart3.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey')
chart3.update_layout(title_x=0.5, legend_title_text='Disability Bias')
chart3.update_traces(marker=dict(size=10),
                               hovertemplate= '<b>%{x}</b><br><br>' +
                                              "Number of Offenders: %{y:,.0f}<br>")

# (4) Offenses

chart4 = px.line(offenses, x="Year", y= offenses.columns, markers=True,
                title = "Number of Offenses, <br>by Disability Bias (2004-2019)", height=600,)
chart4.update_layout(xaxis = dict(
        tickmode = 'linear',))
chart4.update_traces(marker_size=8)
chart4.update_layout(
    plot_bgcolor='rgba(0, 0, 0, 0)',
                     paper_bgcolor='rgba(0, 0, 0, 0)',
                     yaxis_title="Number of Offenses")
chart4.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey')
chart4.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey')
chart4.update_layout(title_x=0.5, legend_title_text='Disability Bias')
chart4.update_traces(marker=dict(size=10),
                               hovertemplate= '<b>%{x}</b><br><br>' +
                                              "Number of Offenses: %{y:,.0f}<br>")


# (5) Comparison

chart5 = px.line(comparison, x="Year", y= comparison.columns, markers=True,
                title = "Number of Victims, <br>by Bias (2004-2019)", height=600,)
chart5.update_layout(xaxis = dict(
        tickmode = 'linear',))
chart5.update_traces(marker_size=8)
chart5.update_layout(
    plot_bgcolor='rgba(0, 0, 0, 0)',
                     paper_bgcolor='rgba(0, 0, 0, 0)',
                     yaxis_title="Number of Offenses")
chart5.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey')
chart5.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey')
chart5.update_layout(title_x=0.5, legend_title_text='Bias')
chart5.update_traces(marker=dict(size=10),
                               hovertemplate= '<b>%{x}</b><br><br>' +
                                              "Number of Victims: %{y:,.0f}<br>")


# (6) US MAP by Victim Count, Disability Bias
chart6 = px.choropleth_mapbox(disability_vcounts , geojson=us_map, locations='STATE_ABBR', color='VICTIM_COUNT',
                           featureidkey="properties.stusab",
                           hover_name = 'STATE_NAME', 
                           hover_data={'VICTIM_COUNT': True, 'STATE_NAME': False, 'STATE_ABBR': False},
                           color_continuous_scale=px.colors.sequential.deep,
                           mapbox_style="carto-positron",
                           zoom=3, center = {"lat": 37.09024, "lon": -95.712891},
                           opacity=0.8,
                           )
chart6.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

# (7) US MAP by Victim Count, Anti-Physical Bias
chart7 = px.choropleth_mapbox(physical, geojson=us_map, locations='STATE_ABBR', color='VICTIM_COUNT',
                           featureidkey="properties.stusab",
                           hover_name = 'STATE_NAME', 
                           hover_data={'VICTIM_COUNT': True, 'STATE_NAME': False, 'STATE_ABBR': False},
                           color_continuous_scale=px.colors.sequential.BuPu,
                           mapbox_style="carto-positron",
                           zoom=3, center = {"lat": 37.09024, "lon": -95.712891},
                           opacity=0.8,
                           )
chart7.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

# (8) US MAP by Victim Count, Anti-Mental Bias
chart8 = px.choropleth_mapbox(mental, geojson=us_map, locations='STATE_ABBR', color='VICTIM_COUNT',
                           featureidkey="properties.stusab",
                           hover_name = 'STATE_NAME', 
                           hover_data={'VICTIM_COUNT': True, 'STATE_NAME': False, 'STATE_ABBR': False},
                           color_continuous_scale=px.colors.sequential.Reds,
                           mapbox_style="carto-positron",
                           zoom=3, center = {"lat": 37.09024, "lon": -95.712891},
                           opacity=0.8,
                           )
chart8.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


# TYPES OF OFFENSES
# Sort column by victim count
sorted_off = offense_type.sort_values('VICTIM_COUNT', ascending=False)
# Top 15 offenses by victim count
top15_off = sorted_off.iloc[0:10,]

chart9 = px.bar(top15_off, x=top15_off['VICTIM_COUNT'], y=top15_off['OFFENSE_NAME'],
                title = "Disability Bias Victim Count, by Top 15 Types of Offenses",
                height=600)
chart9.update(layout=dict(title=dict(x=0.5)))
chart9.update_traces(hovertemplate= '<b>%{y}</b><br><br>' +
                                    "No. of Victims: %{x:,.0f}<br>")
chart9.update_layout(yaxis=dict(showgrid=False, showline=False, showticklabels=True))
chart9.update_layout(yaxis={'categoryorder':'total ascending'})
chart9.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)',paper_bgcolor='rgba(0, 0, 0, 0)',
                    xaxis_title="Number of Victims", yaxis_title="Type of Offense")


# LOCATIONS
# Sort column by victim count
sorted_loc = location.sort_values('VICTIM_COUNT', ascending=False)
# Top 15 offenses by victim count
top15_loc = sorted_loc.iloc[0:10,]

chart10 = px.bar(top15_loc, x=top15_loc['VICTIM_COUNT'], y=top15_loc['LOCATION_NAME'],
                title = "Disability Bias Victim Count, by Top 15 Locations",
                height=600)
chart10.update(layout=dict(title=dict(x=0.5)))
chart10.update_traces(hovertemplate= '<b>%{y}</b><br><br>' +
                                    "No. of Victims: %{x:,.0f}<br>")
chart10.update_layout(yaxis=dict(showgrid=False, showline=False, showticklabels=True))
chart10.update_layout(yaxis={'categoryorder':'total ascending'})
chart10.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)',paper_bgcolor='rgba(0, 0, 0, 0)',
                    xaxis_title="Number of Victims", yaxis_title="Location")


# VICTIM TYPES
chart11 = px.pie(victim_types, values = "VICTIM_COUNT", names ="VICTIM_TYPES",
               title="Disability Bias Victim Count, by Victim Type",
                height = 600,)
chart11.update(layout=dict(title=dict(x=0.5)))
chart11.update_traces(textposition='inside', textinfo='percent')
chart11.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)',paper_bgcolor='rgba(0, 0, 0, 0)')
chart11.update_traces(textposition='inside',
                      textinfo='percent',
                      hovertemplate= '<b>%{label}</b><br><br>' +
                                    "No. Victims: %{value:,.0f}<br>")

# Start the app
app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.LUX])

app.layout = html.Div(children=[

                html.Div(children = dcc.Graph(
                    id = 'victims',
                    figure = chart1),
                    style={'width': '50%', 'display': 'inline-block', 'font-family': 'Montserrat', 'padding-top': '1%', 
                    'padding-bottom': '1%'}),
                    
                html.Div(children = dcc.Graph(
                    id = 'incidents',
                    figure = chart2),
                    style={'width': '50%', 'display': 'inline-block', 'font-family': 'Montserrat', 'padding-top': '1%', 
                    'padding-bottom': '1%'}),

                html.Div(children = dcc.Graph(
                    id = 'offenders',
                    figure = chart3),
                    style={'width': '50%', 'display': 'inline-block', 'font-family': 'Montserrat', 'padding-top': '1%', 
                    'padding-bottom': '1%'}),

                html.Div(children = dcc.Graph(
                    id = 'offenses',
                    figure = chart4),
                    style={'width': '50%', 'display': 'inline-block', 'font-family': 'Montserrat', 'padding-top': '1%', 
                    'padding-bottom': '1%'}),
                

                html.Div(children = dcc.Graph(
                    id = 'comparison',
                    figure = chart5),
                    style={'width': '50%', 'display': 'inline-block', 'font-family': 'Montserrat', 'padding-top': '1%', 
                    'padding-bottom': '1%'}),

                html.Div(children = dcc.Graph(
                    id = 'counts_by_offense',
                    figure = chart9),
                    style={'width': '50%', 'display': 'inline-block', 'font-family': 'Montserrat', 'padding-top': '1%', 
                    'padding-bottom': '1%'}),
                
                html.Div(children = dcc.Graph(
                    id = 'counts_by_location',
                    figure = chart10),
                    style={'width': '50%', 'display': 'inline-block', 'font-family': 'Montserrat', 'padding-top': '1%', 
                    'padding-bottom': '1%'}),

                html.Div(children = dcc.Graph(
                    id = 'victim_types',
                    figure = chart11),
                    style={'width': '50%', 'display': 'inline-block', 'font-family': 'Montserrat', 'padding-top': '1%', 
                    'padding-bottom': '1%'}),

                html.Div(children=[
                html.H2(children="Victim Count by Disability Bias (1997-2020)", 
                className="header"), ],),
                
                html.Div(children = dcc.Graph(
                    id = 'map',
                    figure = chart6),
                    style={'width': '100%', 'display': 'inline-block', 'font-family': 'Montserrat', 'padding-top': '1%', 
                    'padding-bottom': '1%'}),

                html.Div(dcc.Textarea(
                value = "Source: FBI Hate Crime Database (1997-2020) ",
                style={'fontSize': "14px",'width': '80%', 'display': 'inline-block', 'font-family': 'Montserrat', 'margin-left': '50px', 
                'margin-right': '50px', 'color':'#4d4d4d'},
                readOnly = True)),

                html.Div(children=[
                html.H2(children="Victim Count by Anti-Physical Disability Bias (1997-2020)", 
                className="header"), ],),

                html.Div(children = dcc.Graph(
                    id = 'physical',
                    figure = chart7),
                    style={'width': '100%', 'display': 'inline-block', 'font-family': 'Montserrat', 'padding-top': '1%', 
                    'padding-bottom': '1%'}),
                
                html.Div(dcc.Textarea(
                value = "Source: FBI Hate Crime Database (1997-2020) ",
                style={'fontSize': "14px",'width': '80%', 'display': 'inline-block', 'font-family': 'Montserrat', 'margin-left': '50px', 
                'margin-right': '50px', 'color':'#4d4d4d'},
                readOnly = True)),

                html.Div(children=[
                html.H2(children="Victim Count by Anti-Mental Disability Bias (1997-2020)", 
                className="header"), ],),
                
                html.Div(children = dcc.Graph(
                    id = 'mental',
                    figure = chart8),
                    style={'width': '100%', 'display': 'inline-block', 'font-family': 'Montserrat', 'padding-top': '1%', 
                    'padding-bottom': '1%'}),

                html.Div(dcc.Textarea(
                value = "Source: FBI Hate Crime Database (1997-2020) ",
                style={'fontSize': "14px",'width': '80%', 'display': 'inline-block', 'font-family': 'Montserrat', 'margin-left': '50px', 
                'margin-right': '50px', 'color':'#4d4d4d'},
                readOnly = True)),

                
                ])


if __name__ == "__main__":
    app.run_server(debug=True)