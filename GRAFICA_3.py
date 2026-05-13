import matplotlib.pyplot as plt
import requests
from api_conexion import HEADERS

def generar_grafica_pastel_liga():  """Esta funcion sirve para graficar la tabla de clasificacion de la Liga Española en forma de pastel"""
    """Genera gráfico de pastel de la distribución de puntos en La Liga."""
    url = "https://api.football-data.org/v4/competitions/PD/standings"
    try:
        respuesta = requests.get(url, headers=HEADERS)
        if respuesta.status_code == 200:
            datos = respuesta.json()
            tabla = datos['standings'][0]['table']

            equipos = [equipo['team']['shortName'] for equipo in tabla]
            puntos = [equipo['points'] for equipo in tabla]

            plt.figure(figsize=(12, 9))
            plt.pie(
                puntos, 
                labels=equipos, 
                autopct=lambda pct: f'{int(round(pct/100.*sum(puntos)))} pts',
                startangle=140, 
                colors=plt.cm.Paired.colors
            )
            plt.title('Distribución de Puntos: La Liga Española', fontsize=15)
            plt.axis('equal')
            plt.tight_layout()
            print("Gráfica La Liga guardada como 'clasificacion_laliga.png'")
            plt.show()
        else:
            print(f"Error en La Liga: {respuesta.status_code}")
    except Exception as e:
        print(f"Error en La Liga: {e}")
