import re

data = input()
pattern = r"([#|])(?P<name>[A-Za-z ]+)\1(?P<date>[0-9]{2}\/[0-9]{2}\/[0-9]{2})\1(?P<calories>[0-9]{1,4})\1"

matches = re.finditer(pattern,data)
total_calories = 0
food_data = []

for match in matches:
    object_dict = match.groupdict()
    food_data.append(object_dict)
    total_calories += int(object_dict["calories"])

days_left = int(total_calories / 2000)
print(f"You have food to last you for: {days_left} days!")


for food in food_data:

    print(f"Item: {food['name']}, Best before: {food['date']}, Nutrition: {food['calories']}")