def calcular_cuota_mensual(valor_prodcto, interes, cuotas):
    if interes == 0:
        return 0
    else:

        cuota_mes = (valor_prodcto * interes) / (1 - (1 + interes)**(-cuotas))
        return calcular_intereses_antes_de_pagar(cuota_mes, valor_prodcto, cuotas)

def calcular_intereses_antes_de_pagar(cuota_mes, valor_prodcto, cuotas):
    total_intereses = ((cuota_mes * cuotas) - valor_prodcto)
    return total_intereses
