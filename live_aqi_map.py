mport folium

# Create map centered on India
map = folium.Map(location=[22.5, 78.9], zoom_start=5)

# Sample city AQI data
cities = [
    ("Delhi", 28.6, 77.2, 210),
    ("Mumbai", 19.0, 72.8, 120),
    ("Bangalore", 12.9, 77.5, 85),
    ("Chennai", 13.0, 80.2, 95)
]

for city, lat, lon, aqi in cities:
    folium.Marker(
        [lat, lon],
        popup=f"{city} AQI: {aqi}"
    ).add_to(map)

map.save("live_aqi_map.html")
print("Live AQI Map saved as live_aqi_map.html")
