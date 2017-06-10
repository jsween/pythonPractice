import collections

def check_for_duplicates(list):
    seen = set()
    uniq = [x for x in list if x not in seen and not seen.add(x)]
    return uniq


def check_for_matches(list1, list2):
    new_list = []
    for x in list1:
        for y in list2:
            if x == y:
                new_list.append(x)
    return new_list

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


#print(check_for_matches(a,b))
matches_list = check_for_matches(a,b)
print(check_for_duplicates(matches_list))
