def sum_to_one(n):
    if n == 0:
        return 0
    return n + sum_to_one(n-1)


print(sum_to_one(10))
