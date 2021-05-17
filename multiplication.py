def multiplication(a, b):
    if a == 0 or b == 0:
        return 0
    return a + multiplication(a, b-1)


print(multiplication(3, 7))
print(multiplication(5, 5))
print(multiplication(0, 4))
