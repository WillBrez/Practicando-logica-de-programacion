figuras = {
        "triangulo": {
            "base": 2,
            "altura": 4
        },
        "cuadrado": {
            "lado": 2
        },
        "rectangulo": {
            "base": 2,
            "altura": 4
        }
    }

def poligono(pol):
    if pol == "triangulo":
        base = figuras["triangulo"]["base"]
        altura = figuras["triangulo"]["altura"]
        print(f"La base del poligono es: {(base*altura)/2}")

    elif pol == "cuadrado":
        lado = figuras["cuadrado"]["lado"]
        print(f"La base es: {lado**2}")    

    elif pol == "rectangulo":
        base = figuras["rectangulo"]["base"]
        altura = figuras["rectangulo"]["altura"]
        print(f"La base es: {base*altura}")
    else:
        print("Polígono no reconocido. Por favor, ingresa 'triangulo', 'cuadrado' o 'rectangulo'.")

pol = input("Ingresa un poligono: ").lower()
poligono(pol)
