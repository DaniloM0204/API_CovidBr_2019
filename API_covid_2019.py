import requests as r
import datetime as dt

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

