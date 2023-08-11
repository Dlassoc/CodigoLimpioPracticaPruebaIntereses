def calcular_cuota_mensual(valor_prodcto, interes, cuotas):
    if interes == 0 or cuotas == 1:
        return 0
    elif interes >= 0.12:
        return "NO ES POSIBLE"
    elif valor_prodcto == 0:
        return "El valor del producto debe ser mayor a 0"
    elif cuotas < 0:
        return "Las cuotas no pueden ser negativas"
    else:

        cuota_mes = (valor_prodcto * interes) / (1 - (1 + interes) ** (-cuotas))
        return calcular_intereses_antes_de_pagar(cuota_mes, valor_prodcto, cuotas)


def calcular_intereses_antes_de_pagar(cuota_mes, valor_prodcto, cuotas):
    total_intereses = ((cuota_mes * cuotas) - valor_prodcto)
    return total_intereses


def plan_amortizacion(cuota_mes, valor_producto, cuotas, interes):
    plan_amortizacion_datos = []
    saldo_restante = valor_producto

    for mes in range(1, cuotas + 1):
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

        if mes == cuota_mes_extra:  # Aplicar el abono extra en el mes especificado
            pago_interes = saldo_restante * interes
            abono_capital = abono_extra - pago_interes
        else:
            pago_interes = saldo_restante * interes
            abono_capital = cuota_real - pago_interes

        if abono_capital > saldo_restante:
            abono_capital = saldo_restante

        saldo_restante -= abono_capital

        cuota_info = {
            "Mes": mes,
            "Saldo Inicial": saldo_restante + abono_capital,
            "Pago Mensual": cuota_real,
            "Intereses": pago_interes,
            "Capital": abono_capital,
            "Saldo Restante": saldo_restante
        }
        tabla_amortizacion.append(cuota_info)
    print(tabla_amortizacion)
    return tabla_amortizacion
