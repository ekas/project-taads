import ingredient_parser

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

ingredients = ["12 ounces lean ground beef, preferably 85 percent lean", "2x400g cans chopped tomatoes", "400ml crème fraîche",
               "1 celery stick, finely chopped", "500g beef mince", "1 1/3 fresh egg", "1-2 onion , finely chopped", "large handful basil leaves , torn (optional)"]

extracted_ingredients = []

for ingredient in ingredients:
    extracted_ingredients.append(
        ingredient_parser.parse_ingredient(ingredient))

print(extracted_ingredients)
