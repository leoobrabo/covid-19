import PySimpleGUI as sg
from covid import Covid
import sys

covid = Covid()
covid_brasil = covid.get_status_by_country_id(24)
paises = covid.list_countries()

lista = []
tamanho = len(paises)

for i in range(tamanho):
    lista.append(paises[i]['name'])


sg.theme('Reddit')

layout = [
    [sg.Text('Casos de Covid-19 (Global)')],
    [sg.Button('Casos Ativos', size=(20, 0)),
     sg.Input(key='ativos', size=(13, 0))],
    [sg.Button('Casos Confirmados', size=(20, 0)),
     sg.Input(key='confirmados', size=(13, 0))],
    [sg.Button('Casos Recuperados', size=(20, 0)),
     sg.Input(key='recuperados', size=(13, 0))],
    [sg.Button('Casos Fatais', size=(20, 0)),
     sg.Input(key='mortes', size=(13, 0))],
    [sg.Text('Casos de Covid-19 (Brasil)')],
    [sg.Button('Casos Ativos Brasil', size=(20, 0)),
     sg.Input(key='ativos brasil', size=(13, 0))],
    [sg.Button('Casos Confirmados Brasil', size=(20, 0)),
     sg.Input(key='confirmados brasil', size=(13, 0))],
    [sg.Button('Casos Recuperados Brasil', size=(20, 0)),
     sg.Input(key='recuperados brasil', size=(13, 0))],
    [sg.Button('Casos Fatais Brasil', size=(20, 0)),
     sg.Input(key='mortes brasil', size=(13, 0))],
    [sg.Combo(values=(lista), key='escolha', size=(36, 0))],
    [sg.Button('Escolha', size=(20, 0))],
    [sg.Text('Busca Casos de Covid-19', key='pais')],
    [sg.Button('Ativos', size=(20, 0)),
     sg.Input(key='ativos escolha', size=(13, 0))],
    [sg.Button('Confirmados', size=(20, 0)),
     sg.Input(key='confirmados escolha', size=(13, 0))],
    [sg.Button('Recuperados', size=(20, 0)),
     sg.Input(key='recuperados escolha', size=(13, 0))],
    [sg.Button('Fatais', size=(20, 0)),
     sg.Input(key='mortes escolha', size=(13, 0))]
]

janela = sg.Window('Dados Covid-19', layout=layout)

while True:
    event, valores = janela.Read()
    if event == sg.WIN_CLOSED:
        janela.close()
        sys.exit()
        break
    elif event == 'Casos Ativos':
        janela['ativos'].update(float(covid.get_total_active_cases()))
    elif event == 'Casos Confirmados':
        janela['confirmados'].update(covid.get_total_confirmed_cases())
    elif event == 'Casos Recuperados':
        janela['recuperados'].update(covid.get_total_recovered())
    elif event == 'Casos Fatais':
        janela['mortes'].update(covid.get_total_deaths())
    elif event == 'Casos Ativos Brasil':
        janela['ativos brasil'].update(covid_brasil['active'])
    elif event == 'Casos Confirmados Brasil':
        janela['confirmados brasil'].update(covid_brasil['confirmed'])
    elif event == 'Casos Recuperados Brasil':
        janela['recuperados brasil'].update(covid_brasil['recovered'])
    elif event == 'Casos Fatais Brasil':
        janela['mortes brasil'].update(covid_brasil['deaths'])
    elif event == 'Escolha':
        escolha_caso = covid.get_status_by_country_name(valores['escolha'])
        pais = escolha_caso['country']
        janela['pais'].update(f'Casos de Covid-19 {pais}')
    elif event == 'Recuperados':
        janela['recuperados escolha'].update(float(escolha_caso['recovered']))
    elif event == 'Ativos':
        janela['ativos escolha'].update(escolha_caso['active'])
    elif event == 'Confirmados':
        janela['confirmados escolha'].update(escolha_caso['confirmed'])
    elif event == 'Fatais':
        janela['mortes escolha'].update(escolha_caso['deaths'])
