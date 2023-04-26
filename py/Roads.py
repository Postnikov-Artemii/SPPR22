import xmltodict
import json

RoadsName =['абрикос', 'алыч', 'ананас',
            'апельсин', 'базар', 'брусни',
            'винна', 'виноград', 'вишн',
            'груш', 'ежеви', 'земляни',
            'капуст', 'клубни', 'клюкв',
            'консерв', 'крыжовн', 'лимон',
            'малин', 'медо', 'миндаль',
            'мясн', 'огород', 'окун',
            'орех', 'пирог', 'плод',
            'родник', 'слив', 'смородин',
            'солё', 'тутовник', 'хмел',
            'черёмух', 'черешн', 'черник',
            'ябло', 'ягод', 'каштан']

# RoadsName = ['пархоменко']
with open('vlg.osm', 'r', encoding='utf-8') as fin:
    text = fin.read()
dct = xmltodict.parse(text)


roads=[]
for way in dct['osm']['way']:
    if 'tag' in way:
        tags = way['tag']
        name = 'noname'
        flag1 = False
        flag2 = False
        if isinstance(tags, list):
            for tag in tags:
                # Проверка совпадения тега
                if '@k' in tag and tag['@k'] == 'name':
                    for i in RoadsName:
                        if tag['@v'].lower().find(i) != -1:
                            flag1 = True
                if tag['@k'] == 'highway':
                    flag2 = True
                if flag1 == flag2 == True:
                    print(tag['@v'])
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
                    roads.append(coordinats1)
print(roads)
with open('Roads.json', 'w') as file:
    file.write(json.dumps({"roads": roads}))

