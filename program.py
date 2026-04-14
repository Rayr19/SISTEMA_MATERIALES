print("-------------------------------------------------------")
print("++++++++++++++ 3D SERVICES S.A. ++++++++++++++")
print("+++++ SISTEMA DE CÁLCULO DE MATERIALES +++++")
print("-------------------------------------------------------")

cantidad_piezas = int(input("¿Cuantas piezas distintas componen el lote?: "))
costo_ml = float(input("Ingrese el costo de la resina por ml ($): "))

volumen_total_lote = 0.0

for i in range(cantidad_piezas):
    volumen_pieza = float(input(f"Ingrese el volumen de la pieza {i+1} (ml): "))
    
    if volumen_pieza < 0:
        print("¡ERROR! El volumen no puede ser negativo. Saltando esta pieza")
        continue    

    if volumen_pieza > 500:
        print(f"¡ADVERTENCIA! La pieza {i+1} excede los 500ml. Se omitira del lote")
        continue

    volumen_total_lote += volumen_pieza 

costo_total_lote = volumen_total_lote * costo_ml

print("\n--- Resumen de Producción ---")
print(f"Total de piezas solicitadas: {cantidad_piezas}")
print(f"Volumen total aprobado: {volumen_total_lote:.2f} ml")
print(f"Costo total del lote: ${costo_total_lote:.2f}")