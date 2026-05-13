def extraer_datos_partidos(datos):   """Esta funcion sirve para limpiar el codigo y tener los datos ordenados"""
    """Imprime en consola los resultados de los partidos."""
    print("\n--- RESULTADOS DE LOS PARTIDOS ---")
    partidos = datos.get("matches", [])
    if not partidos:
        print("No hay partidos programados para hoy.")
        return

    for idx, partido in enumerate(partidos, 1):
        local = partido.get("homeTeam", {}).get("name", "Local")
        visitante = partido.get("awayTeam", {}).get("name", "Visitante")
        goles_local = partido.get("score", {}).get("fullTime", {}).get("home", "-")
        goles_visitante = partido.get("score", {}).get("fullTime", {}).get("away", "-")
        print(f"{idx}. {local} {goles_local} - {goles_visitante} {visitante}")
