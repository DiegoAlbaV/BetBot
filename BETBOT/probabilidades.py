
def funcion_en_otro_archivo():
    print("FIN\n")

od1_str = input("Cuota equipo A: ")
od2_str = input("Cuota equipo B: ")
od3_str = input("Cuota DRAW: ")

od1 = float(od1_str)
od2 = float(od2_str)
od3 = float(od3_str)

probc1 = ((1/od1)*100)
probc2 = ((1/od2)*100)
probc3 = ((1/od3)*100)
probct = (probc1+probc2+probc3)



probr1 = ((100*probc1)/probct)
probr2 = ((100*probc2)/probct)
probr3 = ((100*probc3)/probct)


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

print("\n--- PROBABILIADAD DE LA CASA ---")

print("PROB LOCAL: {:.2f}".format(probc1))
print("PROB VISITA: {:.2f}".format(probc2))
print("PROB DRAW: {:.2f}".format(probc3))

print("\n--- PROBABILIDAD REAL ---")
print("PROB REAL LOCAL: {:.2f}".format(probr1))
print("PROB REAL VISITA: {:.2f}".format(probr2))
print("PROB REAL DRAW: {:.2f}".format(probr3))
