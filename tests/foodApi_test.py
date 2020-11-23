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

    def test_by_first_letter_one(self):
        list = self.temp.get_list_by_first_letter("a")
        self.assertEqual(len(list['meals']), 2)

    def test_by_first_letter_two(self):
        list = self.temp.get_list_by_first_letter("d")
        self.assertEqual(len(list['meals']), 3)

    def test_by_first_letter_list(self):
        self.assertRaises(TypeError, self.temp.get_list_by_first_letter, ["a", "b"])

    def test_by_id_one(self):
        meal = self.temp.get_meal_by_id("52772")
        self.assertEqual(meal['meals'][0]['strCategory'], "Chicken")

    def test_by_id_two(self):
        meal = self.temp.get_meal_by_id("52768")
        self.assertEqual(meal['meals'][0]['strMeasure1'], "175g/6oz")

    def test_by_id_int(self):
        self.assertRaises(TypeError, self.temp.get_meal_by_id, 20)

    def test_single_random_meal_one(self):
        meal = self.temp.get_single_random_meal()
        self.assertEqual(len(meal['meals']), 1)

    def test_single_random_meal_two(self):
        self.assertRaises(TypeError, self.temp.get_single_random_meal, "test")

    def test_all_meal_categories(self):
        meal = self.temp.get_all_meal_categories()
        category = []
        for i in range(len(meal['categories'])):
            category.append(meal['categories'][i]['strCategory'])
        self.assertEqual(category,
                         [
                             "Beef",
                             "Chicken",
                             "Dessert",
                             "Lamb",
                             "Miscellaneous",
                             "Pasta",
                             "Pork",
                             "Seafood",
                             "Side",
                             "Starter",
                             "Vegan",
                             "Vegetarian",
                             "Breakfast",
                             "Goat"
                         ])

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
