'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here

def get_restaurant(n, restaurants):
    for i in range(1, n):
        swap = False
        for r in range(n-i):
            restaurant1 = restaurants[r]
            name1, price1 = restaurant1[0], restaurant1[-1]
            restaurant2 = restaurants[r+1]
            name2, price2 = restaurant2[0], restaurant2[-1]
            if price2 < price1:
                restaurants[r], restaurants[r+1] = restaurants[r+1], restaurants[r]
                swap = True
            if (price2 == price1) and (name2 > name1):
                restaurants[r], restaurants[r+1] = restaurants[r+1], restaurants[r]
                swap = True
                    
        if not swap:
            break
    return restaurants[-1][0]

n = int(input())
restaurants = []
for _ in range(n):
    r = input().split(" ")
    r[1] = int(r[-1])
    restaurants.append(r)

print(get_restaurant(n, restaurants))

