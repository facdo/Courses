# Dash App layout
# Tutorial provided in:
# https://plot.ly/dash/getting-started

# Dash apps are composed of two parts:
# 1 - The Layout, which describes what the app looks like
# 2 - The Interactivity part, describes the way that the user can
# interact with the dash to change the displayed information

# Gettin Started:

import dash
import dash_core_components as dcc
import dash_html_components as html

# lets initialize our app
app = dash.Dash()

# describe our html layout
app.layout = html.Div(children=[
    html.H1(children='Testing Dash Functionalities'),
    html.Div(children='''
    Dash: A web application framework for Python!
    '''),

    # lets add a graph to our layout
    dcc.Graph(
    id='example-graph',
    figure={
        'data': [
            {'x':['a','b','c'], 'y':[4,1,2], 'type':'bar', 'name':'SF'},
            {'x': ['a','b','c'], 'y':[2,4,5], 'type':'bar', 'name':u'Montréal'}
        ],
        'layout':{
            'title': 'Dash Data Visualization Example'
        }
    }
    )
])

# Now lets run the app in the internal server
app.run_server(debug=True, port=8051)
