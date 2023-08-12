from tabulate import tabulate  # Tiene que instalar para correr el programa la libreria tabulate


class Except_Valor(Exception):
    pass


def calcular_cuota_mensual(valor_producto, interes, cuotas):
    if interes == 0 or cuotas == 1:
        return 0
    elif interes >= 0.12:
        raise Except_Valor("El valor supera los intereses óptimos")
    elif valor_producto == 0:
        raise Except_Valor("El valor del producto debe ser mayor a 0")
    elif cuotas < 0:
        raise Except_Valor("Las cuotas no pueden ser negativas")
    else:
        # Calcular la cuota mensual
        cuota_mes = (valor_producto * interes) / (1 - (1 + interes) ** (-cuotas))
        return calcular_intereses_antes_de_pagar(cuota_mes, valor_producto, cuotas)


def calcular_intereses_antes_de_pagar(cuota_mes, valor_prodcto, cuotas):
    total_intereses = ((cuota_mes * cuotas) - valor_prodcto)
    return total_intereses


def plan_amortizacion(cuota_mes, valor_producto, cuotas, interes):
    plan_amortizacion_datos = []
    saldo_restante = valor_producto

    for mes in range(1, cuotas + 1):
        if interes * 100 > 12:
            raise Except_Valor("EL VALOR ES MUY ALTO, AVARO")
        pago_interes = saldo_restante * interes
        abono_capital = cuota_mes - pago_interes
        saldo_restante -= abono_capital

        plan_amortizacion_datos.append({
            "Mes": mes,
            "Saldo Inicial": saldo_restante + abono_capital,
            "Pago Mensual": cuota_mes,
            "Intereses": pago_interes,
            "Capital": abono_capital,
            "Saldo Restante": saldo_restante
        })

    return plan_amortizacion_datos


def plan_amortizacion_pago_extra(cuota_mes, valor_producto, cuotas, interes, abono_extra, cuota_mes_extra):
    tabla_amortizacion = []
    saldo_restante = valor_producto
    mes = 0

    while saldo_restante > 0:
        mes += 1
        cuota_real = cuota_mes

        pago_interes = saldo_restante * interes
        abono_capital = cuota_real - pago_interes

        if abono_extra > cuota_real:
            raise Except_Valor("Error: el abono extra supera el saldo restante en el mes especificado")

        if mes == cuota_mes_extra:  # Aplicar el abono extra en el mes especificado
            cuota_real = abono_extra
            abono_capital = abono_extra - pago_interes

        if abono_capital > saldo_restante:
            abono_capital = saldo_restante

        saldo_restante -= abono_capital

        cuota_info = [mes,
                      round(saldo_restante + abono_capital),
                      round(cuota_real, 3),
                      round(pago_interes, 3),
                      round(abono_capital, 3),
                      round(saldo_restante, 3)]
        tabla_amortizacion.append(cuota_info)

    headers = ["Mes", "Saldo Inicial", "Pago Mensual", "Intereses", "Capital", "Saldo Restante"]
    print(tabulate(tabla_amortizacion, headers=headers, tablefmt="simple"))
    return tabla_amortizacion
