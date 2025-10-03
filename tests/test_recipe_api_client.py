import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from recipe_api_client import RecipeAPIClient

@pytest.fixture
def api_client():
    return RecipeAPIClient()

def test_search_existing_recipe(api_client):
    result = api_client.search_recipe("Pizza")
    assert "Nazov:" in result
    assert "Postup:" in result
    assert "Odozva:" in result

def test_search_non_existing_recipe(api_client):
    result = api_client.search_recipe("NonExistingRecipeXYZ")
    assert "Recept sa nenasiel." in result
    assert "Odozva:" in result

def test_ivalid_url_has_response_time():
    client = RecipeAPIClient(base_url="http://invalid-url.com/")
    result = client.search_recipe("Pizza")
    assert "Odozva:" in result

