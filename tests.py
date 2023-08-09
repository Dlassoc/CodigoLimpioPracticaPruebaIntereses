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
        interes = 0
        cuotas = 48
        valor_total_intereses = 0
        resultado = Ejercicio.calcular_cuota_mensual(valor_prodcto, interes, cuotas)
        # Usar assertAlmostEqual para comparar valores flotantes con tolerancia
        self.assertAlmostEqual(valor_total_intereses, resultado, places=2)  # places indica la cantidad de decimales a comparar

if __name__ == '__main__':
    unittest.main()
