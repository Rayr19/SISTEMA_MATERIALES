print("-------------------------------------------------------")
print("++++++++++++++ 3D SERVICES S.A. ++++++++++++++")
print("+++++ SISTEMA DE CÁLCULO DE MATERIALES +++++")
print("-------------------------------------------------------")

cantidad_piezas = int(input("¿Cuantas piezas distintas componen el lote?: "))
costo_ml = float(input("Ingrese el costo de la resina por ml ($): "))

volumen_total_lote = 0.0

for i in range(cantidad_piezas):
    volumen_pieza = float(input(f"Ingrese el volumen de la pieza {i+1} (ml): "))
    volumen_total_lote += volumen_pieza # Acumulador

costo_total_lote = volumen_total_lote * costo_ml

print("\n--- Resumen de Producción ---")
print(f"total de piezas: {cantidad_piezas}")
print(f"volumen total requerido: {volumen_total_lote: 2f} ml")
print(f"costo total del lote: ${costo_total_lote: 2f}")

