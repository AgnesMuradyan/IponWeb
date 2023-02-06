# counting sort is only for real numbers
class CountingSortError(Exception):
    pass


#counting sort 1
def counting_sort(l: list) -> list:
    if not isinstance(l, list) or any(x < 0 for x in l):
        raise CountingSortError("Only positive numbers")
    if not l:
        return l
    k = max(l)
    """
    max with loop
    k = l[0]
    for i in l:
        if i > k:
            k = i
    """
    result = [0 for i in range(len(l))]
    count = [0 for i in range(k + 2)]
    # print(result)
    for i in range(len(l)):
        count[l[i] + 1] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in range(len(l)):
        result[count[l[i]]] = l[i]
        count[l[i]] += 1

    return result


#counting sort 2
def counting_sort2(l):
    if not isinstance(l, list) or any(x < 0 for x in l):
        raise CountingSortError("Only positive numbers")
    if not l:
        return l
    maxx = max(l)
    count = [0] * (maxx + 1)
    for i in l:
        count[i] += 1
    result = []
    for i in range(len(count)):
        for j in range(count[i]):
            result.append(i)
    return result


list0 = [1, 4, 1, 2, 7, 5, 2]
list1 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
list2 = []
list3 = [1]
list4 = [5, 2, 3, 1]
list5 = [3, -1]

print(counting_sort(list0))
print(counting_sort(list1))
print(counting_sort(list2))
print(counting_sort(list3))
print(counting_sort(list4))
# This will raise error
# print(counting_sort(list5))
print("*********************************************")
print(counting_sort2(list0))
print(counting_sort2(list1))
print(counting_sort2(list2))
print(counting_sort2(list3))
print(counting_sort2(list4))
# This will raise error
# print(counting_sort2(list5))
