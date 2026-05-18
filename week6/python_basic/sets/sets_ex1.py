#1
def remove_dupes(lst:list) -> list:
    return list(set(lst))


#2
def count_unique(lst:list) -> int:
    unique_set = set(lst)
    counter = 0
    for val in unique_set:
        counter += 1
    return counter


#3
def get_common_elements(lst1:list,lst2:list) -> list:
    return list(set(lst1) & set(lst2))


#4
def elements_in_one(lst1:list,lst2:list) -> list:
    return list(set(lst1).symmetric_difference(set(lst2)))


#5
def is_subset(lst1:list,lst2:list) -> bool:
    return not bool(set(lst1).difference(set(lst2)))


#6
def is_unique_chars(string:str) -> bool:
    return len(set(string)) == len(string)


#7
def first_reapeated(lst:list) -> str:
    seen = set()
    for val in lst:
        if val in seen:
            return val
        seen.add(val)
    return None


#8
def count_distinct_words(words:str) -> int:
    return len(set(words.split()))


#9
def pair_sum_exists(lst: list, target: int) -> bool:
    seen = set()
    for num in lst:
        pair_value = target - num
        if pair_value in seen:
            return True
        seen.add(num)
    return False


#10
def find_symetric_diffrences(lst1:list,lst2:list) -> set:
    dupes = set(lst1) & set(lst2)
    full = set(lst1) | set(lst2)
    for dupe in dupes:
        full.discard(dupe)
    return full


#10.2
def find_symetric_diffrences_v2(lst1:list,lst2:list) -> set:
    lst1 = set(lst1)
    lst2 = set(lst2)
    uniques1 = lst1.difference(lst2)
    uniques2 = lst2.difference(lst1)
    return uniques1.union(uniques2)