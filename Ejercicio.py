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


def plan_amortizacion(cuota_mes, valor_prodcto, cuotas, interes):
    plan_amortizacion_datos = []
    saldo_restante = valor_prodcto

    for i in range (1, cuotas):
        pago_interes = saldo_restante * interes
        abono_capital = cuota_mes - pago_interes
        saldo_deuda = saldo_deuda - abono_capital

        plan_amortizacion.append({
            "Mes": mes,
            "Saldo Inicial": saldo_restante + capital,
            "Pago Mensual": cuota_mensual,
            "Intereses": interes,
            "Capital": capital,
            "Saldo Restante": saldo_restante
        })

        return plan_amortizacion