import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import random
from datetime import datetime, timedelta

# Fonction pour générer une date aléatoire dans la plage spécifiée
def random_date(start_date, end_date):
    return start_date + timedelta(
        days=random.randint(0, (end_date - start_date).days)
    )

# Chargez le fichier GeoJSON délimitant la frontière du Maroc
maroc_geojson_path = 'C:/Users/zineb/Desktop/HJ/venv/Maroc.geojson'
maroc_geojson = gpd.read_file(maroc_geojson_path)

# Fonction pour générer des coordonnées aléatoires au Maroc
def generate_coordinates(maroc_geojson):
    while True:
        lat, lon = round(random.uniform(maroc_geojson.bounds.miny[0], maroc_geojson.bounds.maxy[0]), 6), \
                   round(random.uniform(maroc_geojson.bounds.minx[0], maroc_geojson.bounds.maxx[0]), 6)
        point = Point(lon, lat)
        if maroc_geojson.geometry.contains(point).any():
            return lat, lon

# Génération de données pour 1000 points
num_points = 2000
coordinates = [generate_coordinates(maroc_geojson) for _ in range(num_points)]

# Génération de données pour chaque point
data_points = []
for i in range(num_points):
    lat, lon = coordinates[i]
    temperature = round(random.uniform(0, 50), 2)
    humidity = round(random.uniform(0, 100), 2)
    precipitation = round(random.uniform(0, 20), 2)

    # Conditions pour influencer la propriété 1 en fonction des variables météorologiques
    if temperature > 45 and precipitation < 1:
        prop1 = "Incendie de forêt"
    elif temperature < 5 and precipitation > 10 and humidity > 50:
        prop1 = "Chute de neige importante"
    elif temperature < 25 and precipitation > 15:
        prop1 = "Inondation"
    else:
        prop1 = "Accident de la route"

    point_data = {
        "Type d'Événement": prop1,
        "Gravité de l'événement": random.uniform(1, 50),
        "Variation Temporelle": random.uniform(-20, 20),
        "Date(jour0)": random_date(datetime(2023, 8, 1), datetime(2023, 8, 3)).strftime("%Y-%m-%d"),
        "humidityJour0(%)": humidity,
        "humidityJour-1(%)": random.uniform(0, 100),
        "humidityJour-2(%)": random.uniform(0, 100),
        "humidityJour-3(%)": random.uniform(0, 100),
        "humidityJour-4(%)": random.uniform(0, 100),
        "humidityJour-5(%)": random.uniform(0, 100),
        "humidityJour-6(%)": random.uniform(0, 100),
        "precipitationJour0(cm/m²)": precipitation,
        "precipitationJour-1(cm/m²)": random.uniform(0, 20),
        "precipitationJour-2(cm/m²)": random.uniform(0, 20),
        "precipitationJour-3(cm/m²)": random.uniform(0, 20),
        "precipitationJour-4(cm/m²)": random.uniform(0, 20),
        "precipitationJour-5(cm/m²)": random.uniform(0, 20),
        "precipitationJour-6(cm/m²)": random.uniform(0, 20),
        "temperatureJour0(°C)": temperature,
        "temperatureJour-1(°C)": random.uniform(0, 50),
        "temperatureJour-2(°C)": random.uniform(0, 50),
        "temperatureJour-3(°C)": random.uniform(0, 50),
        "temperatureJour-4(°C)": random.uniform(0, 50),
        "temperatureJour-5(°C)": random.uniform(0, 50),
        "temperatureJour-6(°C)": random.uniform(0, 50),
        "Geometry": gpd.points_from_xy([lon], [lat])[0]
    }
    data_points.append(point_data)

# Création d'un DataFrame pandas
df = pd.DataFrame(data_points)

# Création d'un GeoDataFrame avec GeoPandas
gdf = gpd.GeoDataFrame(df, geometry='Geometry')

# Filtrer les points pour qu'ils soient situés à l'intérieur de la frontière du Maroc
gdf = gdf[gdf.geometry.within(maroc_geojson.unary_union)]

# Enregistrez les données générées au format GeoParquet
gdf.to_parquet('C:/Users/zineb/Desktop/HJ/venv/DATA.parquet')

# Affichage des premières lignes du DataFrame
print(df.head())
