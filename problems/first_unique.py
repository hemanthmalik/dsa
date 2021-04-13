l = [-1,10,2,0,-1,3,2,4,7,-1,7]
freq_dict = {}

for i in range(len(l)):
    curr_item = l[i]
    freq_item = freq_dict.get(curr_item)
    if freq_item:
        freq_dict[curr_item][1] += 1
    else:
        freq_dict[curr_item] = [i, 1]

first_unique = None
for k, v in freq_dict.items():
    if v[1] == 1:
        if first_unique:
            if v[1] < first_unique[1][1]:
                first_unique = (k, v)
        else:
            first_unique = (k, v)
print(first_unique[0])

