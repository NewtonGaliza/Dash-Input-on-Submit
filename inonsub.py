import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([

  html.P('What Thay Say About'),
  dcc.Input(id='my-id', type='text'),
  html.Button('Submit', id='button'),
  html.Div(id='my-div')

])

@app.callback(

  Output(component_id='my-div', component_property='children'),
  [Input('button', 'n_clicks')],
  state=[State(component_id='my-id', component_property='value')]

)

def output(n_clicks,input_value):
    if input_value != None:
        return 'Term is {}'.format(input_value)

if __name__ == '__main__':
    app.run_server(debug=True)
