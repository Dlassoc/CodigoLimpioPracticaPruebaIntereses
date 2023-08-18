from Ejercicio import Cuota_mensual
def datos_cuota_mensual():
    print("Este programa le permite calcular la cuota mensual a pagar por una compra con tarjeta de credito")
    monto = float(input("Ingrese el precio del producto"))
    tasa = float(input("Ingrese la tasa de interés de la tarjeta"))
    cuotas = float(input("Numero de cuotas en que se va a diferir la compra "))
    print(Cuota_mensual.calcular_cuota_mensual(monto, tasa, cuotas))


datos_cuota_mensual()
