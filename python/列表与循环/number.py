for value in range(1, 5):
    print(value)
number = list(range(1, 6))
print(number)
even_number = list(range(2, 11, 2))
print(even_number)
squares = []
for value in range(1, 11):
    '''square = value**2
    squares.append(square)'''
    squares.append(value**2)

print(squares)

squares2 = [value**2 for value in range(1, 11)]
print(squares2)

jishu = [value*3 for value in range(1, 11)]
print(jishu)
