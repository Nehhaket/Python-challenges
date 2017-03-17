inpt = [3628800, 479001600, 6, 18]

for i in inpt:
    x = i
    y = 2
    while x%y == 0:
        if x == y:
            break
        x = x/y
        y += 1
    if x == y:
        print(i, "=", str(int(x)) + "!")
    else:
        print(i, " NONE")
