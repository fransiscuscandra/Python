
backpack = ["sword","rubber duck","pizza","parachute","sword"]

print(backpack.count("sword"))

if backpack.count("sword") < 5:
    backpack.append("sword")
print(backpack)

if "sword" in backpack:
    backpack.remove("sword")
print(backpack)
