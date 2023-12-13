
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

print("\n--- PROBABILIADAD DE LA CASA ---")

print("PROB LOCAL: {:.2f}".format(probc1))
print("PROB VISITA: {:.2f}".format(probc2))
print("PROB DRAW: {:.2f}".format(probc3))

print("\n--- PROBABILIDAD REAL ---")
print("PROB REAL LOCAL: {:.2f}".format(probr1))
print("PROB REAL VISITA: {:.2f}".format(probr2))
print("PROB REAL DRAW: {:.2f}".format(probr3))