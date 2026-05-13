import matplotlib.pyplot as plt
import requests
from api_conexion import HEADERS, obtener_datos

def generar_graficaygoles():   #"""Esta funcion sirve para graficar los partidos jugados al momento que se corre el programa y te da los goles en total en cada partido"""
    #"""Genera gráfica de barras de goles totales por partido (últimos 10)."""
    datos = obtener_datos()
    if not isinstance(datos, dict) or "matches" not in datos:
        print("No se pudieron obtener datos para la gráfica de goles.")
        return

    nombres_partidos = []
    total_goles = []

    for partido in datos["matches"][-10:]:
        home_g = partido["score"]["fullTime"]["home"]
        away_g = partido["score"]["fullTime"]["away"]

        if home_g is not None and away_g is not None:
            local = partido["homeTeam"]["shortName"] or partido["homeTeam"]["name"]
            visita = partido["awayTeam"]["shortName"] or partido["awayTeam"]["name"]
            nombres_partidos.append(f"{local} vs {visita}")
            total_goles.append(home_g + away_g)

    if not nombres_partidos:
        print("No se encontraron partidos con goles finalizados para graficar.")
        return

    plt.figure(figsize=(12, 6))
    plt.bar(nombres_partidos, total_goles, color='skyblue', edgecolor='navy')
    plt.title('Cantidad Total de Goles por Partido', fontsize=15, pad=20)
    plt.xticks(rotation=30, ha='right')
    plt.ylabel('Número de Goles')
    plt.tight_layout()
    plt.savefig('grafica_partidosygoles.png')
    print("Gráfica de goles guardada como 'grafica_partidosygoles.png'")
    plt.show()

def graficar_clasificacionpremier():   #"""Esta funcion te grafica la tabla de clasificacion de la Premier League"""
    #"""Genera gráfica de barras horizontal de la Premier League."""
    url = "https://api.football-data.org/v4/competitions/PL/standings"
    try:
        response = requests.get(url, headers=HEADERS)
        if response.status_code != 200:
            print(f"Error al consultar Premier League: {response.status_code}")
            return

        datos = response.json()
        tabla = datos['standings'][0]['table']
        equipos = [e['team']['shortName'] or e['team']['name'] for e in tabla]
        puntos = [e['points'] for e in tabla]

        equipos.reverse()
        puntos.reverse()

        plt.figure(figsize=(12, 10))
        plt.barh(equipos, puntos, color='teal', edgecolor='black')
        plt.title('Tabla de Clasificación - Premier League', fontsize=16, fontweight='bold')
        for i, v in enumerate(puntos):
            plt.text(v + 0.5, i, str(v), va='center', fontweight='bold')

        plt.tight_layout()
        plt.savefig('clasificacion_premier.png')
        print("Gráfica Premier guardada como 'clasificacion_premier.png'")
        plt.show()
    except Exception as e:
        print(f"Error en Premier League: {e}")
def generar_grafica_pastel_liga():  #"""Esta funcion sirve para graficar la tabla de clasificacion de la Liga Española en forma de pastel"""
    #"""Genera gráfico de pastel de la distribución de puntos en La Liga."""
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
            plt.savefig('clasificacion_laliga.png')
            print("Gráfica La Liga guardada como 'clasificacion_laliga.png'")
            plt.show()
        else:
            print(f"Error en La Liga: {respuesta.status_code}")
    except Exception as e:
        print(f"Error en La Liga: {e}")
