# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

ls_list=[]

launch_sites_df = spacex_df.groupby(['Launch Site'], as_index=False).first()
launch_sites_df = launch_sites_df['Launch Site'].to_frame()
for index,site in launch_sites_df.iterrows():
    ls_list.append({"label":site['Launch Site'],"value":site['Launch Site']})
ls_list.append({"label":"ALL","value":"ALL"})

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                dcc.Dropdown(id='site-dropdown',options=ls_list,searchable=True,placeholder="Select a Launch Site here:", value='ALL',clearable=False),
                                html.Br(),

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                dcc.RangeSlider(id='payload-slider',min=0,max=10000,step=1000,value=[min_payload,max_payload]),

                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
@app.callback(
    Output(component_id='success-pie-chart',component_property='figure'),
    [Input(component_id='site-dropdown',component_property='value'),
     Input(component_id='payload-slider',component_property='value')]
)

def updateGraph(site_dropdown,payload_slider):

    spacex_dff = spacex_df
    spacex_dff = spacex_dff.loc[(spacex_dff['Payload Mass (kg)']>=payload_slider[0]) & (spacex_dff['Payload Mass (kg)']<=payload_slider[1])]

    if site_dropdown!='ALL':
        spacex_dff = spacex_dff.loc[spacex_dff['Launch Site']==site_dropdown]
        piechart = px.pie(spacex_dff,names='class')
    else:
        piechart = px.pie(spacex_dff, values='class', names='Launch Site')

    return piechart

# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(
    Output(component_id='success-payload-scatter-chart',component_property='figure'),
    [Input(component_id='site-dropdown',component_property='value'),
     Input(component_id='payload-slider',component_property='value')]
)

def updateGraph2(site_dropdown,payload_slider):

    spacex_dff = spacex_df
    spacex_dff = spacex_dff.loc[(spacex_dff['Payload Mass (kg)']>=payload_slider[0]) & (spacex_dff['Payload Mass (kg)']<=payload_slider[1])]

    if site_dropdown!='ALL':
        spacex_dff = spacex_dff.loc[spacex_dff['Launch Site']==site_dropdown]
        scatterplot = px.scatter(spacex_dff, x='Payload Mass (kg)',y='class',color='Booster Version Category')
    else:
        scatterplot = px.scatter(spacex_dff, x='Payload Mass (kg)',y='class',color='Launch Site')

    return scatterplot

# Run the app
if __name__ == '__main__':
    app.run_server()
