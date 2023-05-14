import json
from tkinter import *
import tkintermapview

#Создание окна
window = Tk()
window.title('TastyMap')
w = window.winfo_screenwidth()
h = window.winfo_screenheight()
window.geometry(f"{w}x{h}")

#Создание виджета
map_widget = tkintermapview.TkinterMapView(window, width=w, height=h, corner_radius=0)
map_widget.set_position(48.716, 44.510)
map_widget.set_zoom(16)
map_widget.pack(side=TOP)


with open('Polygons.json', 'r') as file:
    text=json.load(file)
print(text.items())
for Name, Pol in text.items():
    Polygons = Pol

print(isinstance(Polygons, list))
print(Polygons)

# Бордовый, Красный, Желтый, Зелёный, Тёмно зелёный
colors=["#800000", "#FF0000", "#FFFF00", "#00FF00", "#008000"]

#Покраска полигонов
for color in range(len(colors)):
    print(Polygons[color][0])
    for i in range(len(Polygons[color])):
        polygon_1 = map_widget.set_polygon(Polygons[color][i],
                                           fill_color=colors[color],
                                           outline_color=colors[color],
                                           border_width=4,
                                           # command=polygon_click,
                                           name=colors[color])

# Покраска дорог
with open('Roads.json', 'r') as file:
    text=json.load(file)
for name, coord in text.items():
    roads = coord
print(roads)
print(isinstance(roads, list))
road = [[[48.7238262, 44.5271429], [48.7231745, 44.5269409], [48.7226671, 44.5267594], [48.7221545, 44.5265761], [48.7215878, 44.5263538]], [[48.7190962, 44.5208323], [48.7192635, 44.5211847]]]
for i in range(len(roads)):
    try:
        road_1 = map_widget.set_path(roads[i], width=5)
    except:
        y=0
window.mainloop()