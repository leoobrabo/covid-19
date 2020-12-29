import PySimpleGUI as sg
from covid import Covid
import sys

sg.theme('Reddit')

lista = ('US', 'India', 'Brazil', 'Russia', 'France', 'United Kingdom', 'Turkey', 'Italy', 'Spain', 'Germany', 'Colombia', 'Argentina', 'Mexico', 'Poland', 'Iran', 'Ukraine', 'South Africa', 'Peru', 'Netherlands', 'Indonesia', 'Czechia', 'Belgium', 'Romania', 'Chile', 'Iraq', 'Canada', 'Bangladesh', 'Pakistan', 'Philippines', 'Switzerland', 'Morocco', 'Sweden', 'Israel', 'Portugal', 'Saudi Arabia', 'Austria', 'Serbia', 'Hungary', 'Jordan', 'Nepal', 'Panama', 'Japan', 'Georgia', 'Azerbaijan', 'Ecuador', 'Croatia', 'United Arab Emirates', 'Kazakhstan', 'Bulgaria', 'Belarus', 'Lebanon', 'Slovakia', 'Dominican Republic', 'CostaRica', 'Denmark', 'Armenia', 'Bolivia', 'Kuwait', 'Qatar', 'Moldova', 'Greece', 'West Bankand Gaza', 'Guatemala', 'Lithuania', 'Egypt', 'Tunisia', 'Oman', 'Ethiopia', 'Burma', 'Honduras', 'Slovenia', 'Venezuela', 'Bosniaand Herzegovina', 'Malaysia', 'Paraguay', 'Libya', 'Algeria', 'Kenya', 'China', 'Bahrain', 'Ireland', 'Nigeria', 'North Macedonia', 'Kyrgyzstan', 'Uzbekistan', 'Korea,South', 'Singapore', 'Albania', 'Ghana', 'Afghanistan', 'Kosovo', 'Norway', 'Montenegro', 'Luxembourg', 'El Salvador', 'Sri Lanka', 'Latvia', 'Finland', 'Uganda',
         'Australia', 'Estonia', 'Cameroon', 'Sudan', 'Namibia', 'Coted"Ivoire"', 'Cyprus', 'Zambia', 'Senegal', 'Mozambique', 'Madagascar', 'Uruguay', 'Angola', 'Congo(Kinshasa)', 'Botswana', 'Mauritania', 'Guinea', 'Maldives', 'Tajikistan', 'Zimbabwe', 'Jamaica', 'Malta', 'Cabo Verde', 'Cuba', 'Syria', 'Belize', 'Haiti', 'Gabon', 'Eswatini', 'Rwanda', 'Andorra', 'Bahamas', 'Trinidad and Tobago', 'Congo(Brazzaville)', 'Mali', 'Thailand', 'Malawi', 'BurkinaFaso', 'Guyana', 'Suriname', 'Nicaragua', 'Djibouti', 'Iceland', 'EquatorialGuinea', 'CentralAfricanRepublic', 'Somalia', 'Gambia', 'Togo', 'SouthSudan', 'Benin', 'Niger', 'Lesotho', 'SierraLeone', 'Guinea-Bissau', 'SanMarino', 'NewZealand', 'Yemen', 'Liechtenstein', 'Chad', 'Liberia', 'Vietnam', 'Mongolia', 'Eritrea', 'SaoTomeandPrincipe', 'Burundi', 'Monaco', 'Taiwan*', 'PapuaNewGuinea', 'Comoros', 'DiamondPrincess', 'Bhutan', 'Mauritius', 'Tanzania', 'Barbados', 'Cambodia', 'SaintLucia', 'Seychelles', 'AntiguaandBarbuda', 'Brunei', 'Grenada', 'SaintVincentandtheGrenadines', 'Dominica', 'Fiji', 'Timor-Leste', 'Laos', 'SaintKittsandNevis', 'HolySee', 'SolomonIslands', 'MSZaandam', 'MarshallIslands', 'Samoa', 'Vanuatu')

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
covid = Covid()
covid_brasil = covid.get_status_by_country_id(24)
paises = covid.list_countries()

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
