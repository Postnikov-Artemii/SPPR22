import xmltodict
from StreetAnalys import *
from pymystem3 import Mystem
import csv

#Открытие OSM и конвертация в Dict
fin = open('vlg.osm', 'r', encoding='utf-8')
text = fin.read()
fin.close()
dct = xmltodict.parse(text)

streets = []

csv_file = open('StreetName.csv', 'w', newline='')
writer = csv.DictWriter(csv_file, fieldnames=['Name', 'Analys'])
writer.writeheader()
my_stem = Mystem()

for way in dct['osm']['way']:
    if 'tag' in way:
        tags = way['tag']
        name = 'noname'
        if isinstance(tags, list):
            for tag in tags:
                # Проверка совпадения тега
                if '@k' in tag and tag['@k'] == 'addr:street':
                    # Сохранение координат
                    equ = False
                    print(tag['@v'])
                    for k in range(len(streets)):
                        if streets[k] == tag['@v']:
                            equ = True
                    if equ == False:
                        print('*')
                        streets.append(tag['@v'])
                        writer.writerow({'Name': tag['@v'], 'Analys': ''.join(my_stem.lemmatize(''.join(street_analysis(tag['@v']))))})

print(streets)
csv_file.close()
