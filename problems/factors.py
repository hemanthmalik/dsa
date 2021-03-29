def factors(n):
    factors = [n]
    for i in range(1, n):
        if n % i == 0:
            factors.append(i)
    return factors

n = int(input("Enter number ----> "))
print(factors(n))