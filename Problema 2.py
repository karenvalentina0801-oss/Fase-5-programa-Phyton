Nombre_estudiante = print(f"Karen Valentina Martinez Ramirez")
Grupo_estudiante = print(f"Grupo 821")
Programa_estudiante = print(f"Ingieneria de sistemas")
Código_fuente = print(f"Código fuente: autoría propia")


Número_de_residentes = int(input("Digite el número de residentes: "))
Valor_cuota_mensual = float(input("Digite el valor de la cuota mensual:$ "))
Residentes_al_día=0
Residentes_Morosos=0
Valor_total_adeudado=0 
    
for i in range (Número_de_residentes):
    Pago_cuota = (input(f"número residente {i + 1}¿Realizo el pago? SI/NO: "))
    if Pago_cuota == "SI":
        Residentes_al_día += 1
    elif Pago_cuota == "NO":
        Residentes_Morosos += 1
        Valor_total_adeudado += Valor_cuota_mensual 
    
    
print(f"Total de residentes al día: {Residentes_al_día}")
print(f"Total de residentes morosos: {Residentes_Morosos}")
print(f"Valor total de la deuda:$ {Valor_total_adeudado}")  