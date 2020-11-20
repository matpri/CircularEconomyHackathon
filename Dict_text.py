# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 10:45:26 2020

@author: MPrina
"""
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import base64
#Osmosi_inversa, Nanofiltrazione, Recupero_calore, PV, PdC

dic_ima={'osmosi':r"C:\Users\MPrina\Desktop\Varie\Hackathon Mantova\App\Osmosi_inversa.png",
         'Nanofiltrazione':r"C:\Users\MPrina\Desktop\Varie\Hackathon Mantova\App\Nanofiltrazione.png",
         'Rec cal':r"C:\Users\MPrina\Desktop\Varie\Hackathon Mantova\App\Rec_cal.png",
         'PV':r"C:\Users\MPrina\Desktop\Varie\Hackathon Mantova\App\PV.png",
         'PdC':r"C:\Users\MPrina\Desktop\Varie\Hackathon Mantova\App\Pompadical.png"}
# dic_ima={'osmosi':r"C:\Users\MPrina\Desktop\Varie\Hackathon Mantova\App\OI.svg"}
encoded_image_OI = base64.b64encode(open(dic_ima['osmosi'], 'rb').read())
encoded_image_N = base64.b64encode(open(dic_ima['Nanofiltrazione'], 'rb').read())
encoded_image_RC = base64.b64encode(open(dic_ima['Rec cal'], 'rb').read())
encoded_image_PV = base64.b64encode(open(dic_ima['PV'], 'rb').read())
encoded_image_PdC = base64.b64encode(open(dic_ima['PdC'], 'rb').read())

Osmosi_inversa=dbc.Row([
    
    dbc.Col([
        dbc.Row([html.H6("Osmosi Inversa"),
                 ], justify='center'),
        dbc.Row([
            dbc.Col([
                dbc.Row([
                    html.Img(src='data:image/png;base64,{}'.format(encoded_image_OI.decode()), style={'height':'50%', 'width':'50%'})
                    ], justify='center')
                ],xs=6, sm=5, md=5, lg=2, xl=2),

            dbc.Col([
                
                # html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()), style={'height':'90%', 'width':'75%'})
                dcc.Markdown('''Per ottenere un siero concentrato al 18% di solidi totali, l’impianto sarà realizzato con due stadi di concentrazione, 
                             entrambi con membrane di osmosi inversa. Il permeato prodotto dall’impianto di osmosi è sì demineralizzato, ma presenta 
                             ancora un COD critico per lo scarico in acque superficiali. Non è quindi garantibile la scaricabilità in acque superficiali, 
                             secondo D. Lgs 152/06, Parte terza, Allegato 5, Tabella 3. Per questo motivo, la nostra offerta prevede anche un **impianto
                            di Polisher**, che tratta il permeato prodotto dall’osmosi al fine di renderlo scaricabile. Il concentrato prodotto dall’impianto
                            Polisher sarà riciclato in testa all’impianto di osmosi, nel serbatoio di stoccaggio siero. Per il calcolo dei costi e delle 
                            emissioni dell'osmosi inversa sono stati considerati i seguenti valori: Produzione di Siero = 50000L/giorno, Mezzi di trasporto 
                            al giorno = 2.5, Percorso medio per camion = 65 km, Costo per trasporto = 1.5€/L, 
                            Prezzo di vendita del siero non concentrato = 11€/t, Prezzo di vendita del siero a valle dell'osmosi inversa = 43 €/t
                            percentuale di siero a valle dell'Osmosi inversa = 32.4%, **Percentuale di permeato** = **67.6**%, consumo di diesel camion = 35L/100km,
                            Fattore di emissione del Diesel =0.267 t CO2/MWh
                            '''),
                # html.P(' '),
                
                ],xs=10, sm=10, md=10, lg=9, xl=9),
                ], justify='center'),
            html.Hr(), 
            ]),
    # html.Hr(),                                            
    ], justify='center')



Recupero_calore=dbc.Row([
    dbc.Col([
        dbc.Row([html.H6("Recupero Calore"),
                 ], justify='center'),        
        dbc.Row([
            dbc.Col([
                dbc.Row([
                    html.Img(src='data:image/png;base64,{}'.format(encoded_image_RC.decode()), style={'height':'50%', 'width':'50%'})
                    ], justify='center')
                ],xs=6, sm=5, md=5, lg=2, xl=2),

            dbc.Col([
                
                # html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()), style={'height':'90%', 'width':'75%'})
                dcc.Markdown('''Il recupero del calore dal siero a 45-50°C permette di riutilizzare questo calore per ridurre i consumi in caldaia
                             e quidni risparmia l'acquisto di combustibili e la produzione di emissioni di CO2. Uno scambiatore di calore, 
                             o semplicemente scambiatore, è un'apparecchiatura chimica in cui si realizza lo scambio di energia termica di un 
                             fluido termovettore con altri aventi temperatura diverse. Per il calcolo dei costi e delle 
                             emissioni del sistema con recupero del calore dal siero sono stati considerati i seguenti valori: 
                             Costo d'investimento = 100000€, Costo di manutenzione = 1000€/anno, Vita utile = 15 anni, 
                             Calore specifico del latte = 3.9 kJ/t, densità latte = 1030 kg/m3, latte al giorno = 600 quintali, 
                             Costo gas naturale = 0.1 €/kWh, Costo energia elettrica = 0.15 €/kWh, Efficienza caldaia = 0.8, efficienza pompa di calore = 3,
                             efficienza recupero calore = 0.65, efficienza chiller = 2.5, fattore di emissione gas naturale = 0.202 kg/kWh,
                             fattore di emissione energia elettrica = 0.483 kg/kWh
                            '''),
                # html.P(' '),
                
                ],xs=10, sm=10, md=10, lg=9, xl=9),
                ], justify='center'),
            html.Hr(), 
            ]),
    # html.Hr(),                                            
    ], justify='center')

Nanofiltrazione=dbc.Row([
    dbc.Col([
        dbc.Row([html.H6("Nanofiltrazione"),
                 ], justify='center'),
        dbc.Row([
            dbc.Col([
                dbc.Row([
                    html.Img(src='data:image/png;base64,{}'.format(encoded_image_N.decode()), style={'height':'50%', 'width':'50%'})
                    ], justify='center')
                ],xs=6, sm=5, md=5, lg=2, xl=2),

            dbc.Col([
                
                # html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()), style={'height':'90%', 'width':'75%'})
                dcc.Markdown('''Per raggiungere la concentrazione del 25%, l’impianto sarà sempre con due stadi, ma, mentre il primo avrà membrane di
                     osmosi inversa, il secondo sarà con membrane di nanofiltrazione che permettono di ottenere concentrazioni più alte con
                     pressioni meno elevate di quelle che si dovrebbero applicare con membrane di osmosi. Per questa concentrazione, è necessaria
                     una maggiore superficie membranica, per cui si prevede l’inserimento di un vessel con 3 membrane in più rispetto all’osmosi. 
                     Il permeato prodotto dall’impianto è sì demineralizzato, ma presenta 
                     ancora un COD critico per lo scarico in acque superficiali. Non è quindi garantibile la scaricabilità in acque superficiali, 
                     secondo D. Lgs 152/06 Parte terza, Allegato 5, Tabella 3. Per questo motivo, la nostra offerta prevede anche un **impianto
                    di Polisher**, che tratta il permeato prodotto dall’osmosi al fine di renderlo scaricabile. Il concentrato prodotto dall’impianto
                    Polisher sarà riciclato in testa all’impianto di osmosi, nel serbatoio di stoccaggio siero.
                    Per il calcolo dei costi e delle emissioni della nanofiltrazione sono stati considerati i seguenti valori:
                    Produzione di Siero = 50000L/giorno, Mezzi di trasporto al giorno = 2.5, Percorso medio per camion = 65 km, Costo per trasporto
                    = 1.5€/L, Prezzo di vendita del siero non concentrato = 11€/t, Prezzo di vendita del siero a valle della nanofiltrazione = 50 €/t
                    percentuale di siero a valle della nanofiltrazione = 24%, **Percentuale di permeato** = **76**%, consumo di diesel camion = 35L/100km,
                    Fattore di emissione del Diesel =0.267 t CO2/MWh'''),
                # html.P(' '),
                
                ],xs=10, sm=10, md=10, lg=9, xl=9),
                ], justify='center'),
            html.Hr(), 
            ]),
    # html.Hr(),                                            
    ], justify='center')




PV=dbc.Row([
    dbc.Col([
        dbc.Row([html.H6("Fotovoltaico (PV)"),
                 ], justify='center'),
        dbc.Row([
            dbc.Col([
                dbc.Row([
                    html.Img(src='data:image/png;base64,{}'.format(encoded_image_PV.decode()), style={'height':'50%', 'width':'50%'})
                    ], justify='center')
                ],xs=6, sm=5, md=5, lg=2, xl=2),

            dbc.Col([
                
                # html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()), style={'height':'90%', 'width':'75%'})
                dcc.Markdown('''Un impianto fotovoltaico è un impianto elettrico costituito essenzialmente dall'assemblaggio di più moduli 
                             fotovoltaici che sfruttano l'energia solare incidente per produrre energia elettrica mediante effetto fotovoltaico,
                             della necessaria componente elettrica (cavi) ed elettronica (inverter) ed eventualmente di sistemi meccanici-automatici 
                             ad inseguimento solare. Può essere utile installare il fotovoltaico per risparmiare sulla energia elettrica autoconsumata.
                             Particolarmente interessante se accoppiato alla pompa di calore che aumenta la domanda di energia elettrica. 
                             Per il calcolo dei costi e delle emissioni del sistema con fotovoltaico sono stati considerati i seguenti valori: Costo d'investimento = 1500€/kW, 
                             Potenza installata = 50kWp, Costo di manutenzione = 750€/anno, vita utile=25 anni, 
                             Calore specifico del latte = 3.9 kJ/t, densità latte = 1030 kg/m3, latte al giorno = 600 quintali, 
                             Costo gas naturale = 0.1 €/kWh, Costo energia elettrica = 0.15 €/kWh, Efficienza caldaia = 0.8, efficienza pompa di calore = 3,
                             efficienza recupero calore = 0.65, efficienza chiller = 2.5, fattore di emissione gas naturale = 0.202 kg/kWh,
                             fattore di emissione energia elettrica = 0.483 kg/kWh
                            '''),
                # html.P(' '),
                
                ],xs=10, sm=10, md=10, lg=9, xl=9),
                ], justify='center'),
            html.Hr(), 
            ]),
    # html.Hr(),                                            
    ], justify='center')


PdC=dbc.Row([
    dbc.Col([
        dbc.Row([html.H6("Pompa di Calore (PdC)"),
                 ], justify='center'),
        dbc.Row([
            dbc.Col([
                dbc.Row([
                    html.Img(src='data:image/png;base64,{}'.format(encoded_image_PdC.decode()), style={'height':'50%', 'width':'50%'})
                    ], justify='center')
                ],xs=6, sm=5, md=5, lg=2, xl=2),

            dbc.Col([
                
                # html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()), style={'height':'90%', 'width':'75%'})
                dcc.Markdown('''Una pompa di calore è una macchina termica in grado di estrarre e trasferire energia termica utilizzando 
                             differenti forme di energia, generalmente meccanica. Questa macchina può estrarre calore dall'ambiente o da una fonte di calore
                             e consumando energia elettrica 
                             produce calore a temperatura piu alta con un elevata efficienza. Può essere interessante l'installazione di pompe di calore 
                             laddove vi sia una una fonte di calore disponibile. In questo caso la fonte di calore è il siero che deve inoltre essere raffreddato prima del suo smaltimento. 
                             l'applicazione della pompa di calore ha un doppio beneficio: sfrutta il calore in eccesso del siero raffreddandolo e produce calore 
                             a temperatura piu elevata che puo essere usato nei processi dell'impianto. Per il calcolo dei costi e delle emissioni 
                             del sistema con pompa di calore sono stati considerati i seguenti valori: Costo d'investimento = 200000€, 
                             Potenza installata = 250kWp, Costo di manutenzione = 2000€/anno, vita utile=15 anni, 
                             Calore specifico del latte = 3.9 kJ/t, densità latte = 1030 kg/m3, latte al giorno = 600 quintali, 
                             Costo gas naturale = 0.1 €/kWh, Costo energia elettrica = 0.15 €/kWh, Efficienza caldaia = 0.8, efficienza pompa di calore = 3,
                             efficienza recupero calore = 0.65, efficienza chiller = 2.5, fattore di emissione gas naturale = 0.202 kg/kWh,
                             fattore di emissione energia elettrica = 0.483 kg/kWh
                            '''),
                # html.P(' '),
                
                ],xs=10, sm=10, md=10, lg=9, xl=9),
                ], justify='center'),
            html.Hr(), 
            ]),
    # html.Hr(),                                            
    ], justify='center')