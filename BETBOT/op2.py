def funcion2():
    print("FIN\n")
    print("\n--- PORCENTAJE PARA INGRESAR ---")
 
bank = input("BANK INICIAL: ")
bank = float(bank)

odd = input("Bet Odd: ")
odd = float(odd)

step = 0.02

porcentaje = bank * step
A = porcentaje / odd
B = A * odd

montobet =  B / (odd-1) 

print("\nBANK INICIAL: {:.2f}$".format(bank))

print("\n--------SUBTOTAL---------")
print("GANANCIA: {:.2f}$".format(B))
print("GANANCIA TOTAL: {:.2f}$".format(B + montobet))

print("\n---------TOTAL----------")
print("MONTO A INGRESAR: {:.2f}$\n".format(montobet))