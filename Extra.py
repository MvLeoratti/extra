from dash import Dash, html, dcc, Output, Input
import pandas as pd
import plotly.express as px

app = Dash(__name__)

df = pd.read_excel("Pets.xlsx")
#Armazena os dados em uma varivel chamada excel



fig = px.pie(df, values='Quantidade', names='Loja')
opcoes = list(df['Loja'].unique())

opcoes.append("Todas as Lojas")

app.layout = html.Div(children=[
    
    html.H1(children = 'Faturamento das Lojas'),
    html.H2(children= 'Grafico de Faturaento de todos os Pets separados por loja'),
    dcc.Dropdown(opcoes, value = 'Todas as Lojas', id='lista_lojas'),
    dcc.Graph 
    (
        id = 'Grafico_quantidade_pets',
        figure = fig
    )    
])

@app.callback(
    Output('Grafico_quantidade_pets', 'figure'),
    Input('lista_lojas', 'value')
)

def update_output(value):
    if value == 'Todas as Lojas':
        fig = px.pie(df, values='Quantidade', names='Loja')
    else:
        tabela_filtrada = df.loc[df['Codigo']==value,:]
        fig = px.pie(tabela_filtrada, values='Quantidade', names='Loja')
    return fig

if __name__=='__main__':
    app.run(debug=True)