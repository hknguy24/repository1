#Huy Kevin Nguyen
#PSID: 1346435


# 2.19

#part 1
cups_lemon = float(input("Enter amount of lemon juice (in cups):"))
cups_water = float(input("Enter amount of water (in cups):"))
cups_agave = float(input("Enter amount of agave nectar (in cups):"))

servings = float(input("How many servings does this make?"))

print("Lemonade ingredients - yields", '{:.2f}'.format(servings))
print('{:.2f}'.format(cups_lemon), "cups(s) lemon juice")
print('{:.2f}'.format(cups_water), "cups(s) water")
print('{:.2f}'.format(cups_agave), "cups(s) agave nectar")

# part 2

desired_servings = float(input("How many servings would you like to make?"))

multiply = desired_servings / servings
desired_cups_lemon = cups_lemon * multiply
desired_cups_water = cups_water * multiply
desired_cups_agave = cups_agave * multiply

print("Lemonade ingredients - yields", '{:.2f}'.format(desired_servings))
print('{:.2f}'.format(desired_cups_lemon), "cups(s) lemon juice")
print('{:.2f}'.format(desired_cups_water), "cups(s) water")
print('{:.2f}'.format(desired_cups_agave), "cups(s) agave nectar")

# part 3
# 16 cups = 1 gallon

desired_gallons_lemon = desired_cups_lemon / 16
desired_gallons_water = desired_cups_water / 16
desired_gallons_agave = desired_cups_agave / 16

print("Lemonade ingredients - yields", '{:.2f}'.format(desired_servings))
print('{:.2f}'.format(desired_gallons_lemon), "gallon(s) lemon juice")
print('{:.2f}'.format(desired_gallons_water), "gallon(s) water")
print('{:.2f}'.format(desired_gallons_agave), "gallon(s) agave nectar")
