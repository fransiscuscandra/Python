healthy = ["kale chips", "brocoli"]
backpack = ["pizza", "frozen custard", "apple crisp", "kale chips"]

print(id(backpack))
backpack[:] = [item for item in backpack if item in healthy]
# we are going keep item for item in backpack if item in healthy
print(backpack)
print(id(backpack))
