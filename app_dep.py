import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import flask

app = dash.Dash(
    __name__,
    assets_folder = 'assets',
    )

url_bar_and_content_div = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


layout = html.Div([
    html.Nav([
        html.Div([
            html.A(['About'], href='/page-about', className='nav_button'),
            html.P(['About Info'], id='about_info'),
        ],className='nav_group'),
    ],
    id='nav')
])

# layout = html.Div([
#     html.Nav([
#         html.Li(html.A(['About'], href='/page-about', className='nav_button'),className='nav_li'),
#         html.Div(html.P('When you hover over one of the menu items this text should show up.'),id='hide'),
#         html.Li(html.A('Map', href='/page-map', className='nav_button'),className='nav_li'),
#         html.Li(html.A('Overview', href='/page-overview', className='nav_button'),className='nav_li'),
#         html.Li(html.A('Compare', href='/page-compare', className='nav_button'),className='nav_li'),
#         html.Li(html.A('Closeup', href='/page-closeup', className='nav_button'),className='nav_li')
#     ],
#     id='nav'
#     ),
# ],
# className='body'
# )


# layout = html.Div([
#     html.Nav([ # the entire nav bar
#         html.A([ # one button on the nav bar
#             html.Div(
#                     dcc.Link(html.H3('About'), href='/page-about'),
#                     className='about_button',
#                     ),
#             html.Div(html.P('When you hover over one of the menu items this text should show up.',
#             className='about_text_hover'),className='hide')
#             ],
#             className='navigationA'
#             ),
#         html.A([ # one button on the nav bar
#             html.Div(
#                     dcc.Link(html.H3('Map'), href='/page-map'),
#                     className='map_button',
#                     ),
#             html.Div(html.P('When you hover over one of the menu items this text should show up.'),className='hide')
#             ],
#             className='navigationA'
#             ),
#         html.A([ # one button on the nav bar
#             html.Div(
#                     dcc.Link(html.H3('Compare'), href='/page-compare'),
#                     className='compare_button',
#                     ),
#             html.Div('When you hover over one of the menu items this text should show up.',className='hide')
#             ],
#             className='navigationA'
#             ),
#         html.A([ # one button on the nav bar
#             html.Div(
#                     dcc.Link(html.H3('Overview'), href='/page-overview'),
#                     className='overview_button',
#                     ),
#             html.Div('When you hover over one of the menu items this text should show up.',className='hide')
#             ],
#             className='navigationA'
#             ),
#         html.A([ # one button on the nav bar
#             html.Div(
#                     dcc.Link(html.H3('Closeup'), href='/page-closeup'),
#                     className='closeup_button',
#                     ),
#             html.Div('When you hover over one of the menu items this text should show up.',className='hide')
#             ],
#             className='navigationA'
#             ),
#     ],
#     className='whole_navbar'
#     ),
# ],
# className='body'
# )

layout_page_1 = html.Div([
    html.H2('Page 1'),
    dcc.Input(id='input-1-state', type='text', value='Montreal'),
    dcc.Input(id='input-2-state', type='text', value='Canada'),
    html.Button(id='submit-button', n_clicks=0, children='Submit'),
    html.Div(id='output-state'),
    html.Br(),
    dcc.Link('Navigate to "/"', href='/'),
    html.Br(),
    dcc.Link('Navigate to "/page-2"', href='/page-2'),
])

layout_page_2 = html.Div([
    html.H2('Page 2'),
    dcc.Dropdown(
        id='page-2-dropdown',
        options=[{'label': i, 'value': i} for i in ['LA', 'NYC', 'MTL']],
        value='LA'
    ),
    html.Div(id='page-2-display-value'),
    html.Br(),
    dcc.Link('Navigate to "/"', href='/'),
    html.Br(),
    dcc.Link('Navigate to "/page-1"', href='/page-1'),
])

# index layout
app.layout = url_bar_and_content_div

# "complete" layout
app.validation_layout = html.Div([
    url_bar_and_content_div,
    layout,
    layout_page_1,
    layout_page_2,
])


# Index callbacks
@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == "/page-about":
        return layout_page_1
    elif pathname == "/page-overview":
        return layout_page_2
    else:
        return layout


# Page 1 callbacks
@app.callback(Output('output-state', 'children'),
              Input('submit-button', 'n_clicks'),
              State('input-1-state', 'value'),
              State('input-2-state', 'value'))
def update_output(n_clicks, input1, input2):
    return ('The Button has been pressed {} times,'
            'Input 1 is "{}",'
            'and Input 2 is "{}"').format(n_clicks, input1, input2)


# Page 2 callbacks
@app.callback(Output('page-2-display-value', 'children'),
              Input('page-2-dropdown', 'value'))
def display_value(value):
    print('display_value')
    return 'You have selected "{}"'.format(value)


if __name__ == '__main__':
    app.run_server(
        debug=True)