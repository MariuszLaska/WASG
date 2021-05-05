import folium
from folium_jsbutton import JsButton
import webbrowser
import csv
import ipywidgets
from ipyleaflet import WidgetControl
from branca.element import Template, MacroElement
import copy


TOTAL_DEATHS = "total_deaths"
TOTAL_CASES  = "total_cases"
TOTAL_VACC   = "total_vaccinations"

COUNTRIES_CSV = "data/countries.csv"
COVID_CSV     = "data/covid.csv"


import menu
class CSVWorker:
    
    @staticmethod
    def get_world_csv():
        countries = []
        longitude = []
        lattitude = []
        with open(COUNTRIES_CSV, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                countries.append(row["Country"])
                longitude.append(row["Longitude"])
                lattitude.append(row["Latitude"])
                line_count += 1
        return countries, longitude, lattitude

    @staticmethod
    def get_values(value):
        countries = []
        deaths    = []

        with open(COVID_CSV, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            country = ""
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                if country != row['location']:
                    country = row['location']
                    deaths.append(row[value])
                    countries.append(row["location"])
                deaths[-1] = row[value]
                line_count += 1

        return countries, deaths



class Map:
    def __init__(self, center, zoom_start, factor):
        self.center = center
        self.zoom_start = zoom_start
        self.factor = factor

    def normalize_radius(self, values):
        values = [x for x in values if x != '']
        values = [float(x) for x in values]
        max_value = max(values)
        print(max_value)

        coefficient = 10000000 / max_value
        return coefficient

    def add_markers(self, map, countries, long, lat):
        c, d = CSVWorker().get_values(self.factor)
        new_d = copy.deepcopy(d)
        coeff = self.normalize_radius(new_d)
        for country, c_long, c_lat in zip(countries, long, lat):
            try:
                idx = c.index(country)
                print(country + ": " + d[idx])
                radius = (float(d[idx])) * coeff
                folium.Circle([float(c_long), float(c_lat)],popup=(c[idx] + "  " +d[idx]), radius = radius, fill=True).add_to(map)
            except Exception as e:
                 pass

    
    def generate(self):
        #Create the map
        my_map = folium.Map(location = self.center, zoom_start = self.zoom_start)
        c, ll, lt = CSVWorker.get_world_csv()
        self.add_markers(my_map, c, lt, ll)

        my_map.get_root().add_child(menu.macro)
        
        #Display the map
        my_map.save("map_" + self.factor + ".html")
        #webbrowser.open("map.html")



coords = [51.5074, 0.1278]
natalka_cords = [54.37663344912994, 18.608048954273528]

map1 = Map(center = coords, zoom_start = 5, factor=TOTAL_VACC)
map2 = Map(center = coords, zoom_start = 5, factor=TOTAL_DEATHS)
map3 = Map(center = coords, zoom_start = 5, factor=TOTAL_CASES)
map1.generate()
map2.generate()
map3.generate()

webbrowser.open("map_total_cases.html")