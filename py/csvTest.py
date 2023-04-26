import csv
from StreetAnalys import *
from pymystem3 import Mystem

print('Парсинг улиц')
with open('StreetName.txt', 'r', encoding='utf-8') as file:
    text = file.read().split("\n")

file = open('StreetName.csv', 'w', newline='')
writer = csv.DictWriter(file, fieldnames=['Name', 'Analys'], delimiter = ';')
writer.writeheader()

my_stem = Mystem()
print('Обработка')
for i in range(len(text)):
    data_upd=''.join(street_analysis(text[i]))
    data = []
    data=my_stem.lemmatize(data_upd)
    for k in data:
        if k == '\n':
            data.remove('\n')
    print(i, ' ', ''.join(data))
    writer.writerow({'Name': text[i], 'Analys': ''.join(data)})

file.close()