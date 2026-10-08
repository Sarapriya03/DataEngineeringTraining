cities = {"Hyderabad", "Mumbai", "Delhi", "Bangalore"}

print(cities)

cities.add("Pune")
print(cities)

cities.remove("Mumbai")
print(cities)

#Safer option to Remove
cities.discard("Chennai")
print(cities)

cities = {
    "Hyderabad",
    "Mumbai",
    "Delhi",
    "Hyderabad",
    "Mumbai"
}
unique_cities = set(cities)
print(unique_cities)