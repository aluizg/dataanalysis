
# streamlit_app.py
import streamlit as st
import folium
from streamlit_folium import st_folium

m = folium.Map(location=[56.130, -106.35], zoom_start=6)
folium.Marker(
    location=[0, 0],
    popup="Título do Mapa",
    tooltip="Clique aqui"
).add_to(m)

st_folium(m, width=800, height=500)
