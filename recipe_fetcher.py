# class RecipeFetcher:
#     def __init__(self):
#         """neskor pridam dalsie udaje"""
#         pass
#
#     def fetch_recipe(self):
#         """
#         Zaklad receptu.
#
#         """
#         return
# print(RecipeFetcher().fetch_recipe())# vypise None

class RecipeFetcher:
    def __init__(self, filename = None):
        """Zadavame vstup co chceme hladat,nazov suboru s receptami"""

        if filename:
            self.filename = filename
        else:
            while True:
                file_input = input("Zadaj nazov suboru s receptami: ").strip()
                if file_input == "":
                    print("Nazov nesmie byt prazdny, skuste znova.")
                else:
                    self.filename = file_input
                    break

    def fetch_recipe(self, recipe_name = None):
        """
        Vyhlada recept podla nazvu v textovom subore kde bude;
        :Nazov:
        :Postup:
        """
        if not(recipe_name):
            while True:
                recipe_name = input("Zadaj nazov receptu: ").strip()
                if recipe_name.strip() == "":
                    print("Nazov nesmie byt prazdny, skuste znova.")
                elif recipe_name.isdigit():
                    print("Nazov nemoze byt cislo, skuste znova.")
                else:
                    break
        try:
            file = open(self.filename, "r") #otvorenie suboru len na citanie
            lines = file.readlines() #nacitanie riadkov
            file.close() #zatvorenie suboru
        except FileNotFoundError:
            return "Subor sa nenasiel."
        except Exception as e:
            return f"Nastala chyba pri citani suboru. {e}"


        recipes = {}
        name, instructions = None, None

        try:
            for line in lines:
                if line.startswith("Nazov:"): #ak zacina slovom nazov
                    name = line.replace("Nazov:", "").strip() # nahradime Nazov a prida sa do name
                elif line.startswith("Postup:"): #kontroluje ci zacina "Postup"
                    instructions = line.replace("Postup:", "").strip() #nahradi slovo postup a prida do instructions
                    if name: #ak mame uz meno receptu
                        recipes[name] = instructions #prida nazov receptu a postup
                        name, instructions = None, None
        except Exception as e:
            return f"Nastala chyba pri spracovani. {e}"
        return recipes.get(recipe_name, "Recept sa nenasiel.")


print(RecipeFetcher("recipes.txt").fetch_recipe("test"))
#Ak nebol vytvoreny subor recipes.txt vystup je zatial len "Subor sa nenasiel"




