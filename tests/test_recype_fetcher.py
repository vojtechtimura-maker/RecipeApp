'''
Testovanie pomocou pytest,ktory musi byt nainstalovany pomocou
(pip install pytest)
subor by mal byt ulozeny v adresari Test/
pod nazov test_recype_fetcher.py
'''

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from recipe_fetcher import RecipeFetcher

@pytest.fixture
def recipe_file(tmp_path):#vytvorime testovaci subor
    test_file = tmp_path /"test_recipes.txt"
    test_file.write_text(
    "Nazov: test\nPostup: Uvar vodu a pridaj cestoviny.\n\n"
    "Nazov: palacinky\nPostup: Zmiesaj muku,mlieko a vajcia, opec na panvici.\n")
    return str(test_file)

def test_fetch_existing_recipe(recipe_file):
    fetcher = RecipeFetcher(recipe_file)
    result = fetcher.fetch_recipe("test")
    assert result == "Uvar vodu a pridaj cestoviny."

def test_fetch_non_existing_recipe(recipe_file):
    fetcher = RecipeFetcher(recipe_file)
    result = fetcher.fetch_recipe("pizza")
    assert result == "Recept sa nenasiel."

def test_file_not_found():
    fetcher = RecipeFetcher("neexistuje.txt")
    result = fetcher.fetch_recipe("test")
    assert result == "Subor sa nenasiel."

