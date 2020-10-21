import requests
import pandas as pd
import json

url = "https://api.openweathermap.org/data/2.5/weather?q=Buenos+Aires&appid=0685c4e8066b577d449babf619cf4ab4&units=metric"
ciudades =["Lima","Buenos Aires","Madrid","La Plata","Santiago Del Estero"]

#MOSTRAR LA CIUDAD CON MAYOR TEMPERATURA Y LA DE MENOR TEMPERATURA 

def detectar_climas():
    temperaturas = []
    for ciudad in ciudades:
        ciudad_url = ciudad.replace(" ","+")
        r = requests.get(url.replace("Buenos+Aires",ciudad_url)).text
        temp = json.loads(r)['main']['temp']
        temperaturas.append(temp)
    return temperaturas

def main():
    temperaturas = detectar_climas()
    climas_ciudades = pd.DataFrame({'Ciudades':ciudades,'Temperaturas':temperaturas})
    print('TEMPERATURA MÁXIMA:')
    print(climas_ciudades.max())
    print('TEMPERATURA MÍNIMA:')
    print(climas_ciudades.min())

main()