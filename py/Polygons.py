#Библиотека для конвертации osm файла в список
import xmltodict
import time
import json
start = time.time()

# Открытие OSM и конвертация в Dict
with open('vlg.osm', 'r', encoding='utf-8') as fin:
    text = fin.read()
dct = xmltodict.parse(text)

# Бордовый, Красный, Желтый, Зелёный, Тёмно зелёный
# Ключи и значения объектов, профильтрованны по цветам
buildings=[[['shop', 'frozen_food'],
            ['shop', 'convenience']],

           [['amenity','biergarten'],
            ['building','kiosk'],
            ['building','supermarket'],
            ['shop', 'supermarket'],
            ['shop','brewing_supplies'],
            ['shop', 'greengrocer'],
            ['shop', 'health_food'],
            ['shop', 'pasta'],
            ['shop', 'water']],

           [['amenity', 'fast_food'],
            ['amenity', 'food_court'],
            ['amenity','ice_cream'],
            ['amenity', 'pub'],
            ['shop', 'alcohol'],
            ['shop', 'bakery'],
            ['shop', 'beverages'],
            ['shop', 'butcher'],
            ['shop', 'cheese'],
            ['shop', 'chocolate'],
            ['shop', 'coffee'],
            ['shop', 'dairy'],
            ['shop', 'farm'],
            ['shop', 'ice_cream'],
            ['shop', 'seafood'],
            ['shop', 'spices'],
            ['shop', 'tea'],
            ['shop', 'wine']],

           [['amenity', 'cafe'],
            ['amenity','bar'],
            ['shop', 'confectionery'],
            ['shop', 'deli'],
            ['shop', 'pastry']],

           [['amenity','restaurant']]]

#Список полигонов, профильтрованных по цветам
colorOfPolygon = []
# colorOfMarkers = []
# for color in range(len(colors)):
for color in range(5):
    #Список полигонов одного цвета
    polygons = []
    for way in dct['osm']['way']:
        if 'tag' in way:
            tags = way['tag']
            flag = False
            if isinstance(tags, list):
                for tag in tags:
                    # Проверка совпадения тега
                    for j in range(len(buildings[color])):
                        if '@k' in tag and tag['@k'] == buildings[color][j][0] and tag['@v'] == buildings[color][j][1]:
                            flag = True
                            # Сохранение координат
                            coordinats1 = []
                            for nd in way['nd']:
                                id = nd['@ref']
                                for node in dct['osm']['node']:
                                    if node['@id'] == id:
                                        coordinats2 = []
                                        coordinats2.append(float(node['@lat']))
                                        coordinats2.append(float(node['@lon']))
                                        coordinats1.append(coordinats2)

                            print(coordinats1)
                            print(buildings[color][j][1])
                            print(color)
                            # Сохранение полигона
                            polygons.append(coordinats1)
                            print()

    # Поиск точек
    for node in dct['osm']['node']:
        if 'tag' in node:
            tags = node['tag']
            flag = False
            if isinstance(tags, list):
                for tag in tags:
                    # Проверка совпадения тега
                    for j in range(len(buildings[color])):
                        if '@k' in tag and tag['@k'] == buildings[color][j][0] and tag['@v'] == buildings[color][j][1]:
                            flag = True
                            # Сохранение координат
                            coordinats1 = []
                            for k in range(5):
                                coordinats2 = []
                                if k == 0 or k == 4:
                                    coordinats2.append(float(node['@lat']) + 0.00005)
                                    coordinats2.append(float(node['@lon']) + 0.00005)
                                if k == 1:
                                    coordinats2.append(float(node['@lat']) - 0.00005)
                                    coordinats2.append(float(node['@lon']) + 0.00005)
                                if k == 2:
                                    coordinats2.append(float(node['@lat']) - 0.00005)
                                    coordinats2.append(float(node['@lon']) - 0.00005)
                                if k == 3:
                                    coordinats2.append(float(node['@lat']) + 0.00005)
                                    coordinats2.append(float(node['@lon']) - 0.00005)
                                coordinats1.append(coordinats2)
                            print(coordinats1)
                            print(buildings[color][j][1])
                            print(color)
                            # Сохранение точек
                            polygons.append(coordinats1)
                            print()
    #Сохранение полигонов текущего цвета
    colorOfPolygon.append(polygons)

with open('Polygons.json', 'w') as file:
    file.write(json.dumps({"polygons": colorOfPolygon}))

end = time.time()
print(end)