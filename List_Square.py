# squares = []
# for i in range(10):
#    squares.append(i**2)
#    print(squares)

# print(squares)

# -------------This is same expression --------
square2 = [i ** 2 for i in range(10)]
print(square2)

squareEven = [i ** 2 for i in range(10) if i % 2 == 0]
print(squareEven)
