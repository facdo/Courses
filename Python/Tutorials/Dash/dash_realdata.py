# Gettin Started:
import pandas as pd
import plotly.offline as py
import plotly.figure_factory as ff
import dash
import dash_auth
import dash_core_components as dcc
import dash_html_components as html


def isfloat(string):
    if string == 'inf':
        return False
    try:
        float(string)
        return True
    except ValueError:
        return False

#
def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )

PASSWORD_PAIR = [['user', 'password']]
# lets initialize our app
app = dash.Dash('auth')
# authentication criteria
auth = dash_auth.BasicAuth(app, PASSWORD_PAIR)

test_report_df = pd.read_excel('datalog_file.xlsx', sheetname=1)
test_report_df = test_report_df.drop(test_report_df.columns[[0,1,3,4]], axis=1)
# test_report_df.set_index('Test#')
print(test_report_df.head())

datalog_df = pd.read_excel('datalog_file.xlsx', sheetname=0)
datalog_df = datalog_df.drop(datalog_df.columns[[2,3,6,8]], axis=1)

test_dict = {}
bin_dict = {}
for test in set(datalog_df['Test#']):
    temp_df = datalog_df[datalog_df['Test#']==test]
    temp_rp = test_report_df[test_report_df['Test#']==test]

    if all(map(isfloat, list(temp_df['Value']))) and all(map(isfloat,list(temp_rp['Sdev']))):
        test_dict[test]=list(map(float,list(temp_df['Value'])))
        bin_dict[test] = [el/10 for el in list(map(float,temp_rp['Sdev']))]

# hist_data = [test_dict[2000]]
# group_labels = ['Test 2000']
bins, hist_data, group_labels = [], [], []
for k in test_dict.keys():
    if bin_dict[k][0]!=0:
        bins.append(bin_dict[k][0])
        hist_data.append(test_dict[k])
        group_labels.append("Test# {}".format(k))

#
test_N, Cpk_list = [], []
for v, c in zip(test_report_df['Test#'], test_report_df['Cpk']):
    if isfloat(c) and not pd.isnull(c) and float(c)<10:
        test_N.append('Test: {}'.format(v))
        Cpk_list.append(c)
# hist_data = list(test_dict.values())
# group_labels = ['Test#: {}'.format(el) for el in list(test_dict.keys())]
# print(len(bins), len(hist_data))

# #Create distplot with custom bin_size
fig = ff.create_distplot(hist_data[10:], group_labels[10:], bin_size=bins[10:])

# Plot!
# py.plot(fig, filename='distplot_tests')

# describe our html layout
app.layout = html.Div(children=[
    html.H1(children='Dash Application Example',
            style={'textAlign': 'center', 'color': '#7FDFF'}),
    html.Div(children='''
    Dash: A web application framework for Python! It enables the generation of
    interactive plots and automatic reports.
    '''),

    html.H3('Distribution Plot - Verum 18 Continuity Tests',
            style={'textAlign': 'center', 'color': '#7FDFF'}),
    # lets add a table to our layout
    # lets add a graph to our layout
    dcc.Graph(
    id='example-graph',
    figure = fig
    # figure={
    #     'data' : fig,
    #     # 'data': [
    #     #     {'x':[1,2,3], 'y':[4,1,2], 'type':'bar', 'name':'SF'},
    #     #     {'x': [1,2,3], 'y':[2,4,5], 'type':'bar', 'name':u'Montréal'}
    #     # ],
    #     'layout':{
    #         'title': 'Dash Data Visualization Example'
    #     }
    # }
    ),
    dcc.Graph(
    id = 'another-graph',
    figure={
        'data': [
            {'x':test_N, 'y':Cpk_list, 'type':'bar', 'name':'Tests Cpk'}
        ],
        'layout':{
            'title':'Verum 18 Tests Cpk'
        }
    }
    ),
    # lets add a table to our layout
    html.H3('Verum 18 Test Summary', style={'textAlign': 'center', 'color': '#7FDFF'}),
    generate_table(test_report_df)
])


app.scripts.config.serve_locally = True
# Now lets run the app in the internal server
app.run_server(debug=True)
