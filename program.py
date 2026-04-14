print("-------------------------------------------------------")
print("++++++++++++++ 3D SERVICES S.A. ++++++++++++++")
print("+++++ SISTEMA DE CÁLCULO DE MATERIALES +++++")
print("-------------------------------------------------------")

capacidad_maxima = 500.0

volumen = float(input("Ingrese el volumen de la pieza (ml): "))

if volumen > capacidad_maxima:
    print("ERROR La pieza excede la capacidad maxima de la impresora (500 ml)")
    print("Sugenrencia: Divida el modelo en partes mas pequeñas.")

else:
    costo_ml = float(input("Ingrese el costo de la resina por ml ($): "))
    costo_total = volumen * costo_ml
    print("Estado: ¡Aprobado para impresión!")
    print(f"El costo total de la impresión es: ${costo_total:.2f}")
    

