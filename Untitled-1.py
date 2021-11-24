def f(start, end):
    b = 0
    for i in range(start + 1 , end):
        if  i % 2 == 0:
            b += 1
    return b

print(f(1,10))
