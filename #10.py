def prime(p):
    factors = 0
    for i in range(1, p+1):
        if ((p % i) == 0):
            factors += 1
    if factors == 2:
        return True
    else:
        return False

def sum_primes(n):
    sum = 0
    for i in range(1, n):
        if (prime(i) == True):
            sum += i
    return sum

x = int(input("Enter upper limit: "))
y = sum_primes(x)
print("The sum of all primes below ", x, " is: ", y)
        
