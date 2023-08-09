def calcular_cuota_mensual(valor_prodcto, interes, cuotas):
    if interes == 0 or cuotas == 1:
        return 0
    elif interes >= 0.12 :
        return "NO ES POSIBLE"
    elif valor_prodcto == 0:
        return "El valor del producto debe ser mayor a 0"
    elif cuotas < 0:
        return "Las cuotas no pueden ser negativas"
    else:

        cuota_mes = (valor_prodcto * interes) / (1 - (1 + interes)**(-cuotas))
        return calcular_intereses_antes_de_pagar(cuota_mes, valor_prodcto, cuotas)

def calcular_intereses_antes_de_pagar(cuota_mes, valor_prodcto, cuotas):
    total_intereses = ((cuota_mes * cuotas) - valor_prodcto)
    return total_intereses
