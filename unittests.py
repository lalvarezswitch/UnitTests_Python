import unittest

class Mis_tests(unittest.TestCase):

    sumandoUno = 0
    sumandoDos = 0
    correr = True

    def setUp(self): #este sirve para poner precondiciones que se ejecutan antes de cada metodo"
        self.sumandoUno = 2
        self.sumandoDos = 2
        if self.sumandoUno * self.sumandoDos == 2000:
            self.correr = False

    def test_suma(self):
        self.assertEqual(self.sumandoUno+self.sumandoDos, 4)
        self.assertTrue(self.correr)

    def test_resta(self):
        self.assertTrue(self.sumandoUno-self.sumandoDos == 0)
        self.assertTrue(self.correr)

    def test_verificar_iguales(self):
        a = 5
        b = 4+1
        #verificar a==b
        self.assertEqual(a,b)

    def test_verificar_no_iguales(self):
        a=10
        b=5*3
        #verificar a!=b
        self.assertNotEqual(a,b,"a tiene que ser igual a b")

    def test_validar_si_verdadero(self):
        a = 2
        self.assertTrue(a==2, "Esperaba un true")

    def test_validar_si_falso(self):
        a = 5
        self.assertFalse(a==2+4, "Esperaba un false")

    def test_es_nulo(self):
        a = None
        self.assertIsNone(a, "Se espera que a sea none")
        #if a is None:
        #    print("a is none")

    def test_no_es_nulo(self):
        a = 9
        self.assertIsNotNone(a, "Se espera que a no sea none")

    def test_es(self):
        a = 5
        b = 5
        if a is b:
            print("Son iguales")
        else:
            print("No son iguales")

    def tearDown(self): #este sirve para poner postcondiciones que se ejecutan despues de cada metodo"
        print("Borrando datos...")
        print("Llevando la base de datos a su posicion inicial")
        print("Guardando resultado del caso")

if __name__ == '__main__':
    unittest.main()
