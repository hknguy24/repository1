#Huy Kevin Nguyen
#PSID: 1346435

print("Birthday Calculator")

print("Current day")

current_month = int(input("Enter the current month:"))
print("Month:", current_month)

current_day = int(input("Enter the current day:"))
print("Day:", current_day)

current_year = int(input("Enter the current year:"))
print("Year:", current_year)

print("Birthday")

birth_month = int(input("Enter your birth month:"))
print("Month:", birth_month)

birth_day = int(input("Enter your birth day:"))
print("Day:", birth_day)

birth_year = int(input("Enter your birth year:"))
print("Year:", birth_year)

difference_years = current_year - birth_year

if current_month > birth_month:
    age = difference_years
elif current_month == birth_month:
    if current_day >= birth_day:
        age = difference_years
    else:
        age = difference_years - 1
elif current_month < birth_month:
    age = difference_years - 1

print("You are", age, "years old.")
