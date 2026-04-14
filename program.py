print("-------------------------------------------------------")
print("++++++++++++++ 3D SERVICES S.A. ++++++++++++++")
print("+++++ SISTEMA DE CÁLCULO DE MATERIALES +++++")
print("-------------------------------------------------------")

volumen = float(input("Ingrese el volumen de la pieza (ml): "))
costo_ml = float(input("Ingrese el costo de la resina por ml ($): "))

costo_total = volumen * costo_ml

print (f"\nEl costo total de manufactura es: ${costo_total:.2f}")
