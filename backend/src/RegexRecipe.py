import sys
import re

pat = r'<ingredients>((.|\n)*?)</ingredients>'

data = open("Recipes.txt").read()

m = re.search(pat,data)
if not m:
    print("No ingredients found")
    print(sys.exit(1))

ingredients = m.group(1)

pat = r'<item\s.*?>(.*?)</item>'
all = re.findall(pat,ingredients)

for item in all:
    print(item)