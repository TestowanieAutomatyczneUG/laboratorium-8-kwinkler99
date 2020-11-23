import requests


class Food:
    def get_meal_by_name(self, meal):
        if type(meal) == str:
            meals = requests.get('https://www.themealdb.com/api/json/v1/1/search.php?s='+meal)
            return meals.json()
        else:
            raise TypeError('Not string!')

    def get_list_by_first_letter(self, letter):
        if type(letter) == str:
            meals = requests.get('https://www.themealdb.com/api/json/v1/1/search.php?f='+letter)
            return meals.json()
        else:
            raise TypeError('Not string!')

    def get_meal_by_id(self, id):
        if type(id) == str:
            meals = requests.get('https://www.themealdb.com/api/json/v1/1/lookup.php?i='+id)
            return meals.json()
        else:
            raise TypeError('Not string!')

    def get_single_random_meal(self):
        meals = requests.get('https://www.themealdb.com/api/json/v1/1/random.php')
        return meals.json()

    def get_all_meal_categories(self):
        meals = requests.get('https://www.themealdb.com/api/json/v1/1/categories.php')
        return meals.json()

    def get_all_categories(self):
        meals = requests.get('https://www.themealdb.com/api/json/v1/1/list.php?c=list')
        return meals.json()

    def get_all_area(self):
        meals = requests.get('https://www.themealdb.com/api/json/v1/1/list.php?a=list')
        return meals.json()

    def get_add_ingredients(self):
        meals = requests.get('https://www.themealdb.com/api/json/v1/1/list.php?i=list')
        return meals.json()

    def get_filter_by_main_ingredient(self, ingredient):
        meals = requests.get('https://www.themealdb.com/api/json/v1/1/filter.php?i='+ingredient)
        return meals.json()

