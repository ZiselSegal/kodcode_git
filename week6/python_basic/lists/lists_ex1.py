#1
def sum_list_values(arr:list[int]) -> int:
    total = 0
    for val in arr:
        if isinstance(val,int):
            total += val
        else:
            continue
    return total


#2
def find_list_max(arr:list[int]) -> int:
    max_val = arr[0]
    for val in arr[1:]:
        if isinstance(val, int):
            if val > max_val:
                max_val = val
    return max_val


#3
def count_list_occurences(arr:list, occ) -> int:
    occ_count = 0
    for val in arr:
        if val == occ:
            occ_count += 1
    return occ_count


#4
def reverse_list(arr:list) -> list:
    left = 0
    right = len(arr) - 1
    while right > left:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

#5
def remove_duplicates(arr:list) -> list:
    unique_chars = set()
    uniqe_lst = []
    for val in arr:
        if val in unique_chars:
            continue
        else:
            unique_chars.add(val)
            uniqe_lst.append(val)
    return uniqe_lst


#5.2
def remove_duplicates_v2(arr: list) -> list:
    return list(dict.fromkeys(arr))


#6
def find_second_largest(arr: list[int]) -> int:
    max_num = arr[1]
    second_largest = None
    for val in arr:
        if val > max_num:
            second_largest = max_num
            max_num = val
        elif val < max_num:
            if second_largest == None or val > second_largest:
                second_largest = val


#7
def sort_lists(lst1,lst2):
    i = 0
    full_lst = lst1 + lst2
    while i < len(full_lst) - 1:
        if full_lst[i] > full_lst[i + 1]:
            full_lst[i], full_lst[i + 1] = full_lst[i + 1], full_lst[i]
            i -= 1
            continue
        i += 1
    return full_lst


#7.2
def sort_lists_v2(lst1,lst2):
    sorted_merged_lst = []
    list1_index = 0
    list2_index = 0
    while list1_index < len(lst1) and list2_index < len(lst2):
        if lst1[list1_index] <= lst2[list2_index]:
            sorted_merged_lst.append(lst1[list1_index])
            list1_index += 1
        elif lst1[list1_index] > lst2[list2_index]:
            sorted_merged_lst.append(lst2[list2_index])
            list2_index += 1
    if list1_index < len(lst1):
        sorted_merged_lst.extend(lst1[list1_index:])
    else:
        sorted_merged_lst.extend(lst2[list2_index:])
    return sorted_merged_lst



#8
def rotate_list(lst:list,k: int) -> list:
    k %= len(lst)
    for times in range(k):
        lst = [lst[-1]] + lst[:-1]
    return lst


#8.2
def  rotate_list_v2(lst:list,k: int) -> list:
    k %= len(lst)
    return lst[-k:] + lst[:-k]



