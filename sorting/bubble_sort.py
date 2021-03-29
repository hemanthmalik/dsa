mylist = [1,4,2,53,234,6,45,-5,345,3]

def bubble_sort(mylist):
    total_items = len(mylist)
    for i in range(1, total_items):
        for e in range(total_items-i):
            if mylist[e] > mylist[e+1]:
                mylist[e], mylist[e+1] = mylist[e+1], mylist[e]
    return mylist

sorted_list = bubble_sort(mylist)

print(sorted_list)