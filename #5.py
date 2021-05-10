def  smallest_multiple(n):
    i = n
    while i >= n:
        if (all((i % j) == 0  for j in range(1, n+1)) == True):
            return i
            break
        i += 1

x = int(input("Enter number of divisors: "))
y = smallest_multiple(x)
print("The smallest positive integer divisible by all numbers 1 through ", x, "is: ", y)
            
        
