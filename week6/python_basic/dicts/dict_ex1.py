#1
def sum_of_values(dct:dict) -> int:
    total = 0
    for val in dct.values:
        total += val
    return total


#2
def get_max_value(dct:dict) -> int:
    return max(dct.values())


#3
def count_chars(string:str) -> dict:
    count_dict = {}
    for char in string:
        count_dict[char] = count_dict.get(char,0) + 1
    return count_dict


#4
def invert_dictionary(dct:dict) -> dict:
    new_dct = {val:key for key,val in dct.items()}
    return new_dct


#5
def merge_dicts(dct1:dict,dct2:dict) -> dict:
    dct1.update(dct2)
    return dct1


#6
def filter_by_value(dct:dict, threshold:int) -> dict:
    filterd_dct = {key:val for key,val in dct.items() if val > threshold}
    return filterd_dct


#7
def group_by_first_letter(lst:list) -> dict:
    grouping_dct = {}
    for word in lst:
        grouping_dct[word[0]] = grouping_dct.get(word[0],[]) + [word]
    return grouping_dct


#8
def get_word_frequency(words:str) -> dict:
    frequency_dct = {}
    for word in words.split():
        frequency_dct[word] = frequency_dct.get(word,0) + 1
    return frequency_dct


#9
def get_common_keys(dct1:dict,dct2:dict) -> list:
    common_keys_lst = [key for key in dct1 if key in dct2]
    return common_keys_lst


#10
def get_most_frequent_value(dct:dict):
    value_counter_dct = {}
    for val in dct.values():
        value_counter_dct[val] = value_counter_dct.get(val,0) + 1
    return max(value_counter_dct, key=value_counter_dct.get)
    
