from collections import Counter

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

print(Counter(backpack))  # Create Dictionary
# Counter({'sword': 4, 'rubber duck': 4, 'parachute': 4,
# 'slice of pizza': 3, 'pizza': 1, 'cannon': 1, 'laser cannon': 1,
# 'Canon 90D': 1, 'can of soup': 1})
