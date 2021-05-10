def palindrome(a):
    if str(a) == (str(a)[::-1]):
        return True
    else:
        return False

def larpal(n):
    pal = []
    for i in range(10**(n-1), 10**n):
        for j in range(10**(n-1), 10**n):
            if ((palindrome(i*j) == True)):
                pal.append(i*j)
    return max(pal)

x = int(input("Enter number of digits in numbers to be multiplied: "))
y = larpal(x)
print("The largest palindrome made from the product of two ", x, "-digit numbers is: ", y)
