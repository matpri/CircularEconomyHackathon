# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 14:49:29 2020

@author: MPrina
"""
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
import base64
import dash_daq as daq
import plotly.graph_objs as go
import chart_studio.plotly as py
import numpy as np
from Dict_text import Osmosi_inversa, Nanofiltrazione, Recupero_calore, PV, PdC

def NPV(C0, Cesercizio, lifetime, Dr):
    t = pd.DataFrame(index = np.arange(lifetime))
    
    cash_flow=[]
    NPV=[]
    for a in range(len(t.index)):
        if a==0:
            cash_flow.append(C0)
            NPV.append(cash_flow[-1]*-1)
        else:
            cash_flow.append((Cesercizio*-1)/((1+Dr)**a))
            NPV.append(NPV[-1] + cash_flow[-1])
    t['cash flow'] = cash_flow
    t['NPV'] = NPV
    print(t)
    
    payback=t[t['NPV'] >=0.].index.tolist()
    payback.append(lifetime)
    PbT= min(payback)
    NetPV=NPV[-1]
        
    # print(t)
    return t, PbT, NetPV

dic={'Soluzione 1':'S1 = Osmosi inversa',
     'Soluzione 2':'S2 = Nanofiltrazione',
     'Soluzione 3':'S3 = Recupero calore',
     'Soluzione 4':'S4 = Recupero calore + Osmosi inversa',
     'Soluzione 5':'S5 = Recupero calore + Nanofiltrazione',
     'Soluzione 6':'S6 = Recupero calore + Fotovoltaico',
     'Soluzione 7':'S7 = Recupero calore + Fotovoltaico + Pompa di Calore',
     'Soluzione 8':'S8 = Recupero calore + Fotovoltaico + Pompa di Calore + Osmosi inversa',
     'Soluzione 9':'S9 = Recupero calore + Fotovoltaico + Pompa di Calore + Nanofiltrazione',
     'Soluzione 10':'S10 = Fotovoltaico + Pompa di Calore'}

dic2={'Soluzione 1':[Osmosi_inversa],
     'Soluzione 2':[Nanofiltrazione],
     'Soluzione 3':[Recupero_calore],
     'Soluzione 4':[Recupero_calore, Osmosi_inversa],
     'Soluzione 5':[Recupero_calore, Nanofiltrazione],
     'Soluzione 6':[Recupero_calore, PV],
     'Soluzione 7':[Recupero_calore, PV, PdC],
     'Soluzione 8':[Recupero_calore, PV, PdC, Osmosi_inversa],
     'Soluzione 9':[Recupero_calore, PV, PdC, Nanofiltrazione],
     'Soluzione 10':[PV, PdC]}

ex = pd.ExcelFile("calcolo_stato_dell_arte.xlsx")
df = ex.parse("soluzioni (2)")
df=df.set_index('soluzioni')

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

image_filename = "C:\\Users\\MPrina\\Desktop\\Varie\\Hackathon Mantova\\App\\CEH.png"

image_filename_Virg = "C:\\Users\\MPrina\\Desktop\\Varie\\Hackathon Mantova\\App\\Virgilio.png"
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

encoded_image_Virg = base64.b64encode(open(image_filename_Virg, 'rb').read())
# the style arguments for the sidebar.
SIDEBAR_STYLE = {
    # 'position': 'fixed',
    # 'top': 0,
    # 'left': 0,
    # 'bottom': 0,
    # 'width': '20%',
    'padding': '20px 10px',
    'background-color': '#f8f9fa'
}

MAIN_STYLE = {
    # 'position': 'fixed',
    # 'top': 0,
    # 'left': 0,
    # 'bottom': 0,
    # 'width': '20%',
    'padding': '20px 10px',
    'background-color': 'white'
}

Footbar_STYLE = {
    'padding': '25px 75px 50px 30px',
    'background-color': '#BBBDBF'
}

padding_STYLE = {
    'padding': '25px 0px 0px 0px'
}

riquadri_STYLE= {
    'padding': '25px 25px 25px 25px',
    # 'background-color': '#D0D2D3'
}

CARD_TEXT_STYLE = {
    'textAlign': 'center',
    'color': '#D0D2D3'
}
charts_STYLE= {
    'padding': '50px 0px 0px 0px',
    # 'background-color': '#D0D2D3'
}

app.layout = html.Div([
        dbc.Row([
            dbc.Col([
                dbc.Row([html.H2("Soluzioni")
                         ], justify='center'),
                html.Hr(),
                dbc.Row([html.H5("Scegli una soluzione impiantistica:")
                         ], justify='center'),
                dbc.Row([dcc.RadioItems(id='radio_items',options=[
                                {'label': 'S1 = Osmosi inversa (OI)', 'value': 'Soluzione 1'},
                                {'label': 'S2 = Nanofiltrazione (N)', 'value': 'Soluzione 2'},
                                {'label': 'S3 = Recupero calore', 'value': 'Soluzione 3'},
                                {'label': 'S4 = Recupero calore + OI', 'value': 'Soluzione 4'},
                                {'label': 'S5 = Recupero calore + N', 'value': 'Soluzione 5'},
                                {'label': 'S6 = Recupero calore + PV', 'value': 'Soluzione 6'},
                                {'label': 'S7 = Recupero calore + PV + PdC', 'value': 'Soluzione 7'},
                                {'label': 'S8 = Recupero calore + PV + PdC + OI', 'value': 'Soluzione 8'},
                                {'label': 'S9 = Recupero calore + PV + PdC + N', 'value': 'Soluzione 9'},
                                {'label': 'S10 = PV + PdC', 'value': 'Soluzione 10'},
                                        ], value='Soluzione 1', inputStyle={"margin-right": "20px"}, labelStyle={'display': 'block'} )
                    ], justify='center'),
                html.Hr(),
                dbc.Row([html.H5("Scegli i valori dei parametri:")
                          ], justify='center'),
                dbc.Row([
                    dbc.Col([
                        daq.NumericInput(id='input-num', value=5, label="Tasso d'interesse", labelPosition='top')
                        ], xs=12, sm=12, md=10, lg=6, xl=6),
                    dbc.Col([
                        daq.NumericInput(id='input-num2', value=1, label="Tasso d'inflazione", labelPosition='top'),
                        ], xs=12, sm=12, md=10, lg=6, xl=6),
                    ], justify='center'),

                html.Hr(),
                dbc.Row([dbc.Button('Calcola', id='button', size="lg", className="mr-1", color="dark")
                         ], justify='center'),
                ], xs=12, sm=12, md=10, lg=5, xl=3,style=SIDEBAR_STYLE),
            
            dbc.Col([
                dbc.Row([html.H2("Visualizzazione dei risultati")
                         ], justify='center'), 
                html.Hr(),
                # dcc.Graph(id='graph_pbt'),
                dbc.Tabs(children=[
                    dbc.Tab(label="Descrizione", tab_id="Descrizione", children= [
                        dbc.Row([html.H5(id='definition', children=["init"])
                                 ], justify='center', style=padding_STYLE),
                        html.Hr(),
                        html.Div(id='other_div')
                        ]),
                    
                    dbc.Tab(label="Grafici", tab_id="Grafici", children=[
                        dbc.Row([html.H5(id='definition2', children=["init2"])
                                 ], justify='center', style=padding_STYLE),
                        html.Hr(),
                        dbc.Row([
                            dbc.Col([
                                dbc.Card(
                                    dbc.CardBody([
                                        html.H5("Tempo di ritorno dell'investimento", className="card-title"),
                                        html.P(id='GraficoDef1', children=["initG1"], className="card-text")
                                        ]), style={"background-color": "#E6E7E8", 'min-height': '100px'},),  #style={"background-color": "#D0D2D3"},                              
                                ], xs=12, sm=12, md=10, lg=4, xl=4,style=riquadri_STYLE),
                            dbc.Col([
                                dbc.Card(
                                    dbc.CardBody([
                                        html.H5("Risparmio di emissioni di CO2", className="card-title"),
                                        html.P(id='GraficoDef2', children=["initG2"], className="card-text")
                                        ]), style={"background-color": "#E6E7E8", 'min-height': '100px'},),                                
                                ], xs=12, sm=12, md=10, lg=4, xl=4,style=riquadri_STYLE),                            
                            dbc.Col([
                                dbc.Card(
                                    dbc.CardBody([
                                        html.H5("Infortuni nei trasporti", className="card-title"),
                                        html.P(id='GraficoDef3', children=["initG3"], className="card-text")
                                        ]), style={"background-color": "#E6E7E8", 'min-height': '100px'},),                                
                                ], xs=12, sm=12, md=10, lg=4, xl=4,style=riquadri_STYLE),
                                 ], justify='center', style=padding_STYLE),  
                        html.Hr(),
                        dbc.Row([
                            html.H6("Tempo di ritorno dell'investimento e Net Present Value finale"),
                            ], justify='center'),
                        dbc.Row([
                            dbc.Col([
                                dcc.Graph(id='graph_pbt')
                                ], xs=11, sm=11, md=10, lg=10, xl=10),
                            ], justify='center'),
                        ]),
                    dbc.Tab(label="Confronto", tab_id="Confronto",children=[
                        dbc.Row([
                            dbc.Col([
                                dcc.Graph(id='graph_pbt2')
                                ], xs=11, sm=11, md=10, lg=5, xl=5, style=charts_STYLE),
                            dbc.Col([
                                dcc.Graph(id='graph_pbt3')
                                ], xs=11, sm=11, md=10, lg=5, xl=5, style=charts_STYLE),                           
                            ], justify='center'),
                        dbc.Row([
                            dbc.Col([
                                dcc.Graph(id='graph_pbt4')
                                ], xs=11, sm=11, md=10, lg=5, xl=5, style=charts_STYLE),
                            dbc.Col([
                                dcc.Graph(id='graph_pbt5')
                                ], xs=11, sm=11, md=10, lg=5, xl=5, style=charts_STYLE),                           
                            ], justify='center'),
                            ])
                    ])
                # html.H5("Scegli una soluzione impiantistica:")
                ], xs=12, sm=12, md=10, lg=7, xl=9,style=MAIN_STYLE),
            ], justify='center'),
        
        dbc.Row([
            dbc.Col([
                dbc.Row([
                    dbc.Col([
                            html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()), style={'height':'90%', 'width':'75%'})
                            ], xs=12, sm=10, md=8, lg=6, xl=4),
                    dbc.Col([
                            html.H5("Sfida 4 - Consorzio Virgilio"),
                            html.P("Scopo: Rendere piu sostenibile il trasporto e lo smaltimento del siero, prodotto di scarto dei caseifici del consorzio."),
                            html.H5("Gruppo Aria"), 
                            html.P("Membri: Chiara Dipasquale, Riccardo Marchetti, Matteo Giacomo Prina, Anna Saccoccio, Angelo Scardino"), 
                            ], xs=12, sm=10, md=8, lg=6, xl=5),
                    dbc.Col([
                            html.Img(src='data:image/png;base64,{}'.format(encoded_image_Virg.decode()), style={'height':'90%', 'width':'85%'})
                            ], xs=12, sm=10, md=8, lg=6, xl=3)                    
                    ]),
                ], xs=12, sm=12, md=12, lg=12, xl=12,style=Footbar_STYLE)
            ], justify='center')

])

@app.callback(
    Output('graph_pbt', 'figure'),
    [Input('button', 'n_clicks')],
    [State('radio_items', 'value'),
     State('input-num', 'value'),
     State('input-num2', 'value')])
def update_graph_1(n_clicks, value, T_int, T_inf):
    
    T_SDS=T_int-T_inf
    solution= value
    print(value)
    # print(T_int, type(T_int))
    z, PbT, NetPV=NPV(df.loc[solution, 'Investimento iniziale'], df.loc[solution, 'Costo annuale [€]'],df.loc[solution, 'Vita utile'], T_SDS/100.)
    
    z["Color"] = np.where(z["NPV"]<0, '#E15837', '#9DB155')

    
    trace0 = go.Bar(
        x=z.index,
        y=z['NPV'],
        name="NPV",
        marker_color=z['Color'],
        showlegend= False
        # mode="lines+markers",
        # line=dict(color="#013848")
    )
    
    trace1 = go.Scatter(
        x=z.index,
        y=z['NPV'],
        name="NPV",
        mode="lines+markers",
        line=dict(color="#013848"),
        showlegend= False
        
    )
    trace2 = go.Scatter(
        x=[PbT],
        y=[0],
        name="Pay back time",
        mode="markers",
        marker_symbol='x',
        marker_color="gold",
        marker=dict(size=16,line=dict(width=2,color='DarkSlateGrey'))
        # line=dict(color="#013848")
    )
    
    data = [trace0,trace1,trace2]#, trace3]
    
    layout = go.Layout(yaxis=dict(title='cash flow [€]', zeroline=False),
                        xaxis=dict(title="Years", zeroline = False),
                        legend=dict(yanchor="bottom", y=0.01, xanchor="right", x=0.99),
                        margin=dict(l=0, r=0, t=20, b=20)
                        )
    
    fig = go.Figure(data=data, layout=layout)
    return fig

@app.callback(
    [Output('graph_pbt2', 'figure'),
     Output('graph_pbt3', 'figure'),
     Output('graph_pbt4', 'figure'),
     Output('graph_pbt5', 'figure')],
    [Input('button', 'n_clicks')],
    [State('radio_items', 'value'),
     State('input-num', 'value'),
     State('input-num2', 'value')])
def update_graph_2(n_clicks, value, T_int, T_inf):
    
    T_SDS=T_int-T_inf
    
    list_PbT=[]
    list_NetPV=[]
    list_index=list(df.index)
    for a in range(len(list_index)):
        solution=list_index[a]
        z, PbT, NetPV=NPV(df.loc[solution, 'Investimento iniziale'], df.loc[solution, 'Costo annuale [€]'],df.loc[solution, 'Vita utile'], T_SDS/100.)
        list_PbT.append(PbT)
        list_NetPV.append(NetPV)
    
    df['PbT']=list_PbT
    df['NPV']=list_NetPV
    
    #plot 1 PBT-----------------
    df["Color1"] = np.where(df.index==value, '#ECBF48', '#9C9EA1')
    # df["Color2"] = np.where(df["Emissioni di CO2 all'anno [t]"]==df.loc[value, "Emissioni di CO2 all'anno [t]"], 'gold', 'blue')
    
    trace011 = go.Bar(
        y=df.index,
        x=df["PbT"],
        name="Ritorno dell'investimento",
        orientation='h',
        marker_color=df['Color1'],
        showlegend= False
        # mode="lines+markers",
        # line=dict(color="#013848")
    )
    # trace012 = go.Scatter(
    #     x=df["PbT"],
    #     y=df.index,
    #     name="NPV",
    #     mode="lines+markers",
    #     line=dict(color="#013848"),
    #     showlegend= False
        
    # )
    
   
    data01 = [trace011]#, trace012]
    
    layout01 = go.Layout(title="Ritorno dell'investimento", 
                         xaxis=dict(title="Ritorno dell'investimento [anni]", zeroline = False),
                       margin=dict(l=0, r=20, t=50, b=20)
                      )
    
    fig01 = go.Figure(data=data01, layout=layout01)
    
    #plot 2 Emissions-----------------
    df["Color2"] = np.where(df.index==value, '#ECBF48', '#9C9EA1')
    # df["Color2"] = np.where(df["Emissioni di CO2 all'anno [t]"]==df.loc[value, "Emissioni di CO2 all'anno [t]"], 'gold', 'blue')
    
    trace021 = go.Bar(
        y=df.index,
        x=df["Emissioni di CO2 all'anno [t]"],
        name="Emissioni di CO2",
        orientation='h',
        marker_color=df['Color2'],
        showlegend= False
        # mode="lines+markers",
        # line=dict(color="#013848")
    )
    trace022 = go.Scatter(
        x=df["Emissioni di CO2 all'anno [t]"],
        y=df.index,
        name="Emissioni di CO2",
        mode="lines+markers",
        line=dict(color="#5F8852"),
        showlegend= False
        
    )
   
    data = [trace021, trace022]
    
    layout = go.Layout(title="Emissioni di CO2",
                       xaxis=dict(title="Emissioni di CO2 [t]", zeroline = False),
                       margin=dict(l=0, r=20, t=50, b=20)
                      )
    
    fig02 = go.Figure(data=data, layout=layout)
    #plot 3 NPV-----------------

    df["Color3"] = np.where(df.index==value, '#ECBF48', '#9C9EA1')
    # df["Color3"] = np.where(df["Investimento iniziale"]==df.loc[value, "Investimento iniziale"], 'gold', 'blue')
    
    trace031 = go.Bar(
        y=df.index,
        x=df["NPV"],
        name="Net Present Value",
        orientation='h',
        marker_color=df['Color3'],
        showlegend= False
        # mode="lines+markers",
        # line=dict(color="#013848")
    )
    trace032 = go.Scatter(
        x=df["NPV"],
        y=df.index,
        name="NPV",
        mode="lines+markers",
        line=dict(color="grey"),
        showlegend= False
        
    )
    
   
    data02 = [trace031, trace032]
    
    layout02 = go.Layout(title="Net Present Value",
                         xaxis=dict(title="Net Present Value [€]", zeroline = False),
                       margin=dict(l=0, r=20, t=50, b=20)
                      )
    
    fig03 = go.Figure(data=data02, layout=layout02)
    #plot 4 Inv iniz-----------------
    df["Color4"] = np.where(df.index==value, '#ECBF48', '#9C9EA1')
    # df["Color3"] = np.where(df["Investimento iniziale"]==df.loc[value, "Investimento iniziale"], 'gold', 'blue')
    
    trace041 = go.Bar(
        y=df.index,
        x=df["Investimento iniziale"],
        name="Investimento iniziale",
        orientation='h',
        marker_color=df['Color4'],
        showlegend= False
        # mode="lines+markers",
        # line=dict(color="#013848")
    )
    trace042 = go.Scatter(
        x=df["Investimento iniziale"],
        y=df.index,
        name="Investimento iniziale",
        mode="lines+markers",
        line=dict(color="grey"),
        showlegend= False
        
    )
    
   
    data04 = [trace041, trace042]
    
    layout04 = go.Layout(title="Investimento iniziale",
                         xaxis=dict(title="Investimento iniziale [€]", zeroline = False),
                       margin=dict(l=0, r=20, t=50, b=20)
                      )
    
    fig04 = go.Figure(data=data04, layout=layout04)
    
    
    return fig01, fig02, fig03, fig04
    

@app.callback(
    [Output('definition', 'children'),
     Output('definition2', 'children'),
     Output('GraficoDef1', 'children'),
     Output('GraficoDef2', 'children'),
     Output('GraficoDef3', 'children')],
    [Input('button', 'n_clicks')],
    [State('radio_items', 'value'),
     State('input-num', 'value'),
     State('input-num2', 'value')])
def update_text_2(n_clicks, value, T_int, T_inf):
    
    T_SDS=T_int-T_inf
    text=dic[value]
    
    solution= value
    z, PbT, NetPV=NPV(df.loc[solution, 'Investimento iniziale'], df.loc[solution, 'Costo annuale [€]'],df.loc[solution, 'Vita utile'], T_SDS)
    # df.loc[]
    risparmio_emiss=df.loc['Stato attuale', "Emissioni di CO2 all'anno [t]"]-df.loc[value, "Emissioni di CO2 all'anno [t]"]
    
    infortuni= df.loc[value, "Infortuni"]
    if infortuni==0:
        text_inf='Nessuna variazione'
    else:
        text_inf='Riduzione pari al '+ str(infortuni)+ '%'
    
    Riq_1=str(PbT)+ " anni."
    Riq_2=str(round(risparmio_emiss, 1)) + " kt di emissioni di CO2 all'anno."
    Riq_3=text_inf
    
    
    return text, text, Riq_1, Riq_2, Riq_3


@app.callback(
    Output('other_div', 'children'),
    [Input('button', 'n_clicks')],
    [State('radio_items', 'value')])
def update_description(n_clicks, value):
    # text=dic[value]
    solution= value
    
    output=[]
    # i=0
    for a in range(len(dic2[solution])):
        # output.append((html.Div(id='id-' + str(i), children=[html.Button('Reset', id='id-0-'+str(i), n_clicks=0)])))
        # i=i+1
        output.append(dic2[solution][a])
    
    return html.Div(children=output)

if __name__ == "__main__":
    app.run_server(debug=True)