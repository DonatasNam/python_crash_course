pizzas = ["Pepperoni", "Vulcano", "Texas"]

friend_pizzas =pizzas[:]

pizzas.append("Napolitan")
friend_pizzas.append("Hawaiian")

print(f"My favorite pizzas are:")
for p in pizzas:
    print(p)

print(f"My friend's favorite pizzas are:")
for p in pizzas:
    print(p)


