import random
import unittest

import mycalc

class MyCalcTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("[имитируется бурная деятельность настройки]")
        print("v" * 30)

    @classmethod
    def tearDownClass(cls):
        print("^" * 30)
        print("[здесь мы всё подчистили типа]")

    def setUp(self):
        print(f"Подготовка к запуску {self.shortDescription()}")

    def tearDown(self):
        print(f"Очистка после прогона {self.id()}")
        print("---")

    def test_add(self):
        """ проверка сложения """
        self.assertEqual(mycalc.add(1, 2), 3)

    def test_mul(self):
        ''' проверка умножения '''
        self.assertEqual(mycalc.mul(3, 7), 21)

    def test_sub(self):
        """ проверка вычитания
        """
        self.assertEqual(mycalc.sub(4, 2), 2)

    def test_div(self):
        ''' проверка деления
        '''
        self.assertEqual(mycalc.div(16, 8), 2)
        with self.assertRaises(ZeroDivisionError):
            mycalc.div(1, 0)

    def test_sqrt(self):
        "проверка корня"
        self.assertAlmostEqual(
            mycalc.sqrt(9),
            3,
            delta=0.000000001
        )

if __name__ == "__main__":
    unittest.main()