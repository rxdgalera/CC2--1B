import random

# converting section
lbs_to_kg = 0.453592
mi_to_km = 1.60934
fahrenheit_to_celsius = lambda f: (f - 32) * 5 / 9

# variables
lbs = 150
mi = 50
fahrenheit = 80
student_ages = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

# computing
kg = lbs * lbs_to_kg
km = mi * mi_to_km
celsius = fahrenheit_to_celsius(fahrenheit)
average_age = sum(student_ages) / len(student_ages)

# outputs
print("Pounds to Kilograms Conversion:")
print(f"{lbs} lbs = {kg} kg")

print("\nMiles to Kilometers Conversion:")
print(f"{mi} mi = {km} km")

print("\nFahrenheit to Celsius Conversion:")
print(f"{fahrenheit} °F = {celsius} °C")

print("\nAges of Students:")
for age in student_ages:
    print(age)
print(f"Average Age: {average_age:.2f}")

# fantasy story section
characters = ["Ichijo", "Natsumi", "Rei", "Arata", "Gyu"]
equipments = ["Sword", "Dagger", "Magic Book", "Pistol", "Bow"]
items = ["Restoration Potion", "Water Bottle", "Weapon Attachment", "Enhancement Potion", "Smoke Bomb"]
abilities = ["Split", "Circle of the Saint", "Beam of Heaven", "Minoan Shield", "Companion's Call"]

random_character = random.choice(characters)
random_equipment = random.choice(equipments)
random_item = random.choice(items)
random_ability = random.choice(abilities)

story = f"\nAn Isekai Story:\n{random_character} has been teleported to another dimension by a sorcerer. The sorcerer is in need of help from the evil wizard wrecking havock in their kingdom. They were given a weapon such as a {random_equipment}, along with items for their journey such as a {random_item}.As they proceed to their journey, they have gained abilities such {random_ability}, and they used those powers to help defeat the evil wizard.\n\nWill they ever succeed with this quest? What secrets will they encounter during this journey?"

print(story)
