Nombre_estudiante = print(f"Karen Valentina Martinez Ramirez")
Grupo_estudiante = print(f"Grupo 821")
Programa_estudiante = print(f"Ingieneria de sistemas")
Código_fuente = print(f"Código fuente: autoría propia")

Tipos = [1,2,3,4,5]
Tamaños = ["Pequeña","Mediana","Larga","Familiar","Extra Familiar"]
Porciones = [2,4,6,8,12]
Precios = [10000,15000,20000,25000,35000]

Total_pizzas_vendidas = 0
Total_ventas = 0
Total_porciones_vendidas = 0
Pizzas_por_tipo = [0,0,0,0,0]

print("SISTEMA DE VENTAS - PIZZERÍA")
print("")
Número_clientes = int(input("¿Cuántos clientes se atenderan?:"))

for Cliente in range(1,Número_clientes + 1):
    print(f"Atendiendo al cliente {Cliente}")

    print("Menú de pizzas:")
    print("1.Pequeña - 2 porciones $10000")
    print("2.Mediana - 4 porciones $15000")
    print("3.Larga - 6 porciones $20000")
    print("4.Familiar - 8 porciones $25000")
    print("5.Extra Familiar - 12 porciones $35000")
    print("0. Finalizar la orden")
    
    tipo = -1
    Total_cliente = 0
    while tipo!= 0:
       tipo = int(input("Seleccione la pizza (1-5) o (0) para finalizar:"))
    
       if tipo >= 1 and tipo <= 5:
           indice = tipo - 1
       
           Total_pizzas_vendidas += 1
           Pizzas_por_tipo [indice] += 1
           Total_porciones_vendidas += Porciones [indice]
           Total_cliente += Precios [indice] 
             
           print(f"Pizza {Tipos[indice]} Agregada - Precio: $ {Precios [indice]}")

print(f"Valor total a pagar por el cliente{Cliente}: {Total_cliente}")
Total_ventas += Total_cliente

print("RESUMEN FINAL DE VENTAS")

print(f"Total de pizzas vendidas:{Total_pizzas_vendidas} vendidas")
print(f"Total de porciones vendidas:{Total_porciones_vendidas}")
print(f"Valor total de ventas:$ {Total_ventas}")

print("Ventas por tipo de pizza:")
for i in range (5):
    print(f"Pizza {Tipos[i]}: {Pizzas_por_tipo[i]} vendidas")