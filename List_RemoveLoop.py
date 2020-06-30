healthy = ["kale chips", "brocoli"]
backpack = ["pizza", "frozen custard", "apple crisp", "kale chips"]

# healthy_backpack = [item.upper() for item in backpack if item in healthy]

healthy_backpack = []
for item in backpack:
    if item in healthy:
        healthy_backpack.append(item.upper())

print(healthy_backpack)
