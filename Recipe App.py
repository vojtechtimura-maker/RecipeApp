from recipe_fetcher import RecipeFetcher
from recipe_api_client import RecipeAPIClient


print("=== Recipe App ===")
print("1. Hladat recept v lokalnom subore")
print("2. Hladat cez API")
choice = input("Vyber moznost (1/2): ")

if choice == "1":
    fetcher = RecipeFetcher("recipes.txt")
    name = input(str("Zadaj nazov receptu:"))
    print(fetcher.fetch_recipe(name))
elif choice == "2":
    api_client = RecipeAPIClient()
    name = input(str("Zadaj nazov receptu:"))
    print(api_client.search_recipe(name))

else:
    print("Neplatna volba.")

