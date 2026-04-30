import requests
import json
 
def obtener_datos():
    url = "https://api.football-data.org/v4/matches"
   
    headers = {
        "X-Auth-Token": "3468641386934e6f9fbc4344d8347104" 
    }
    try:
        respuesta = requests.get(url, headers=headers)
    
        if respuesta.status_code == 200:
            datos = respuesta.json()
            return datos
        else:
            return f"Información no encontrada"
    except requests.exceptions.RequestException as e:
        return f"Ocurrió un error de conexión: {e}"
 
if __name__ == "__main__":
    datos = obtener_datos()
    
    if isinstance(datos, dict):
        
        import json
        print(json.dumps(datos, indent=4))
    else:
        print(datos)
