from os import write
from PIL import Image
from IPython.display import display
import requests as r
import datetime as dt
import csv


url = "https://api.covid19api.com/dayone/country/brazil"
resp = r.get(url)
print(resp.status_code)
raw_data = resp.json()
print(raw_data[0])
final_data = []
for obs in raw_data:
    final_data.append([obs['Confirmed'], obs['Deaths'], obs['Recovered'], obs['Active'], obs['Date']])
    print(final_data)

final_data.insert(0, ['confirmados', 'obitos', 'confirmados','ativos', 'data'])
print(final_data)

CONFIRMADOS = 0
OBITOS = 1
RECUPERADOS = 2
ATIVOS = 3
DATA = 4

for i in range(1, len(final_data)):
    final_data[i][DATA] = final_data[i][DATA][:10]
    print(final_data) 

# Exemplo de como utilizar date time
# print(dt.time(12,6,21,7), 'Hora:minuto:segundo.microsegundo')
# print('----')
# print(dt.date(2020,4,25), 'Ano-mês-dia')
# print('----')
# print(dt.datetime(2020,4,25,12,6,21,7), 'Ano-mês-dia Hora:minuto:segundo.microsegundo')

# Exemplo de uso do date

natal = dt.date(2020,12,25)
reveillon = dt.date(2021,1,1)

print(reveillon - natal)
print((reveillon - natal).days)
print((reveillon - natal).seconds)
print((reveillon - natal).microseconds)

# Utilizando csv
whit open('brasil-covid-csv', 'w') as file:
    write = csv.writer(file)
    write.writerows(final_data)

for i in range(1, len(final_data)):
    final_data[i][DATA] = dt.datetime.strptime(final_data[i][DATA], '%Y-%m-%d')
    print(final_data)

def get_datasets(y,labels):
    if type(y[0]) == list:
        datasets = []
        for i in range(len(y)):
            datasets.append({
                'label' : labels[i],
                'data' : y[i]})
        return datasets
    else:
        return [
            {
                'label' : labels[0],
                'data': y
                }
            ]

def set_title(title=''):
    if title != '':
        dispay = 'true'
    else:
        display = 'false'
    return {
        'title':title,
        'display': display
        }

def create_chart(x,y,labels,kind='bar',title=''):

    datasets = get_datasets(y,labels)
    options = set_title(title)

    chart = {
        'type' : kind,
        'data' : {
            'labels': x,
            'datasets': datasets
            },
        'options':options
        }
    return chart

def get_api_chart(chart):
    url_base = 'https://quickchart.io/chart'
    resp = r.get(f'{url_base}?c={str(chart)}')
    return resp.content

def save_image(path, content):
     whit open(path, 'wb') as image:
         image.write(content)

def display_image(path):
    img_pil = Image.open(path)
    display(img_pil)

y_data_1 = []
for obs in final_data[1::10]:
    y_data_1.append(obs[CONFIRMADOS])

y_data_2 = []
for obs in final_data[1::10]:
    y_data_1.append(obs[RECUPERADOS])

label = ['Confirmados', 'Recuperados']

x = []
for obs in final_data[1::10]:
    x.append(obs[DATA].strftime('%d/%m/%Y'))

chart =  create_chart(x [y_data_1, y_data_2], labels, title='Gráfico confirmados vs recuperados')
chart_content = get_api_chart(chart)
save_image('meu-primeiro-grafico.png',chart_content)
display_image('meu-primeiro-grafico.png')