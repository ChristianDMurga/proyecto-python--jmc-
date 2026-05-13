import requests

# Configuración global
TOKEN = "3468641386934e6f9fbc4344d8347104"
HEADERS = {"X-Auth-Token": TOKEN}

def obtener_datos():
    """Obtiene los partidos generales del día."""
    url = "https://api.football-data.org/v4/matches"
    try:
        respuesta = requests.get(url, headers=HEADERS)
        if respuesta.status_code == 200:
            return respuesta.json()
        else:
            return f"Error: Información no encontrada (Status: {respuesta.status_code})"
    except requests.exceptions.RequestException as e:
        return f"Ocurrió un error de conexión: {e}"
