def insertion_sort(l: list) -> list:
    for i in range(1, len(l)):
        curr = l[i]
        j = i - 1
        while j > -1 and l[j] > curr:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = curr
    return l


list0 = [1, 4, 1, 2, 7, 5, 2]
list1 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
list2 = []
list3 = [1]
list4 = [5, 2, 3, 1]
list5 = [3, -1, 6, -10]

print(insertion_sort(list0))
print(insertion_sort(list1))
print(insertion_sort(list2))
print(insertion_sort(list3))
print(insertion_sort(list4))
print(insertion_sort(list5))
