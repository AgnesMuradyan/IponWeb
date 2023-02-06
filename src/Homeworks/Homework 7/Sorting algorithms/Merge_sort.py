# class MergeSortError(Exception):
#     pass

class MergeSortError(Exception):
    pass


def merge(l, left, right):
    i = j = k = 0
    while i < len(right) and j < len(left):
        if right[i] < left[j]:
            l[k] = right[i]
            i += 1
        else:
            l[k] = left[j]
            j += 1
        k += 1
    while i < len(right):
        l[k] = right[i]
        i += 1
        k += 1

    while j < len(left):
        l[k] = left[j]
        j += 1
        k += 1


def merge_sort1(my_list):
    if len(my_list) > 1:
        mid = len(my_list) // 2
        right = my_list[:mid]
        left = my_list[mid:]
        merge_sort1(right)
        merge_sort1(left)
        merge(my_list, right, left)


# Merge sort 2
def merge2(l, start, mid, end):
    if len(l) > 1:
        left = l[start:mid + 1]
        right = l[mid + 1:end + 1]
        i = 0
        j = 0
        k = start
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                l[k] = left[i]
                i += 1
            else:
                l[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            l[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            l[k] = right[j]
            j += 1
            k += 1


def merge_sort2(l, start, end):
    if not isinstance(start, int) or not isinstance(end, int) or start < 0:
        raise MergeSortError
    if start < end:
        mid = (start + end) // 2
        merge_sort2(l, start, mid)
        merge_sort2(l, mid + 1, end)
        merge2(l, start, mid, end)


list0 = [1, 4, 1, 2, 7, 5, 2]
list1 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
list2 = []
list3 = [1]
list4 = [5, 2, 3, 1]
list5 = [3, -1]
merge_sort1(list0)
print(list0)
merge_sort1(list1)
print(list1)
merge_sort1(list2)
print(list2)
merge_sort1(list3)
print(list3)
merge_sort1(list4)
print(list4)
merge_sort1(list5)
print(list5)

print("*****************************************")
merge_sort2(list0, 0, 6)
print(list0)
merge_sort2(list1, 0, 9)
print(list1)
merge_sort2(list2, 0, 0)
print(list2)
merge_sort2(list3, 0, 0)
print(list3)
merge_sort2(list4, 0, 3)
print(list4)
merge_sort2(list5, 0, 2)
print(list5)