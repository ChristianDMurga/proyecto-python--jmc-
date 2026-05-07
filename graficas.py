import matplotlib.pyplot as plt
import api_conexion
def generar_graficaygoles():
    datos = obtener_datos_con_goles()
    if not datos or "matches" not in datos:
        print("No se pudieron obtener datos.")
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
        print("No se encontraron partidos con goles numéricos.")
        return
 
    plt.figure(figsize=(12, 6))
    plt.bar(nombres_partidos, total_goles, color='skyblue', edgecolor='navy')
    plt.title('Cantidad Total de Goles por Partido', fontsize=15, pad=20)
    plt.xlabel('Partidos', fontsize=12)
    plt.ylabel('Número de Goles ', fontsize=12)
    plt.xticks(rotation=30, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('grafica_partidosygoles.png')
    plt.show()
 
 
def graficar_clasificacionpremier():
 
    url = "https://api.football-data.org/v4/competitions/PL/standings"
    headers = {"X-Auth-Token": "3468641386934e6f9fbc4344d8347104"}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Error al consultar la API: {response.status_code}")
            return
        datos = response.json()
        tabla = datos['standings'][0]['table']
        equipos = []
        puntos = []
 
        for entrada in tabla:
            nombre = entrada['team']['shortName'] or entrada['team']['name']
            pts = entrada['points']
            equipos.append(nombre)
            puntos.append(pts)
        equipos.reverse()
        puntos.reverse()
 
      
        plt.figure(figsize=(12, 10))
        barras = plt.barh(equipos, puntos, color='teal', edgecolor='black')
        plt.title('Tabla de Clasificación - Premier League', fontsize=16, fontweight='bold', pad=20)
        plt.xlabel('Puntos Totales', fontsize=12)
        plt.ylabel('Equipos', fontsize=12)
        for i, v in enumerate(puntos):
            plt.text(v + 0.5, i, str(v), color='black', va='center', fontweight='bold')
 
        plt.grid(axis='x', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.savefig('clasificacion_premier.png')
        plt.show()
 
    except Exception as e:
        print(f"Ocurrió un error: {e}")
if __name__ == "__main__":
    generar_graficaygoles()
    graficar_clasificacionpremier()
