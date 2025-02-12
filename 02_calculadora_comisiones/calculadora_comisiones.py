nombre = input("Dime tu nombre: ")
venta_mes = float(input("Dime cuando has vendido este mes: "))
comision = venta_mes * 13 / 100
comision = round(comision, 2)
print(f"Ok {nombre} este mes ganaste {comision} €")
