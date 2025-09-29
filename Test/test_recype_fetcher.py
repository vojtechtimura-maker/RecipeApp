'''
Testovanie pomocou pytest,ktory musi byt nainstalovany pomocou
(pip install pytest)
subor by mal byt ulozeny v adresari Test/
pod nazov test_recype_fetcher.py
'''

import pytest
from recipe_fetcher import RecipeFetcher

@pytest.fixture
def recipe_file():#vytvorime testovaci subor
    test_file = "test_recipes.txt"
    with open(test_file,"w") as f:
        f.write("Nazov: test\nPostup: Uvar vodu a pridaj cestoviny.\n\n")
        f.write("Nazov: palacinky\nPostup: Zmiesaj muku,mlieko a vajcia, opec na panvici.\n")
    return test_file

def test_fetch_existing_recipe(recipe_file):
    fetcher = RecipeFetcher(recipe_file)
    result = fetcher.fetch_recipe("test")
    assert result == "Uvar vodu a pridaj cestoviny."

def test_fetch_non_existing_recipe(recipe_file):
    fetcher = RecipeFetcher(recipe_file)
    result = fetcher.fetch_recipe("pizza")
    assert result == "Recept sa nenasiel."

def test_file_not_found(recipe_file):
    fetcher = RecipeFetcher("neexistuje.txt")
    result = fetcher.fetch_recipe("test")
    assert result == "Subor sa nenasiel."

