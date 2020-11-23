import requests


class Food:
    def test(self):
        meals = requests.get('https://www.themealdb.com/api/json/v1/1/search.php?s=Arrabiata')
        return meals.json()
