import unittest
import plan_amortizacion
import plan_amortizacion_extra
import Ejercicio

class MyTestCase(unittest.TestCase):

    def testPayment1(self):
        valor_prodcto = 200000
        interes = 0.031
        cuotas = 36
        valor_total_intereses = 134726.53
        resultado = Ejercicio.Cuota_mensual.calcular_cuota_mensual(valor_prodcto, interes, cuotas)
        # Usar assertAlmostEqual para comparar valores flotantes con tolerancia
        self.assertAlmostEqual(valor_total_intereses, resultado,
                               places=2)  # places indica la cantidad de decimales a comparar

    def testPayment2(self):
        valor_prodcto = 850000
        interes = 0.034
        cuotas = 24
        valor_total_intereses = 407059.97
        resultado = Ejercicio.Cuota_mensual.calcular_cuota_mensual(valor_prodcto, interes, cuotas)
        # Usar assertAlmostEqual para comparar valores flotantes con tolerancia
        self.assertAlmostEqual(valor_total_intereses, resultado,
                               places=2)  # places indica la cantidad de decimales a comparar

    def testPayment3(self):
        valor_prodcto = 480000
        interes = 0
        cuotas = 48
        valor_total_intereses = 0
        resultado = Ejercicio.Cuota_mensual.calcular_cuota_mensual(valor_prodcto, interes, cuotas)
        # Usar assertAlmostEqual para comparar valores flotantes con tolerancia
        self.assertAlmostEqual(valor_total_intereses, resultado,
                               places=2)  # places indica la cantidad de decimales a comparar

    def testPayment4(self):
        valor_producto = 480000
        interes = 0.125
        cuotas = 48
        try:
            resultado = Ejercicio.Cuota_mensual.calcular_cuota_mensual(valor_producto, interes, cuotas)
        except Ejercicio.Except_Valor as e:
            self.assertEqual(str(e), "El valor supera los intereses óptimos")

    def testPayment5(self):
        valor_producto = 0
        interes = 0.024
        cuotas = 60
        try:
            resultado = Ejercicio.Cuota_mensual.calcular_cuota_mensual(valor_producto, interes, cuotas)
        except Ejercicio.Except_Valor as e:
            self.assertEqual(str(e), "El valor del producto debe ser mayor a 0")

    def testPayment6(self):
        valor_producto = 50000
        interes = 0.01
        cuotas = -10
        try:
            resultado = Ejercicio.Cuota_mensual.calcular_cuota_mensual(valor_producto, interes, cuotas)
        except Ejercicio.Except_Valor as e:
            self.assertEqual(str(e), "Las cuotas no pueden ser negativas")

    def test_plan_amortizacion(self):
        cuota_mes = 9297.96
        valor_producto = 200000
        cuotas = 36
        interes = 0.031
        try:
            plan = plan_amortizacion.plan_amortizacion_logica(cuota_mes, valor_producto, cuotas, interes)
        except Ejercicio.Except_Valor as e:
           self.assertEqual(str(e), "Las cuotas no pueden ser negativas")

    def test_plan_amortizacion_2(self):
        cuota_mes = 10000
        valor_producto = 480000
        cuotas = 48
        interes = 0
        try:
            plan = plan_amortizacion.plan_amortizacion_logica(cuota_mes, valor_producto, cuotas, interes)
        except Ejercicio.Except_Valor as e:
            self.assertEqual(str(e), "Las cuotas no pueden ser negativas")

    def test_plan_amortizacion_extra_1(self):
        cuota_mes = 9297.96
        valor_producto = 200000
        cuotas = 27
        interes = 0.031
        extra = 53000
        mes_abono_extra = 5

        plan = plan_amortizacion_extra.plan_amortizacion_pago_extra(cuota_mes, valor_producto, cuotas, interes, extra, mes_abono_extra)
        self.assertEqual(len(plan), cuotas)


    def test_plan_amortizacion_extra_2(self):
        cuota_mes = 52377.50
        valor_producto = 850000.00
        cuotas = 23
        interes = 0.034
        extra = 90000
        mes_abono_extra = 5
        plan = plan_amortizacion_extra.plan_amortizacion_pago_extra(cuota_mes, valor_producto, cuotas, interes, extra, mes_abono_extra)
        self.assertEqual(len(plan), cuotas)


    def test_plan_amortizacion_extra_3(self):
        cuota_mes = 52377
        valor_producto = 850000
        cuotas = 23
        interes = 0.034
        extra = 90000
        mes_abono_extra = 10
        try:
            plan = plan_amortizacion_extra.plan_amortizacion_pago_extra(cuota_mes, valor_producto, cuotas, interes, extra, mes_abono_extra)

        except Ejercicio.Except_Valor as e:
            self.assertEqual(str(e), "El abono debe ser mayor a la cuota base ")

    def test_plan_amortizacion_extra_4(self):
        cuota_mes: float = 52377.50
        valor_producto = 850000.00
        cuotas = 23
        interes = 0.034
        extra = 90000
        mes_abono_extra = 22
        try:
            plan = plan_amortizacion_extra.plan_amortizacion_pago_extra(cuota_mes, valor_producto, cuotas, interes, extra, mes_abono_extra)

        except Ejercicio.Except_Valor as e:
            self.assertEqual(str(e), "El abono debe ser mayor a la cuota base ")


if __name__ == '__main__':
    unittest.main()
