import api_conexion
def extraer_datos_partidos(datos):
    """Recorre la lista de partidos, extrae los nombres de los equipos 
   y con sus marcadores."""
    partidos = datos.get("matches", [])
    for idx, partido in enumerate(partidos, 1): # Recorre cada partido y o enumera (1, 2, 3...)
        local = partido.get("homeTeam", {}).get("name", "Local")
        visitante = partido.get("awayTeam", {}).get("name", "Visitante")

        goles_local = partido.get("score", {}).get("fullTime", {}).get("home", "-") # Accede a los goles del tiempo completo 
        goles_visitante = partido.get("score", {}).get("fullTime", {}).get("away", "-")
        print(f"{idx}. {local} {goles_local} - {goles_visitante} {visitante}")
 
if __name__ == "__main__":
    datos = obtener_datos()
    if datos:
        extraer_datos_partidos(datos)
    else:
        print("No se pudieron obtener los datos.")
