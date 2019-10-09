# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

import dash

import dash_core_components as dcc

import dash_daq as daq

import dash_html_components as html

from dash.dependencies import Input, Output

 

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

 

df = pd.read_csv("Admission_Values.csv")

X = df[df.columns.difference(['Chance of Admit ', 'Serial No.'])]

Y=df['Chance of Admit ']

 

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression

 

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

 

regressor = LinearRegression() 

regressor.fit(X_train, Y_train)

 

 

 

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

 

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server=app.server

 

app.layout = html.Div([

       

    html.H1('Master Program Acceptance Predictor'),

       

    html.Div([  

    html.Label('GRE Score'),

    dcc.Slider(id='gre-slider',

            min=0, max=340, step=1, value=170,

               marks={

        0: {'label': '0'},

        100: {'label': '100'},

        200: {'label': '200'},

        300: {'label': '300'},

        340: {'label': '340'}                                

    }),

 

html.Br(),

html.Label('TOEFL Score'),

dcc.Slider(id='toefl-slider',

            min=0, max=120, step=1, value=60,

               marks={

        0: {'label': '0'},

        25: {'label': '25'},

        50: {'label': '50'},

        75: {'label': '75'},

        100: {'label': '100'},

        120: {'label': '120'}                               

    }),

 

html.Br(),

html.Label('University Rating'),

dcc.Slider(id='rating-slider',

            min=0, max=5, step=1, value=3,

               marks={

        0: {'label': '0'},

        1: {'label': '1'},

        2: {'label': '2'},

        3: {'label': '3'},

        4: {'label': '4'},

        5: {'label': '5'},

                                

    }),

 

html.Br(),

html.Label('Statement of Purpose'),

dcc.Slider(id='sop-slider',

            min=0, max=5, step=1, value=3,

               marks={

        0: {'label': '0'},

        1: {'label': '1'},

        2: {'label': '2'},

        3: {'label': '3'},

        4: {'label': '4'},

        5: {'label': '5'},

                               

    }),

 

html.Br(),

html.Label('Letter of Recommendation'),

dcc.Slider(id='lor-slider',

            min=0, max=5, step=1, value=3,

               marks={

        0: {'label': '0'},

        1: {'label': '1'},

        2: {'label': '2'},

        3: {'label': '3'},

        4: {'label': '4'},

        5: {'label': '5'},

                                

    }),

 

html.Br(),

html.Label('College GPA'),

dcc.Slider(id='gpa-slider',

            min=0, max=10, step=1, value=5,

               marks={

        0: {'label': '0'},

        2: {'label': '2'},

        4: {'label': '4'},

        6: {'label': '6'},

       8: {'label': '8'},

        10: {'label': '10'},

                               

    }),

 

html.Br(),

html.Label('Research Experience'),

dcc.Slider(id='research-slider',

            min=0, max=1, step=1, value=0,

               marks={

        0: {'label': '0'},

        1: {'label': '1'},

                               

    }),

],className="pretty_container four columns"),

 

  html.Div([

 

    daq.Gauge(

        id='my-gauge',

        showCurrentValue=True,

        color={"gradient":True,"ranges":{"red":[0,0.4],"yellow":[0.4,0.7],"green":[0.7,1]}},

        label="Probability",

        max=1,

        min=0,

        value=1

    ),

])

    ])

 

 

@app.callback(

    Output('my-gauge', 'value'),

    [Input('gre-slider', 'value'),

     Input('toefl-slider', 'value'),

     Input('rating-slider', 'value'),

     Input('sop-slider', 'value'),

     Input('lor-slider', 'value'),

     Input('gpa-slider', 'value'),

     Input('research-slider', 'value')

     ])

def update_output_div(gre,

                      toefl,

                      rating,

                      sop,

                      lor,

                      gpa,

                      research):

   X_case =pd.DataFrame({'CGPA':[gpa],'GRE Score':[gre],'LOR':[lor],'Research':[research],'SOP':[sop],'TOEFL Score':[toefl],'University Rating':[rating]})

   Y_case = regressor.predict(X_case)

 

   return Y_case[0]

 

 

if __name__ == '__main__':

    app.run_server()
