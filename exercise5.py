import collections
import random

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

a = random.sample(range(100), 11)
b = random.sample(range(30), 13)


print(str(a) + "\n" + str(b))
matches_list = check_for_matches(a,b)
print(check_for_duplicates(matches_list))
