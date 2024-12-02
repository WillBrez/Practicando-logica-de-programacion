import requests # pip install requests
from PIL import Image # pip install Pillow
from io import BytesIO
from math import gcd

url = input("Ingresa una URL: ")


#Respuesta = solicita
response = requests.get(url) 

if response.status_code == 200:
    img = Image.open(BytesIO(response.content))  #Representacion predeterminada de un objeto
    ancho, largo = img.size
    mcd = gcd(ancho, largo)
    if mcd == 1:
        print(f"{ancho}:{largo}")
    else:
        r1 = round(ancho / mcd)
        r2 = round(largo / mcd)
        print(f"{r1}:{r2}")     