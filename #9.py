for a in range(1, 999):
    for b in range(1, 999):
        for c in range(1, 999):
            if a < b and b < c and (a*a + b*b) == c*c and a + b + c == 1000:
                print(a, b, c)
                print("The product abc is = ", a*b*c)
                break

