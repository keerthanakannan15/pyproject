def prime(a):
    for i in range(0, len(a)):
        print("a[i] value is", a[i])
        if a[i] > 1:
            for x in range(2, a[i] // 2):
                print("x value is ", x)
                if (a[i] % x) == 0:
                    print(a[i], " not a prime")
                    break
            else:
                print(a[i], "prime no")
        else:
            print("no")


n =[2 ,3 ,6 ,7]
print(prime(n))