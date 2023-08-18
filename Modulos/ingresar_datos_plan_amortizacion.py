from plan_amortizacion import plan_amortizacion_logica
def datos_amortizacion():
    print("Este programa le permite calcular la cuota mensual a pagar por una compra con tarjeta de credito")
    cuota_mes = int(input("Ingrese la cuota mensual"))
    valor_producto = float(input("Ingrese valor del producto"))
    cuotas = int(input("Ingrese numero de cuotas a pagar "))
    interes = float(input("Ingrese el interes que tiene que pagar en cada cuota")) #Interes se coloca en decimal, tipo 0.31 si es el 3.1 %
    print(plan_amortizacion_logica(cuota_mes, valor_producto, cuotas, interes))


datos_amortizacion()
