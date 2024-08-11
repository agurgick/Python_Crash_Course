# Enter code below
first_planet_input = input("enter the distance between the sun and the first plane in km: ")
second_planet_input = input("enter the distance between the sun and the second plane in km: ")

frist_planet = int(first_planet_input)
second_planet = int(second_planet_input)

distanc_km = second_planet - frist_planet
print(abs(distanc_km))