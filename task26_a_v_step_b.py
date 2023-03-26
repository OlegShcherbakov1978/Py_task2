def step(a, b):
    if b == 1:
        return a
    elif b == 0:
        return 1
    return a * (step(a, (b-1)))


print(step(2, 6))
