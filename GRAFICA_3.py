def generar_grafica_pastel_liga():
   url = "https://api.football-data.org/v4/competitions/PD/standings"
   headers = {
       "X-Auth-Token": "3468641386934e6f9fbc4344d8347104"
   }
   try:
       respuesta = requests.get(url, headers=headers)
       if respuesta.status_code == 200:
           datos = respuesta.json()
           # Accedemos a la tabla de posiciones
           tabla = datos['standings'][0]['table']
           # Extraemos nombres y puntos
           equipos = [equipo['team']['shortName'] for equipo in tabla]
           puntos = [equipo['points'] for equipo in tabla]
           # Configuración de la gráfica
           plt.figure(figsize=(12, 9))
           # Función para mostrar los puntos reales en lugar de solo el porcentaje
           def fmt(pct, allvals):
               absolute = int(round(pct/100.*sum(allvals)))
               return f'{absolute} pts'
           # Crear el gráfico de pastel
           wedges, texts, autotexts = plt.pie(
               puntos,
               labels=equipos,
               autopct=lambda pct: fmt(pct, puntos),
               startangle=140,
               pctdistance=0.85, # Distancia de los números al centro
               colors=plt.cm.Paired.colors
           )
           # Mejorar la legibilidad de las etiquetas
           plt.setp(autotexts, size=9, weight="bold")
           plt.setp(texts, size=10)
           plt.title('Distribución de Puntos: La Liga Española', fontsize=15)
           plt.axis('equal')  # Asegura que el pastel sea circular
           plt.tight_layout()
           plt.savefig('clasificacion_laliga.png')
           plt.show()
       else:
           print(f"Error en la API: {respuesta.status_code}")
   except Exception as e:
       print(f"Ocurrió un error: {e}")
if __name__ == "__main__":
   generar_grafica_pastel_liga()
