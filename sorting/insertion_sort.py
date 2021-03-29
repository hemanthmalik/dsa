mylist = [1,4,2,53,234,6,45,-5,345,3]

def insertion_sort(mylist):
    total_items = len(mylist)
    for i in range(1, total_items):
        selected_val, selected_index = mylist[i], i
        for e in range(i-1, -1, -1):
            if selected_val < mylist[e]:
                mylist[e+1],selected_index = mylist[e], e
        mylist[selected_index] = selected_val
    return mylist

def insertion_sort_while(mylist):
    total_items = len(mylist)
    for i in range(1, total_items):
        j = i - 1
        selected_val = mylist[i]
        while (j >= 0) and (selected_val < mylist[j]):
            mylist[j+1] = mylist[j]
            j -= 1
        mylist[j+1] = selected_val

    return mylist

sorted_list = insertion_sort_while(mylist)

print(sorted_list)