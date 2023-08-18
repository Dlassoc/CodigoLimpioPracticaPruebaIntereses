from plan_amortizacion_extra import plan_amortizacion_pago_extra
def datos_amortizacion_extra():
    print("Este programa le permite calcular la cuota mensual a pagar por una compra con tarjeta de credito")
    cuota_mes = float(input("Ingrese la cuota mensual"))
    valor_producto = float(input("Ingrese valor del producto"))
    cuotas = int(input("Ingrese numero de cuotas a pagar "))
    interes = float(input("Ingrese el interes que tiene que pagar en cada cuota")) #Interes se coloca en decimal, tipo 0.31 si es el 3.1 %
    abono_extra = int(input("Ingrese el abono extra que va a realizar"))
    cuota_mes_extra = int(input("Ingrese el mes en el que se hará el abono"))
    print(plan_amortizacion_pago_extra(cuota_mes, valor_producto, cuotas, interes,abono_extra, cuota_mes_extra))


datos_amortizacion_extra()
