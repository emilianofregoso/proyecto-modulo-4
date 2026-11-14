# Proyecto Modulo 4 - Gestion de calificaciones

class Alumno:
    def __init__(self, nombre, matricula, calificaciones):
        self.nombre = nombre
        self.matricula = matricula
        self.calificaciones = calificaciones  # lista de enteros

    def promedio(self):
        return sum(self.calificaciones) / len(self.calificaciones)


alumnos = []   # lista de alumnos
matriz = []    # matriz: cada fila son las calificaciones de un alumno

n = int(input("Cuantos alumnos vas a registrar? "))
c = int(input("Cuantas calificaciones por alumno? "))

for i in range(n):
    print(f"\nAlumno {i + 1}")
    nombre = input("Nombre: ")
    matricula = input("Matricula: ")
    calificaciones = []
    for j in range(c):
        cal = int(input(f"Calificacion {j + 1}: "))
        calificaciones.append(cal)

    alumno = Alumno(nombre, matricula, calificaciones)
    alumnos.append(alumno)
    matriz.append(calificaciones)

# Promedio por alumno
print("\n--- Promedios por alumno ---")
for a in alumnos:
    print(f"{a.nombre} ({a.matricula}): {a.calificaciones} -> promedio {a.promedio():.2f}")

# Estadisticas del grupo
mayor = alumnos[0]
menor = alumnos[0]
suma = 0
for a in alumnos:
    if a.promedio() > mayor.promedio():
        mayor = a
    if a.promedio() < menor.promedio():
        menor = a
    suma += a.promedio()

print("\n--- Estadisticas del grupo ---")
print(f"Promedio mayor: {mayor.promedio():.2f} ({mayor.nombre})")
print(f"Promedio menor: {menor.promedio():.2f} ({menor.nombre})")
print(f"Promedio general: {suma / len(alumnos):.2f}")

# Promedio por cada calificacion usando la matriz
print("\n--- Promedio del grupo por calificacion ---")
for col in range(c):
    total = 0
    for fila in range(n):
        total += matriz[fila][col]
    print(f"Calificacion {col + 1}: {total / n:.2f}")
