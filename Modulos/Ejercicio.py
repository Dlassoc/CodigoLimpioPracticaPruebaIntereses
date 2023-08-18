class Except_Valor(Exception):
    pass


class Cuota_mensual:

    @staticmethod
    def calcular_cuota_mensual(valor_producto, interes, cuotas):
        if interes == 0 or cuotas == 1:
            return 0
        elif interes / 100 > 0.12:
            return  Except_Valor("El valor del producto debe ser mayor a 0")
        elif cuotas < 0:
            raise Except_Valor("Las cuotas no pueden ser negativas")
        else:
            cuota_mes = (valor_producto * interes) / (1 - (1 + interes) ** (-cuotas))
            return round(Cuota_mensual.calcular_intereses_antes_de_pagar(cuota_mes, valor_producto, cuotas), 2)

    @staticmethod
    def calcular_intereses_antes_de_pagar(cuota_mes, valor_producto, cuotas):
        total_intereses = (cuota_mes * cuotas) - valor_producto
        return total_intereses

