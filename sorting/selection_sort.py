mylist = [1,4,2,53,234,6,45,-5,345,3]

def selection_sort(mylist):
    total_items = len(mylist)
    for i in range(total_items):
        selected_index = i
        for e in range(i, total_items):
            if mylist[selected_index] > mylist[e]:
                selected_index = e
        mylist[selected_index], mylist[i] = mylist[i], mylist[selected_index]
    return mylist

sorted_list = selection_sort(mylist)

print(sorted_list)