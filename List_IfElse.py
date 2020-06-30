healthy = ["pizza", "frozen custard", "apple crisp"]

print("chicken pot pie" in healthy)
print("pizza" in healthy)
print("frozen" in healthy)

if "pizzaa" in healthy:
    print("pizza", " found")
elif "brocolli" not in healthy:
    print("Need to buy ", "Brocolli")
else:
    print("Thank you")
