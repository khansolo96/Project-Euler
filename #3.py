def prime(p):
    factors = 0
    for i in range(1, p+1):
        if ((p % i) == 0):
            factors += 1
    if factors == 2:
        return True
    else:
        return False
        
    
def largest_prime(n):
    primes = []
    for i in range(1, n+1):
        if (((n % i) == 0) and (prime(i) == True)):
            primes.append(i)
    return max(primes)

x = int(input("Enter number: "))
y = largest_prime(x)
print("The largest prime factor of ", x, "is", y)
