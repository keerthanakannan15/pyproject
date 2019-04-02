a=3
if a > 1:
    for x in range(2, a // 2):
        print("x value is ", x)
        if (a % x) == 0:
            print(a, " not a prime")
            break
    else:
        print(a, "prime no")
else:
    print("no")