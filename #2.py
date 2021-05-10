a = 1
b = 1
i = 0
sum = 0

while i < 4000000:
    i = a + b
    if ((i % 2) == 0):
        sum += i
    a = b
    b = i
print(sum)
