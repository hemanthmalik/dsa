def gcd(n1, n2):
    smaller, larger = [n1, n2] if n1 < n2 else [n2, n1]
    rem = larger % smaller
    while rem:
        larger = smaller
        smaller = rem
        rem = larger % smaller
    return smaller
    # time complexity = O(log n)

def gcd1(n1, n2):
    fn = []
    for i in range(1, n1+1):
        if (n1 % i) == 0:
            fn.append(i)

    fm = []
    for j in range(1, n2+1):
        if (n2 % j) == 0:
            fm.append(j)
    
    ff = []
    for f in fn:
        if f in fm:
            ff.append(f)

    return ff[-1]
    # time complexity = O(n)

n1 = int(input('Enter 1st number -- '))
n2 = int(input('Enter 2nd number -- '))

def gcd2(n1, n2):
    for d in range(min(n1, n2), 0, -1):
        if ((n1 % d) == 0) and ((n2 % d) == 0):
            return d

def gcd3(n1, n2):
    if n1 < n2:
        n1, n2 = n2, n1
    if (n2 % n1) == 0:
        return n1
    else:
        diff = n1 - n2
        return gcd3(n2, diff)


print(gcd3(n1, n2))