import folium

# mapa = folium.Map(location=[52.21, 21.0], zoom_start=6)
# folium. Marker(location=[52.21, 21.0], popup=f"").add_to(mapa)
# mapa.save('mapa.html')
def ger_cordinates(city_name:str)->list:
    import requests
    from bs4 import BeautifulSoup
    url=f"https://pl.wikipedia.org/wiki/Warszawa"
    response=requests.get(url).text
    response_html=BeautifulSoup(response,'html.parser')
    latitude=float(response_html.select(".latitude")[1].text.replace(",","."))
    longitude=float(response_html.select(".longitude")[1].text.replace(",","."))
    print(latitude,longitude)
    return [latitude,longitude]

ger_cordinates("Wałbrzych")