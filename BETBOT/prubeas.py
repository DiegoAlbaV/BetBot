
print("\n--- PROBABILIADAD ACTUAL by footystats ---")

# HOME MATRIZ
home = [
    [0, 0],
    [0, 0],
    [0, 0]
]

#RECIBIR DATOS
print("\nHOME STATS:")
 # OVERALL WIN
try:
    homeoverallwin_str = input("OVERALL WIN: ")
except ValueError:
    print("Error: Ingresa un número válido.")
# Modificar
home[0][0] = homeoverallwin_str

# OVERALL DRAW
try:
    homeoveralldraw_str = input("OVERALL DRAW: ")
except ValueError:
    print("Error: Ingresa un número válido.")
# Modificar
home[1][0] = homeoveralldraw_str

# OVERALL LOSS
try:
    homeoverallloss_str = input("OVERALL LOSS: ")
except ValueError:
    print("Error: Ingresa un número válido.")
# Modificar
home[2][0] = homeoverallloss_str

# HOME WIN
try:
    homewin_str = input("HOME WIN: ")
except ValueError:
    print("Error: Ingresa un número válido.")
# Modificar
home[0][1] = homewin_str

# HOME DRAW
try:
    homedraw_str = input("HOME DRAW: ")
except ValueError:
    print("Error: Ingresa un número válido.")
# Modificar
home[1][1] = homedraw_str

# HOME DRAW
try:
    homedraw_str = input("HOME LOSS: ")
except ValueError:
    print("Error: Ingresa un número válido.")
# Modificar
home[2][1] = homedraw_str

# AWAY MATRIZ
away = [
    [0, 0],
    [0, 0],
    [0, 0]
]

#RECIBIR DATOS

print("\nAWAY STATS:")

 # OVERALL WIN
try:
    awayoverallwin_str = input("OVERALL WIN: ")
except ValueError:
    print("Error: Ingresa un número válido.")
# Modificar
away[0][0] = awayoverallwin_str

# OVERALL DRAW
try:
    awayoveralldraw_str = input("OVERALL DRAW: ")
except ValueError:
    print("Error: Ingresa un número válido.")
# Modificar
away[1][0] = awayoveralldraw_str

# OVERALL LOSS
try:
    awayoverallloss_str = input("OVERALL LOSS: ")
except ValueError:
    print("Error: Ingresa un número válido.")
# Modificar
away[2][0] = awayoverallloss_str

# AWAY WIN
try:
    awaywin_str = input("HOME WIN: ")
except ValueError:
    print("Error: Ingresa un número válido.")
# Modificar
away[0][1] = awaywin_str

# AWAY DRAW
try:
    awaydraw_str = input("HOME DRAW: ")
except ValueError:
    print("Error: Ingresa un número válido.")
# Modificar
away[1][1] = awaydraw_str

# AWAY DRAW
try:
    awaydraw_str = input("HOME LOSS: ")
except ValueError:
    print("Error: Ingresa un número válido.")
# Modificar
away[2][1] = awaydraw_str



# MOSTRAR LA MATRIZ HOME
print("\nHOME STATS:")
print("OVERALL/HOME")
for fila in home:
    print(fila)

# MOSTRAR LA MATRIZ AWAY
print("\nAWAY STATS:")
print("OVERALL/HOME")
for fila in away:
    print(fila)


#PROBABILIDADES COMBINADAS
#LOCAL-VISITA

# Acceder a cuatro elementos específicos
elemento1 = home[0][1]
elemento2 = away[0][1]
elemento3 = home[2][1]
elemento4 = away[2][1]

elemento1 = float(elemento1)
elemento2 = float(elemento2)
elemento3 = float(elemento3)
elemento4 = float(elemento4)

# Calcular la suma de los cuatro elementos
suma_elementos = elemento1 + elemento2 + elemento3 + elemento4
print("La suma de los cuatro elementos es:", suma_elementos)

