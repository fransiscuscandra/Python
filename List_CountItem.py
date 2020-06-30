backpack = [
    "sword",
    "rubber duck",
    "pizza",
    "parachute",
    "sword",
    "rubber duck",
    "slice of pizza",
    "parachute",
    "sword",
    "rubber duck",
    "slice of pizza",
    "parachute",
    "sword",
    "rubber duck",
    "slice of pizza",
    "parachute",
    "cannon",
    "laser cannon",
    "Canon 90D",
    "can of soup",
]

counts = [[item, backpack.count(item)] for item in set(backpack)]

print(counts)

[print(backpack.count(item), item) for item in set(backpack)]
