import ingredient_parser

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# app = FastAPI()
#
#
# @app.get("/")
# async def root():
#     return parse_ingredient("12 ounces lean ground beef, preferably 85 percent lean")

# result = ingredient_parser.parse_ingredient("12 ounces lean ground beef, preferably 85 percent lean")
result = ingredient_parser.parse_ingredient("2 x 400g cans chopped tomatoes")
# result = ingredient_parser.parse_ingredient("2 rashers smoked streaky bacon")
# result = ingredient_parser.parse_ingredient("1 celery stick, finely chopped")
# result = ingredient_parser.parse_ingredient("500g beef mince")
# result = ingredient_parser.parse_ingredient("1 fresh egg")
print(f"Found results: \n {result}")