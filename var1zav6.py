import requests
import csv

b = str(input('Введите код региона = '))

reg1 = [ 12, 18, 21, 23, 26, 32, 35, 44, 46, 48, 51, 53, 56, 59, 61, 63, 65, 68, 71, 73, 74, 80, 85]
reg2 = ['01', '05', '07']
a = int(b) in reg1
c = reg1 in reg2


if a is False:
    if c is False:
        print('Код региона не в списке доступных. Повторите ввод')
        exit(0)

r = requests.get('https://registry.edbo.gov.ua/api/universities/?ut=1&lc='+b+'&exp=json')

universities: list = r.json()
data_headers = [
    'university_name',
    'university_site'
]

filtered_data = [{k: row[k] for k in data_headers} for row in universities]

with open('websites.csv', mode='w', encoding='CP1251') as f:
    writer = csv.DictWriter(f, fieldnames=filtered_data[0].keys())
    writer.writeheader()
    writer.writerows(filtered_data)
