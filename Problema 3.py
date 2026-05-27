Nombre_estudiante = print(f"Karen Valentina Martinez Ramirez")
Grupo_estudiante = print(f"Grupo 821")
Programa_estudiante = print(f"Ingieneria de sistemas")
Código_fuente = print(f"Código fuente: autoría propia")

valor_ventas_mañana = float(input("Digite el valor de las ventas de la mañana: "))
valor_ventas_tarde = float(input("Digite el valor de las ventas de la tarde: "))
valor_ventas_noche = float(input("Digite el valor de las ventas de la noche: "))

suma_ventas = valor_ventas_mañana + valor_ventas_tarde + valor_ventas_noche 

if suma_ventas >= 150000:
    mensaje = "Meta alcanzada"
elif suma_ventas < 150000:
    mensaje = "Meta no alcanzada"
    
print(f"El valor total de ventas del día fue: {suma_ventas}")  
print(f"Su mensaje fue: {mensaje}")  