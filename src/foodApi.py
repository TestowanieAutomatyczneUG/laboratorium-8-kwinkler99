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