
def calcular_total(precio, cantidad):
    total = precio * cantidad
    return total

def main():
    precio = 10
    cantidad = 3

    resultado = calcular_total(precio, cantidad)

    print("El total de la compra es:", resultado)

main()
