# coding=utf-8

from flask import Flask
import plotly.graph_objs as go
import dash_html_components as html
import dash_core_components as dcc
import dash

from dash.dependencies import Input, Output

text_color = 'rgb(36,36,36)'
bg_color = 'rgb(255,255,255)'
grid_color = '#666666'
black_text = '#000000'
block_quote_text = 'rgb(64,64,64)'
blue_text = 'rgb(51, 153, 255)'
hard_gray = 'rgb(77,77,77)'

server = Flask(__name__)

elections = dash.Dash(name='Bootstrap_docker_app',
                server=server,
                url_base_pathname='/elections/',
                csrf_protect=False)

elections.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})



tabs_styles = {
    'height': '54px'
	# 'color': 'rgb(51,153,255)'
}
tab_style = {
    'borderBottom': '2px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold',
	'font-size':'24px',
	'color': 'rgb(51,153,255)'
}

tab_selected_style = {
    'borderTop': '2px solid #d6d6d6',
    'borderBottom': '2px solid #d6d6d6',
    'backgroundColor': '#119DFF',
	'font-size':'24px',
    'padding': '6px'
}

elections.layout = html.Div([
    dcc.Tabs(id="tabs-styled-with-inline", value='tab-2', children=[
        dcc.Tab(label='Economic', value='tab-1', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Elections', value='tab-2', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Social', value='tab-3', style=tab_style, selected_style=tab_selected_style)

    ], style=tabs_styles),
    html.Div(id='tabs-content-inline')
]
)

@elections.callback(Output('tabs-content-inline', 'children'),
              [Input('tabs-styled-with-inline', 'value')])
def render_content(tab):

	if tab == 'tab-1':
	    return html.Div([
			dcc.Graph(
			id='example-graph-1',
			figure = {
			        'data': [
			        {'x': [1, 2, 3], 'y': [4, 1, 2],
			         'type': 'bar', 'name': 'SF','color':'rgb(77,77,77)'},
			        {'x': [1, 2, 3], 'y': [2, 4, 5],
			         'type': 'bar', 'name': u'Montréal'},
			        ],
					'layout': go.Layout(
						title = 'this is the Economic Slide',
						paper_bgcolor = 'rgba(0,0,0,0)',
						plot_bgcolor = 'rgba(0,0,0,0)'
				 )
				    }
			    )

	    ])



	elif tab == 'tab-2':
	    return html.Div([
		    dcc.Graph(
		    id='example-graph-2',
		    figure={
			    'data': [
				    {'x': [1, 2, 3], 'y': [1, 4, 1],
				     'type': 'bar', 'name': 'SF'},
				    {'x': [1, 2, 3], 'y': [1, 2, 3],
				     'type': 'bar', 'name': u'Montréal'},
			    ]
		    }
	    )
		        ]
	    )

	elif tab == 'tab-3':
	    return html.Div([
		    dcc.Graph(
		    id='example-graph-3',
		    figure={
			    'data': [
				    {'x': [1, 2, 3], 'y': [2, 4, 3],
				     'type': 'bar', 'name': 'SF'},
				    {'x': [1, 2, 3], 'y': [2, 1, 3],
				     'type': 'bar', 'name': u'Montréal'},
			    ]
		    }
	    )
		        ]
	    )



if __name__ == '__main__':
    elections.run_server(debug=True)