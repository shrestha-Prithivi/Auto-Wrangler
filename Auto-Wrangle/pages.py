import dash 
import dash_bootstrap_components as dbc 
import dash_core_components as dcc 
import dash_html_components as html
from graphs import * 
from dash_extensions import Download


def Homepage():
  HomePage = html.Div([
    html.Br(),
    html.Br(),
    html.Br(),
    dcc.Upload(
    id='upload-data',
    children=html.Div([

     html.Button('Select Files',className="btn btn--1"),
  
    ],style={'textAlign': 'center'}
    ),
   
    
    multiple=True
),
  html.Br(),
    html.Br(),
    
 
  html.Div([
    html.Div([dcc.Loading(children=[  html.Div(id='output-data-upload', style ={ 'display' : 'flex', 'justify-content' : 'center'}),html.Br(),],type='circle'),
  ],style={'width':'1200px', 'textAlign': 'center'}),
  
 

  html.Div([ html.Button('Clean Data', className="btn btn--2",id='btn-1',n_clicks=0)],style={'position':'relative','width':'1200px','textAlign': 'center'}),
  
  html.Div([dcc.Loading(children=[html.Div([html.Div(id='cleaned-data', style ={ 'display' : 'flex', 'justify-content' : 'center'}),])],type='circle')],style={'width':'1200px','textAlign': 'center'}),
 

  html.Div([html.Button("Download cleaned csv", className="btn btn--3", id="btnn"), Download(id="download")])
  ],
  style={'position':'relative','width':'1200px', 'textAlign': 'center'}
),


  ],style={}

  )


  return HomePage

def About_us():
  content = html.Div([
   
    html.Div([ html.H2("About Us:",style={'color':'white'}),html.P("Data pre-processing and visualization made easy with “AUTO WRANGLER”",style={'color':'white'})]),
    html.Hr(style={'border':'1px solid white'}),
    html.Br(),
    
    html.P("The world is becoming more and more data driven with endless amount of data available to work with, that also in several areas or fields. You will need to invest a significant amount of time to get your data pre-processed or analyzed to derive any useful insights. It is indeed a fact.",style={'color':'white'}),
    html.Br(),
    html.P("""But drop all your worries and your frets over not having the time, as we give to you the successfully developed amazing web application.    
             AUTO WRANGLER helps you pre-process any set of data and also provides you with a feature to effectively visualize your data set for better understanding of any information the data can produce.
     This automated data cleaning and analyzing web application has been built in python’s framework Dash along with the help of python’s libraries as a part of our semester project to free you of all the tedious tasks as you get involved in working your ways with any data.""",style={"color":"white"}),
    html.A("Get Started!", href="/homepage",style={'color':'white'})  
  ],style={'textAlign':'center'})  

  return content



def Charts(cleaned_data):
    try:
        if cleaned_data == 0:
            
            print("No data")
            Charts = dbc.Container(html.H5("No data"))
    except:        
        output_graph = RunGraph(cleaned_data)
        Charts = dbc.Container([html.Div(children = output_graph)])


    return Charts
