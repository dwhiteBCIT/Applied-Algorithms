sample_lst_sorted = [2, 4, 5, 6, 7, 9, 10]

sample_lst_unsorted = [2, 3, 6, 8, 7, 9, 10]

def is_sorted (lst):
    for num in range (len(lst) - 1):
        if lst[num] > lst[num + 1]:
            print ("no pass", lst[num], lst[num + 1])
            return False
        print (lst[num])
    print (lst[num + 1])
    return True

print ("ANSWER (sorted) = ", is_sorted(sample_lst_sorted))
print ("ANSWER (sorted) = ",is_sorted(sample_lst_unsorted))


sample_lst_adjacent = [2, 4, 6, 8, 9, 10, 10, 12]

sample_lst_no_adjacent = [2, 4, 6, 12, 9, 10, 12]

def has_adjacent_duplicate(lst):
    for num in range(len(lst) - 1):
        if lst[num] == lst[num + 1]:
            print ("Pass", lst[num], lst[num + 1])
            return True
        print (lst[num])
    print (lst[num + 1])
    return False


print ("ANSWER (adjacent)", has_adjacent_duplicate(sample_lst_adjacent))
print ("ANSWER (adjacent)", has_adjacent_duplicate(sample_lst_no_adjacent))