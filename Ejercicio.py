from tabulate import tabulate
from decimal import Decimal, ROUND_HALF_UP


class Except_Valor(Exception):
    pass


class Ejercicio:  # Agregar esta línea para definir la clase Ejercicio

    @staticmethod
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
            cuota_mes = (valor_producto * interes) / (1 - (1 + interes) ** (-cuotas))
            return Ejercicio.calcular_intereses_antes_de_pagar(cuota_mes, valor_producto, cuotas)

    @staticmethod
    def calcular_intereses_antes_de_pagar(cuota_mes, valor_producto, cuotas):
        total_intereses = (cuota_mes * cuotas) - valor_producto
        return total_intereses

    @staticmethod
    def plan_amortizacion(cuota_mes: float, valor_producto, cuotas, interes):
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

    @staticmethod
    def plan_amortizacion_pago_extra(cuota_mes: float, valor_producto: float, cuotas: int, interes: float,
                                     abono_extra: float, cuota_mes_extra: float):
        tabla_amortizacion = []
        saldo_restante = Decimal(str(valor_producto))  # Convertir a Decimal para precisión

        mes = 0
        while saldo_restante > 0:
            mes += 1
            cuota_real = Decimal(str(cuota_mes))  # Convertir a Decimal para precisión

            pago_interes = saldo_restante * Decimal(str(interes))
            abono_capital = cuota_real - pago_interes

            if mes == cuota_mes_extra:
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
