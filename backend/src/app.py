import ingredient_parser

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

result1 = ingredient_parser.parse_ingredient("12 ounces lean ground beef, preferably 85 percent lean")
result2 = ingredient_parser.parse_ingredient("2x400g cans chopped tomatoes")
result3 = ingredient_parser.parse_ingredient("400ml crème fraîche")
result4 = ingredient_parser.parse_ingredient("1 celery stick, finely chopped")
result5 = ingredient_parser.parse_ingredient("500g beef mince")
result6 = ingredient_parser.parse_ingredient("1 1/3 fresh egg")
result7 = ingredient_parser.parse_ingredient("1-2 onion , finely chopped")
result8 = ingredient_parser.parse_ingredient("large handful basil leaves , torn (optional)")
print(f"Found results: \n {result1}")
print(f"Found results: \n {result2}")
print(f"Found results: \n {result3}")
print(f"Found results: \n {result4}")
print(f"Found results: \n {result5}")
print(f"Found results: \n {result6}")
print(f"Found results: \n {result7}")
print(f"Found results: \n {result8}")