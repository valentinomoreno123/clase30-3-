cant=float(input("Cantidad a invertir? "))
inter=float(input("Porcentaje anual que desea recibir? "))
años=int(input("Por cuantos años?"))
for a in range(años):
    cant *= 1 + inter / 100 
    print("Capital tras " + str(a+1) + " años: " + str(round(cant, 2)))