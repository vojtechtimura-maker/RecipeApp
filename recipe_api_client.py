import requests
import time

class RecipeAPIClient: #Klient pre API,webova adresa
    def __init__(self, base_url="https://www.themealdb.com/api/json/v1/1/"):
        self.base_url = base_url

    def search_recipe(self, recipe_name):#bude vyhladavat recept
        start = time.time()
        result = ""
        try:
            url = f"{self.base_url}search.php?s={recipe_name}"
            response = requests.get(url)

            if response.status_code != 200:
                return f"Chyba API: {response.status_code}"
            else:
                data = response.json()
                if data["meals"] is None:
                    result =  "Recept sa nenasiel."
                else:
                    meal = data["meals"][0]
                    result = f"Nazov: {meal["strMeal"]}\nPostup: {meal["strInstructions"]}"

        except Exception as e:
            result =  f"Nastala chyba pri volani API: {e}"

        finally:
            elapsed = time.time() - start
            result += f"Odozva: {elapsed:.2f}s"

        return result


