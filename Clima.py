# Ciudades, días y semanas
ciudades = ['Atacames', 'Esmeraldas', 'Muisne']
dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
semanas = 2

# Crear matriz 3D: [ciudad][día][semana]
# Inicializamos con temperaturas de ejemplo
temperaturas = [[[0 for _ in range(semanas)] for _ in range(len(dias))] for _ in range(len(ciudades))]

# Ejemplo: asignar temperaturas manualmente (puedes automatizar o pedir al usuario)
temperaturas[0][0][0] = 28  # Atacames, Lunes, Semana 1
temperaturas[0][1][0] = 29
# ... llena el resto con datos ficticios o reales
# Para simplicidad asigno algunos valores:
import random
for c in range(len(ciudades)):
    for d in range(len(dias)):
        for s in range(semanas):
            temperaturas[c][d][s] = random.randint(25, 35)  # Temperaturas entre 25 y 35 grados

# Calcular promedio por ciudad y semana
for c in range(len(ciudades)):
    for s in range(semanas):
        suma = 0
        for d in range(len(dias)):
            suma += temperaturas[c][d][s]
        promedio = suma / len(dias)
        print(f"Promedio temperaturas en {ciudades[c]} durante la semana {s+1}: {promedio:.2f} °C")
