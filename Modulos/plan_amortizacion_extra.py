from tabulate import tabulate
from decimal import Decimal, ROUND_HALF_UP


def plan_amortizacion_pago_extra(cuota_mes: float, valor_producto: float, cuotas: int, interes: float,
                                 abono_extra: float, cuota_mes_extra: float):
    tabla_amortizacion = []
    saldo_restante = Decimal(str(valor_producto))

    mes = 0
    while saldo_restante > 0 and mes < cuotas:
        mes += 1
        cuota_real = Decimal(str(cuota_mes))

        pago_interes = saldo_restante * Decimal(str(interes))
        abono_capital = cuota_real - pago_interes

        if mes == cuota_mes_extra:
            if abono_extra >= cuota_real:
                abono_capital = abono_extra - pago_interes
            else:
                cuota_real = Decimal(str(abono_extra))
                abono_capital = abono_extra - pago_interes

        if abono_capital > saldo_restante:
            abono_capital = saldo_restante

        saldo_restante -= abono_capital

        cuota_info = [
            mes,
            "{:.2f}".format(saldo_restante.quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP)),
            "{:.2f}".format(cuota_real.quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP)),
            "{:.2f}".format(pago_interes.quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP)),
            "{:.2f}".format(abono_capital.quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP)),
            "{:.2f}".format(saldo_restante.quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP))
        ]
        tabla_amortizacion.append(cuota_info)

    headers = ["Mes", "Saldo Inicial", "Pago Mensual", "Intereses", "Capital", "Saldo Restante"]
    print(tabulate(tabla_amortizacion, headers=headers, tablefmt="simple"))
    return tabla_amortizacion
