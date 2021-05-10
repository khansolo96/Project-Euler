def sum_3_5(n):
    sum = 0
    for i in range(1, n):
        if (((i % 3) == 0) or ((i % 5) == 0)):
            sum += i
    return sum

x = int(input("Enter number: "))
y = sum_3_5(x)
print("The sum of multiples of 3 and 5 below ", x, "is ", y)
