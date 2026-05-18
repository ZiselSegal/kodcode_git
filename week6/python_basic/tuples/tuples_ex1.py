#1
def sum_tuple_values(tup:tuple) -> int:
    total = 0
    for val in tup:
        if isinstance(val,int):
            total += val
        else:
            continue
    return total


#2
def find_tuple_max(tup:tuple) -> int:
    max_val = tup[0]
    for val in tup[1:]:
        if isinstance(val, int):
            if val > max_val:
                max_val = val
    return max_val


#3
def count_list_occurences(tup:tuple, occ) -> int:
    occ_count = 0
    for val in tup:
        if val == occ:
            occ_count += 1
    return occ_count


#4
def reverse_tup(tup:tuple) -> tuple:
    new_tup = tuple()
    for i in range(len(tup)-1,-1,-1):
        new_tup += (tup[i],)
    return new_tup


#5
def swap_pairs(tup:tuple) -> tuple:
    new_tup = tuple()
    i = 0
    while i < len(tup):
        new_tup += tup[i + 1], tup[i]
        i += 2
    return new_tup


#6
def find_min_max(tup:tuple) -> tuple:
    min = tup[0]
    max = tup[0]
    for val in tup:
        if val > max:
            max = val
        elif val < min:
            min = val
    return min,max


#7
def calc_distance(point1:tuple, point2:tuple):
    return ((point2[1] + point1[1]) **  2 + (point2[0] + point1[0]) ** 2) ** 0.5


#8
def sort_and_merge(tup1:tuple, tup2:tuple) -> tuple:
    sorted_1 = tuple_merge_sort(tup1)
    sorted_2 = tuple_merge_sort(tup2)
    return merge(sorted_1, sorted_2)


def tuple_merge_sort(tup:tuple) -> tuple:
    if len(tup) <= 1:
        return tup
    
    mid = len(tup) // 2
    left = tup[:mid]
    right = tup[mid:]

    left_sorted = tuple_merge_sort(left)
    right_sorted = tuple_merge_sort(right)

    return merge(left_sorted,right_sorted)


def merge(left_tup:tuple,right_tup:tuple) -> tuple:
    left_index = 0
    right_index = 0
    sorted_lst = []

    while left_index < len(left_tup) and right_index < len(right_tup):
        if left_tup[left_index] <= right_tup[right_index]:
            sorted_lst.append(left_tup[left_index])
            left_index += 1
        else:
            sorted_lst.append(right_tup[right_index])
            right_index += 1

    sorted_lst.extend(right_tup[right_index:])
    sorted_lst.extend(left_tup[left_index:])

    return tuple(sorted_lst)


#9
def count_occurences(tup:tuple) -> tuple:
    count_dict = {}
    for val in tup:
        count_dict[val] = count_dict.get(val,0) + 1
    count_tuple = tuple(((key,val) for key,val in count_dict.items()))
    return count_tuple


#10
def  rotate_tup(tup:tuple,k:int) -> tuple:
    k %= len(tup)
    return tup[-k:] + tup[:-k]