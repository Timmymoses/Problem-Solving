def merge_sorted_lists(list1, list2):
    merged_list = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list += [list1[i]]
            i += 1
        else:
            merged_list += [list2[j]]
            j += 1
    while i < len(list1):
        merged_list += [list1[i]]
        i += 1
    while j < len(list2):
        merged_list += [list2[j]]
        j += 1
    return merged_list

list1 = [1, 3, 4, 5]
list2 = [2, 6, 7, 8]

merged_list = merge_sorted_lists(list1, list2)
print(merged_list)