import re
#The village chelf has been taking oders from dragons all morning 
#but, the dragons' handwriting is terrible. 
#You've been hired to clean up the order list so the chelf can actually read it.
#
# You are given a messy string of dragon food orders:
# " fire-balls, smoke cakes, lava pies, molten-milk "
order_string = " fire-balls, smoke cakes, lava pies, molten-milk "
# Write a python program that: 
# 1. Strips extra spaces from the begining and en of the whole string. 
order_string = order_string.strip()

# 2. Splits the string into a list of individual food items ( they are separated by commas).
food_items = order_string.split(",")

# 3. Strips extra spaces from each item in the list. 

for i in range(len(food_items)):
    food_items[i] = food_items[i].strip()

# 4. Replaces any hyphens (-) with spaces so the name look nicer.
cleaned_food_items = []
for food_item in food_items:
    cleaned = food_item.replace("-", " ")
    cleaned = re.sub(r'\s+', ' ', cleaned)  # Replace multiple spaces with a single space
    cleaned_food_items.append(cleaned)

# 5. Prints the cleaned list of dragon foods. 
print(cleaned_food_items)
#
#Example output:
# ['fire balls', 'smoke cakes', 'lava pies', 'molten milk']