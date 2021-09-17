#Huy Kevin Nguyen
#PSID: 1346435


# 5.22

# part 1

oil_change_price = 35
tire_rotation_price = 19
car_wash_price = 7
car_wax_price = 12

print("Davy's auto shop services")
print("Oil change -- $",oil_change_price)
print("Tire rotation -- $",tire_rotation_price)
print("Car wash -- $",car_wash_price)
print("Car wax -- $",car_wax_price)

# part 2
service1 = input("Select first service:")
service2 = input("Select second service:")

#part3

if service1 == "Oil change":
    service1_price = oil_change_price
elif service1 == "Tire rotation":
    service1_price = tire_rotation_price
elif service1 == "Car wash":
    service1_price = car_wash_price
elif service1 == "Car wax":
    service1_price = car_wax_price
elif service1 == "-":
    service1_price = ' '
else:
    service1 = "Not valid service"

if service2 == "Oil change":
    service2_price = oil_change_price
elif service2 == "Tire rotation":
    service2_price = tire_rotation_price
elif service2 == "Car wash":
    service2_price = car_wash_price
elif service2 == "Car wax":
    service2_price = car_wax_price
elif service2 == "-":
    service2 = "No service"
else:
    service2 = "Not valid service"
print("Davy's auto shop invoice")
print("Service 1:", service1, ", $", service1_price)
print("Service 2:", service2, ", $", service2_price)
total = service1_price + service2_price
print("Total: $", total)

# part 4
if service1 == "Oil change":
    service1_price = oil_change_price
elif service1 == "Tire rotation":
    service1_price = tire_rotation_price
elif service1 == "Car wash":
    service1_price = car_wash_price
elif service1 == "Car wax":
    service1_price = car_wax_price
else:
    service1 = "Not valid service"

if service2 == "Oil change":
    service2_price = oil_change_price
elif service2 == "Tire rotation":
    service2_price = tire_rotation_price
elif service2 == "Car wash":
    service2_price = car_wash_price
elif service2 == "Car wax":
    service2_price = car_wax_price
else:
    service2 = "Not valid service"
print("Davy's auto shop invoice")
print("Service 1:", service1, ", $", service1_price)
print("Service 2:", service2, ", $", service2_price)
total = service1_price + service2_price
print("Total: $", total)

#doing part 4 wrong because i cant automate the printing of the omitted service to say "no service"
#unless i edit part 3 to go along with it as well 