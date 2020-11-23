import unittest
from src.foodApi import Food


class FoodApiTest(unittest.TestCase):

    def setUp(self):
        self.temp = Food()

    def test_one(self):
        meal = self.temp.test()
        self.assertEqual(meal['meals'][0]['strMeal'], "Spicy Arrabiata Penne")

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
