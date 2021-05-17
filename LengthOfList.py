listExp = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def length(listExp):
    if not listExp:
        return 0
    else:
        return 1 + length(listExp[1:])


print(length(listExp))