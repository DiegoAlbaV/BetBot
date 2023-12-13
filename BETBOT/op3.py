def funcion3():
    print("FIN\n")

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
print("OVERALL/AWAY")
for fila in away:
    print(fila)

#PROBABILIDADES UNITARIAS
#LOCAL WIN
homewin = home[0][1]
awayloss = away[2][1]
homewin = float(homewin)
awayloss = float(awayloss)
homewin1 = (homewin+awayloss)
numero = 200
# Convertir la cadena a entero 
resultado = (int(homewin1) / numero)

#AWAY WIN
homeloss = home[2][1]
awaywin = away[0][1]
homeloss = float(homeloss)
awaywin = float(awaywin)
awaywin1 = (homeloss+awaywin)
numero = 200
# Convertir la cadena a entero 
resultado2 = (int(awaywin1) / numero)

#DRAW
awaydraw = away[1][1]
homedraw = home[1][1]
awaydraw = float(awaydraw)
homedraw = float(homedraw)
draw = (awaydraw+homedraw)
numero = 200
# Convertir la cadena a entero 
resultado3 = (int(draw) / numero)


#PROBABILIDADES COMBINADAS
#LOCAL-VISITA
homeaway = 100 - (resultado3 * 100)
#LOCAL-DO
homeDo = 100 - (resultado2 * 100)
#AWAY-DO
awayDo = 100 - (resultado * 100)


#IMPRIMIR PROBS ACTUALES
print("\n--- PROBABILIADADES ACTUAL by footystats ---")

print("LOCAL ML: {:.1f}%".format(resultado * 100))
print("VISITA ML: {:.1f}%".format(resultado2 * 100))
print("DRAW: {:.1f}%".format(resultado3 * 100))
print("VISITA/D.O: {:.1f}%".format(homeaway))
print("VISITA/D.O: {:.1f}%".format(homeDo))
print("VISITA/D.O: {:.1f}%".format(awayDo))


#IMPRIMIR PROBS GENERALES

#PROBABILIDADES UNITARIAS GENERALES
#LOCAL WIN
homewinov = home[0][0]
awaylossov = away[2][0]

homewinov = float(homewinov)
awaylossov = float(awaylossov)
homewin1ov = (homewinov+awaylossov)
numero = 200
# Convertir la cadena a entero 
resultadov = (int(homewin1ov) / numero)

#AWAY WIN
homelossov = home[2][0]
awaywinov = away[0][0]

homelossov = float(homelossov)
awaywinov = float(awaywinov)
awaywin1ov = (homelossov+awaywinov)
numero = 200
# Convertir la cadena a entero 
resultado2ov = (int(awaywin1ov) / numero)

#DRAW
awaydrawov = away[1][0]
homedrawov = home[1][0]

awaydrawov = float(awaydrawov)
homedrawov = float(homedrawov)
drawov = (awaydrawov+homedrawov)
numero = 200
# Convertir la cadena a entero 
resultado3ov = (int(drawov) / numero)


#PROBABILIDADES COMBINADAS
#LOCAL-VISITA
homeawayov = 100 - (resultado3ov * 100)
#LOCAL-DO
homeDov = 100 - (resultado2ov * 100)
#AWAY-DO
awayDov = 100 - (resultadov * 100)

print("\n--- PROBABILIADADES OVERALL by footystats ---")

print("LOCAL ML: {:.1f}%".format(resultadov * 100))
print("VISITA ML: {:.1f}%".format(resultado2ov * 100))
print("DRAW: {:.1f}%".format(resultado3ov * 100))
print("VISITA/D.O: {:.1f}%".format(homeawayov))
print("VISITA/D.O: {:.1f}%".format(homeDov))
print("VISITA/D.O: {:.1f}%".format(awayDov))