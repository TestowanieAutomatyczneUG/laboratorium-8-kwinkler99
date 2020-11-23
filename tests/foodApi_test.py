import unittest
from src.foodApi import Food


class FoodApiTest(unittest.TestCase):

    def setUp(self):
        self.temp = Food()

    def test_by_name_one(self):
        meal = self.temp.get_meal_by_name("Arrabiata")
        self.assertEqual(meal['meals'][0]['strMeal'], "Spicy Arrabiata Penne")

    def test_by_name_two(self):
        meal = self.temp.get_meal_by_name("Frangipan")
        self.assertEqual(meal['meals'][0]['idMeal'], "52768")

    def test_by_empty_name(self):
        meal = self.temp.get_meal_by_name("")
        self.assertEqual(meal['meals'][0]['strMeal'], "Corba")

    def test_by_int_name(self):
        self.assertRaises(TypeError, self.temp.get_meal_by_name, 10)


    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
