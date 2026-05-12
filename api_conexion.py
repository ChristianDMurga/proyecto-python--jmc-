import requests
import json
import matplotlib.pyplot as plt

def obtener_datos():  """Esta funcion sirve para obtener los datos de la API mediante una llave que conseguimos registrandonos en la pagina del API."""
    url = "https://api.football-data.org/v4/matches"
   
    headers = {
        "X-Auth-Token": "3468641386934e6f9fbc4344d8347104" 
    }
    try:
        respuesta = requests.get(url, headers=headers)
    
        if respuesta.status_code == 200:
            datos = respuesta.json() #Convierte la respuesta de string a JSON
            return datos
        else:
            return f"Información no encontrada"
    except requests.exceptions.RequestException as e: # Captura errores de la red, como falta de internet o URL caída
        return f"Ocurrió un error de conexión: {e}"
 
if __name__ == "__main__":
    datos = obtener_datos()
    
    if isinstance(datos, dict): # Verifica si 'datos' es un diccionario
        
        import json
        print(json.dumps(datos, indent=4))
    else:
        print(datos)
