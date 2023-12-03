import folium
import leafmap.foliumap as leafmap
from streamlit_folium import folium_static

m = leafmap.Map(height=600, center=[39.4948, -108.5492], zoom=12)
url = "D:/3CI TOPO/Web Mapping/Projet/Partie1/code/ikoko.tif"
url2 = "D:/3CI TOPO/Web Mapping/Projet/Partie1/code/ikk.tif"
m.split_map(url, url2)

folium_static(m)

#---------------------------
import leafmap.foliumap as leafmap
import streamlit as st

# Créez la carte Leafmap
m = leafmap.Map(height=600, center=[39.4948, -108.5492], zoom=12)

# Ajoutez les images locales en tant que calques raster
url = "D:/3CI TOPO/Web Mapping/Projet/Partie1/code/ikk_cog.tif"
url2 = "D:/3CI TOPO/Web Mapping/Projet/Partie1/code/ikoko_cog.tif"
m.split_map(url, url2)

# Créez une page HTML temporaire pour afficher la carte Leafmap
st.components.v1.html(m.to_html(), height=600, scrolling=True)

#--------------------------------------------------------
import subprocess

def convert_to_cog(input_path, output_path):
    # Utilisez la commande rio cogeo create pour convertir le GeoTIFF en COG
    subprocess.run([
        "rio",
        "cogeo",
        "create",
        input_path,
        output_path,
        "--co",
        "overview_level=6"
    ])

if __name__ == "__main__":
    input_geotiff = "D:/3CI TOPO/Web Mapping/Projet/Partie1/code/ikoko.tif"
    output_cog = "D:/3CI TOPO/Web Mapping/Projet/Partie1/code/ikoko_cog.tif"

    convert_to_cog(input_geotiff, output_cog)

