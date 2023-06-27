start_lst = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
my_set = set()

for i in range(len(start_lst)):
    for val in start_lst[i].values():
        my_set.add(val)
print(my_set)
