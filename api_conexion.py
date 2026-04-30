import requests

def obtener_datos():
    """Descarga y retorna los datos JSON de la API."""
    url = "https://www.football-data.org/"
    respuesta = requests.get(url)
    datos = respuesta.json()
    return datos

if __name__ == "__main__":
    datos = obtener_datos()
    print(datos)
