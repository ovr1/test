import mygame
import unittest

class MyGameTest(unittest.TestCase):
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

    def validate_board(self):
        """ проверять формат вывода (булевый) """
        self.assertTrue(1)

