from api_conexion import obtener_datos
from procesamiento import extraer_datos_partidos
from graficas import generar_graficaygoles, graficar_clasificacionpremier, generar_grafica_pastel_liga

if __name__ == "__main__":
    print("Iniciando extracción de datos futbolísticos...")

    # 1. Obtener y mostrar datos crudos en consola
    data_partidos = obtener_datos()
    
    if isinstance(data_partidos, dict):
        # Mostrar resumen de partidos
        extraer_datos_partidos(data_partidos)

        # 2. Generar gráfica de goles (desde graficas.py)
        generar_graficaygoles()
    else:
        print(data_partidos)

    # 3. Generar gráfica de la Premier League (desde graficas.py)
    graficar_clasificacionpremier()

    # 4. Generar gráfica de La Liga (desde graficas.py)
    generar_grafica_pastel_liga()

    print("\nProceso finalizado con éxito.")
