import requests


class Food:
    def get_meal_by_name(self, meal):
        if type(meal) == str:
            meals = requests.get('https://www.themealdb.com/api/json/v1/1/search.php?s='+meal)
            return meals.json()
        else:
            raise TypeError('Not string!')
