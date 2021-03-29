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
            if name2 > name1:
                restaurants[r], restaurants[r+1] = restaurants[r+1], restaurants[r]
                swap = True           
        if not swap:
            break
    return restaurants[-1][0]

file1 = open('/home/tnameh/Downloads/03f4bfecd4-in.txt.clean.txt', 'r')
Lines = file1.readlines()
n = int(Lines[0])

def get_shortlisted_restaurant(n):
    restaurants = []
    for l in range(1, n+1):
        r = Lines[l].split(" ")
        r[-1] = int(r[-1])
        if len(restaurants):
            if (r[-1] > restaurants[-1][-1]):
                restaurants = []
                restaurants.append(r)
            elif (r[-1] == restaurants[-1][-1]):
                restaurants.append(r)
        else:
            restaurants.append(r)
    return get_restaurant(len(restaurants), restaurants)

# print(restaurants)

print(get_shortlisted_restaurant(n))