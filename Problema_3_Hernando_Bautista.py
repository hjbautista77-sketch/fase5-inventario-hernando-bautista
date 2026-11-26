# Fase 5 - Evaluación Final POA
# Estudiante: Hernando José Bautista Hernández
# Grupo: 213022_324
# Problema 3: Control de inventario y reabastecimiento


def calcular_cantidad_pedir(stock_actual, stock_minimo):
    "Calcula las unidades necesarias para alcanzar el stock mínimo."
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0



inventario = [
    ["A001", "Cuadernos", 5, 12],
    ["A002", "Lápices", 20, 15],
    ["A003", "Borradores", 8, 8],
    ["A004", "Marcadores", 0, 6],
    ["A005", "Carpetas", 4, 10]
]

print("INFORME DE REABASTECIMIENTO")
print()


for articulo in inventario:
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    cantidad = calcular_cantidad_pedir(stock_actual, stock_minimo)

    print(f"{nombre}: {cantidad} unidades a solicitar")