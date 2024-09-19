from dash import Dash, html, dcc, Output, Input
import pandas as pd
import plotly.express as px

app = Dash(__name__)

df = pd.read_excel("PETS.xlsx")
#Armazena os dados em uma varivel chamada excel

fig = px.bar(df, x="Raça", y = "Quantidade", color="ID_PET", barmode="group")

opcoes = list(df['ID_PET'].unique())

opcoes.append("Todas as Loja")

app.layout = html.Div(children=[
    
    html.H1(children = 'Faturamento das Lojas'),
    html.H2(children= 'Grafico de Faturaento de todos os produtos separados por loja'),
    dcc.Dropdown(opcoes, value = 'Todas as Lojas', id='lista_lojas'),
    dcc.Graph 
    (
        id = 'Grafico_quantidade_produto',
        figure = fig
    )    
])

@app.callback(
    Output('grafico_quantidade_produto', 'figure'),
    Input('lista_lojas', 'value')
)

def update_output(value):
    if value == 'Todas as Lojas':
        fig = px.bar(df, x = 'Raça', y = 'Quantidade', color='ID_PET', barmode= 'group')
    else:
        tabela_filtrada = df.loc[df['ID_PET']==value,:]
        fig = px.bar(tabela_filtrada, x = "Raça", y="Quantidade",  color="ID_PET", barmode="group")
    return fig

if __name__=='__main__':
    app.run(debug=True)