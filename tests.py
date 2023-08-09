import unittest
import Ejercicio


class MyTestCase(unittest.TestCase):

    def testPayment1(self):
        valor_prodcto = 200000
        interes = 0.031
        cuotas = 36
        valor_total_intereses = 134726.53
        resultado = Ejercicio.calcular_cuota_mensual(valor_prodcto, interes, cuotas)
        # Usar assertAlmostEqual para comparar valores flotantes con tolerancia
        self.assertAlmostEqual(valor_total_intereses, resultado, places=2)  # places indica la cantidad de decimales a comparar

    def testPayment2(self):
        valor_prodcto = 850000
        interes = 0.034
        cuotas = 24
        valor_total_intereses = 407059.97
        resultado = Ejercicio.calcular_cuota_mensual(valor_prodcto, interes, cuotas)
        # Usar assertAlmostEqual para comparar valores flotantes con tolerancia
        self.assertAlmostEqual(valor_total_intereses, resultado, places=2)  # places indica la cantidad de decimales a comparar


    def testPayment3(self):
        valor_prodcto = 480000
        interes = 0
        cuotas = 48
        valor_total_intereses = 0
        resultado = Ejercicio.calcular_cuota_mensual(valor_prodcto, interes, cuotas)
        # Usar assertAlmostEqual para comparar valores flotantes con tolerancia
        self.assertAlmostEqual(valor_total_intereses, resultado, places=2)  # places indica la cantidad de decimales a comparar

    def testPayment4(self):
        valor_prodcto = 480000
        interes = 0.125
        cuotas = 48
        valor_total_intereses = "NO ES POSIBLE"
        resultado = Ejercicio.calcular_cuota_mensual(valor_prodcto, interes, cuotas)

        # Verificar si el resultado es igual a "NO ES POSIBLE" o 0
        self.assertEqual(valor_total_intereses, resultado)


    def testPayment5(self):
        valor_prodcto = 0
        interes = 0.024
        cuotas = 60
        valor_total_intereses =  "El valor del producto debe ser mayor a 0"
        resultado = Ejercicio.calcular_cuota_mensual(valor_prodcto, interes, cuotas)

        self.assertEqual(valor_total_intereses, resultado)


    def testPayment6(self):
        valor_prodcto = 50000
        interes = 0.01
        cuotas = -10
        valor_total_intereses =  "Las cuotas no pueden ser negativas"
        resultado = Ejercicio.calcular_cuota_mensual(valor_prodcto, interes, cuotas)

        self.assertEqual(valor_total_intereses, resultado)

    def test_plan_amortizacion(self):
        cuota_mes = 9297.96
        valor_producto = 200000
        cuotas = 36
        interes = 0.031
        plan = Ejercicio.plan_amortizacion(cuota_mes, valor_producto, cuotas, interes)
        self.assertEqual(len(plan), cuotas)

    def test_plan_amortizacion_2(self):
        cuota_mes = 10000
        valor_producto = 480000
        cuotas = 48
        interes = 0
        plan = Ejercicio.plan_amortizacion(cuota_mes, valor_producto, cuotas, interes)
        self.assertEqual(len(plan), cuotas)


    def test_plan_amortizacion_extra(self):
        cuota_mes = 9297.96
        valor_producto = 480000
        cuotas = 27
        interes = 0.031
        extra = 53000
        plan = Ejercicio.plan_amortizacion_pago_extra(cuota_mes, valor_producto, cuotas, interes, extra)
        self.assertEqual(len(plan), cuotas)#aa

if __name__ == '__main__':
    unittest.main()
