import collections
import math
import re

# Task 1    **********************************************************************************************

'''Տրված է թվաբանական պրոգրեսիայի առաջին և երկրորդ անդամները։ Տրված n֊ի
համար, վերադարձնել այդ պրոգրեսիայի n֊րդ անդամը։'''


def progression(x, y, n):
    return x + (n - 1) * (y - x)


# print(progression(2.5,3.5,5))


# Task 2    **********************************************************************************************
'''CodeMaster-ը նոր է վերադարձել գնումներից։ Նա սկանավորեց իր գնած ապրանքների
չեկը և ստացված շարանը տվեց Ratiorg֊ին՝ պարզելու գնված ապրանքների
ընդհանուր թիվը: Քանի որ Ratiorg-ը բոտ է, նա անպայման պատրաստվում է այն
ավտոմատացնել, ուստի նրան անհրաժեշտ է ծրագիր, որը կամփոփի բոլոր թվերը,
որոնք հայտնվում են տվյալ մուտքագրում:
Օգնեք Ratiorg-ին՝ գրելով ֆունկցիա, որը վերադարձնում է տվյալ inputString-ում
հայտնված թվերի գումարը։'''


def ratiorg(str1):
    sum = 0
    i = 0
    size = len(str1)
    while i < size:
        curr = "0"
        while i < size and '0' <= str1[i] <= '9':
            curr += str1[i]
            i += 1
        sum += int(curr)
        if i < size:
            i += 1
    return sum


def ratiorg2(str1):
    count = 0
    for i in re.findall('[0-9]+', str1):
        count += int(i)
    return count


# print(ratiorg2("2 apples, 12 oranges, 3 rbyhik"))

# Task 3    **********************************************************************************************
'''Մուտքագրեք երեք ամբողջ թիվ: Տպեք «Տեսակավորված» բառը, եթե թվերը նշված են
ոչ աճող կամ չնվազող հերթականությամբ, իսկ «Չտեսակավորված» հակարակ
դեփքում:'''


def sortted(l):
    for i in range(len(l)):
        j = i
        while j + 1 < len(l) and l[j] <= l[j + 1]:
            j += 1
        if j + 1 == len(l):
            return "sorted"
        j = i
        while j + 1 < len(l) and l[j] >= l[j + 1]:
            j += 1
        if j + 1 == len(l):
            return "sorted"
        return "unsorted"


def sortted_for_3_elements(a, b, c):
    if (a < b < c) or (a > b > c):
        return "sorted"
    return "unsorted"


# print(sortted([5,3,3]))
# print(sortted_for_3_elements(1,2,3))

# Task 4    **********************************************************************************************
"""Գրել ֆունկցիա, որը տրված բնական թվի համար կստուգի, արդյոք այն
կատարյալ թիվ է, թե ոչ։"""


def perfect(num):
    sum = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            sum += i
    return sum == num


# print(perfect(496))

# Task 5   **********************************************************************************************
'''Գրել ծրագիր, որը տրված թվային արժեքներով ցուցակի համար, կհաշվի նրա
էլեմենտների գումարը։'''


def summ(lis):
    if len(lis) == 0:
        return "List is empty"
    sum1 = 0
    for i in lis:
        sum1 += i
    return sum1


# print(summ([1,2,3,4,5]))

# Task 6    **********************************************************************************************
'''Գրել ֆունկցիա, որը տրված թվային արժեքներով ցուցակի համար, կվերադարձնի այդ
ցուցակի ամենամեծ էլեմենտը։'''


def maxx(lis):
    if len(lis) == 0:
        return "List is empty"
    max = lis[0]
    for i in lis:
        if max < i:
            max = i
    return max


# print(maxx([10000,2,378,3,4,5]))


# Task 7    **********************************************************************************************
'''Գրել ֆունկցիա, որը տրված ցուցակից կջնջի տրված արժեքին հավասար բոլոր
էլեմենտները։'''


def dele(lis, num):
    for i in lis:
        if i == num:
            lis.remove(i)
    return lis


def dele2(lis, num):
    return [i for i in lis if i != num]


# print(dele2([1,2,378,1,3,4,5],1))


# Task 8   **********************************************************************************************
'''Գրեք ֆունկցիա որը կվերադարձնի տրված թվային արժեքներով ցուցակի բոլոր
էլեմենտների արտադրյալը։'''


def mull(lis):
    if len(lis) == 0:
        return "List is empty"
    mul = 1
    for i in lis:
        mul *= i
    return mul


# print(mull([1,2,3,4,5]))

# Task 9   **********************************************************************************************
'''Գրեք ֆունկցիա՝ տողը հակադարձելու համար, եթե դրա երկարությունը 4-ի
բազմապատիկ է։'''


def func1(str):
    if len(str) % 4 == 0:
        return str[::-1]
    return "String doesn't need to be reversed"


# print(func1("agnesaqw"))

# Task 10  **********************************************************************************************
'''Գրեք ֆունկցիա՝ որը տրված բնական n թվի համար վերադարձնում է Ֆիբոնաչիի n-րդ
անդամը։ Խնդիրը լուծել և ռեկուրսիվ, և իտերատիվ մեթոդներով։'''


def fib1(n):
    n_fib = None
    if n < 1:
        print('n must be > 0')
    elif n == 1:
        n_fib = 0
    elif n == 2:
        n_fib = 1
    else:
        prev_2, prev_1 = 0, 1
        for i in range(2, n):
            n_fib = prev_2 + prev_1
            prev_2 = prev_1
            prev_1 = n_fib
    return n_fib


# print(fib1(4))


def fib2(n):
    if n <= 0:
        return "Input positive number"
    if n == 1:
        value = 0
    elif n == 2:
        value = 1
    else:
        value = fib2(n - 2) + fib2(n - 1)
    return value


# print(fib2(4))

# Task 11   **********************************************************************************************
'''Գրել ֆունկցիա, որը տրված 2 բնական թվերի համար կվերադարձնի նրանց
ամենափոքր ընդհանուր բազմապատիկը։'''


def lcm(x, y):
    # curr = max(x, y)
    curr = x if x > y else y
    while (True):
        if curr % x == 0 and curr % y == 0:
            return curr
        curr += 1


# print(lcm(6, 7))


# Task 12   **********************************************************************************************
'''Գրեք python ծրագիր՝ նշված թվի հաջորդ ամենափոքր պալինդրոմը գտնելու համար:'''


def nextPol(num):
    while (True):
        num += 1
        if str(num) == str(num)[::-1]:
            return num


# print(nextPol(121))

# Task 13   **********************************************************************************************
'''Ռոբոտը կանգնած է ուղղանկյուն ցանցի վրա և ներկայումս գտնվում է կետում (X0,
Y0): Կոորդինատները ամբողջ թիվ են։ Այն ստանում է N հեռակառավարման
հրամաններ: Յուրաքանչյուր հրաման մեկն է՝ վեր, վար, ձախ, աջ: Ճիշտ հրաման
ստանալուց հետո ռոբոտը մեկ միավոր է տեղափոխում տվյալ ուղղությամբ։ Եթե
ռոբոտը սխալ հրաման է ստանում, նա պարզապես անտեսում է այն: Որտե՞ղ է
գտնվելու ռոբոտը բոլոր հրամաններին հետևելուց հետո:
Ուշադրություն: աջը՝ x0+1, ձախը՝ x0-1, վերևը՝ y0+1, ներքևը՝ y0-1։'''


# match case

def robot(str1):
    x0 = 0
    y0 = 0
    for i in str1:
        if i == 'u':
            y0 += 1
        if i == 'd':
            y0 -= 1
        if i == 'l':
            x0 -= 1
        if i == 'r':
            x0 += 1
    return x0, y0


# print(robot("udrluqhfhuhc"))


# Task 14   **********************************************************************************************
'''Ստուգեք, արդյոք 2 ցուցակները 1-քայլ ցիկլիկ են:'''


def func2(l1, l2):
    for i in range(len(l1) - 1):
        if l1[i] != l2[i + 1]:
            return False
    if l1[-1] != l2[0]:
        return False
    return True


def funcc(l1, l2):
    if len(l1) != len(l2):
        return False
    if not func2(l1, l2) and not func2(l1[::-1], l2[::-1]):
        return False
    return True


# print(funcc([1, 2, 3, 4, 5, 6], [6, 1, 2, 3, 4, 5]))

# Task 15   **********************************************************************************************
'''Գրել ծրագիր, որը ստանւմ է թիվ, գտեք առավելագույն թիվը, որը կարող եք ստանալ՝
ջնջելով տվյալ թվի ուղիղ մեկ թվանշանը:'''


def delNum2(num):
    str1 = str(num)
    curr = str1[0]
    index = 0
    for i in range(len(str1)):
        if str1[i] < curr:
            curr = str1[i]
            index = i
    return int(str(str1[:index]) + str(str1[index + 1:]))


def delete_digit(n):
    str_num = str(n)
    min_digit = int(str_num[0])
    index = 0
    for i in range(len(str_num)):
        if int(str_num[i]) < min_digit:
            min_digit = int(str_num[i])
            index = i
    return int(str_num[:index] + str_num[index + 1:])


# print(delete_digit(1980))
# print(delNum2(152671))

# Task 16   **********************************************************************************************
'''Գրեք ֆուկցիա որը ստանում է tuple տիպի օբյեկտ և վերադարձնում նոր tuple
բաղկացած միայն առաջին tuple֊ի թվերից։'''


# complex numbers are also numbers, so I decided to include them

def tup1(oldTup):
    listt = []
    for i in oldTup:
        if type(i) in (float, int, complex):
            listt.append(i)
    return tuple(listt)


# print(tup1((1.3, 2 + 3j, "te", [123], 3, 6, True)))

# Task 17   **********************************************************************************************
'''Գրեք Python ֆուկցիա որը ստանում է tuple և ցանկացաց տիպի օբյեկտ և ավելացնում
է ստացած արժեքը tuple մեջ։'''


def addTuple(tup, elem):
    return tup + (elem,)


# print(addTuple((1,2,3), [1,2,3]))


# Task 18  **********************************************************************************************
'''Գրեք Python ֆուկցիա որը ստանում է tuple դարձնում է string։ Tuplex֊ի էլեմենտները
ստրինգում պետք է բաժանված լինեն ‘-’ նշանով։'''


def func3(tup):
    # str1 = ""
    # for i in tup:
    #     str1 += str(i) + "-"
    str1 = '-'.join(map(str, tup))
    return str1


# print(func3((1, 2, 3, 4, [1, 2, 3], "esim")))

# Task 19  **********************************************************************************************
'''Գրեք Python ֆուկցիա որը ստանում է list և պետքա գտնել նրա երկարությունը առանց
len() ֆունկցիա֊ի օգտագորձմամբ։'''


def lengthh(listt):
    count = 0
    for i in listt:
        count += 1
    return count


# print(lengthh([1,2,3,4,5]))


# Task 20  **********************************************************************************************
'''Ticket numbers usually consist of an even number of digits. A ticket number is considered
lucky if the sum of the first half of the digits is equal to the sum of the second half.
Given a ticket number n, determine if it&#39;s lucky or not. Not using: string, list, tuple, set'''


def lucky(num):
    curr = num
    count = 0
    while curr >= 1:
        count += 1
        curr /= 10
    if count % 2 != 0:
        return "not lucky"
    n = count / 2
    sum1 = 0
    while n:
        sum1 += num % 10
        num //= 10
        n -= 1
    while num >= 1:
        sum1 -= num % 10
        num //= 10
    return sum1 == 0


# print(lucky(11112020))


# Task 21  **********************************************************************************************
'''Euler function is return a count of numbers not great than N, which are mutualy simple with
N.'''


# 1 solution

def is_mutually(num1, num2):
    for i in range(2, num1):
        if num1 % i == 0 and num2 % i == 0:
            return False
    return True


def euler1(num):
    count = 0
    for i in range(1, num):
        if is_mutually(num, i):
            count += 1
    return count


# 2 solution
def euler2(n):
    count = 0
    for i in range(1, n):
        if math.gcd(i, n) == 1:
            count += 1
    return count


# print(euler2(11))

# Task 22  **********************************************************************************************
'''You are given a 0-indexed string array words, where words[i] consists of lowercase English
letters. In one operation, select any index i such that 0 &lt; i &lt; words.length and words[i - 1]
and words[i] are anagrams, and delete words[i] from words. Keep performing this operation
as long as you can select an index that satisfies the conditions.
Return words after performing all operations. It can be shown that selecting the indices for
each operation in any arbitrary order will lead to the same result.
An Anagram is a word or phrase formed by rearranging the letters of a different word or
phrase using all the original letters exactly once. For example, &quot;dacb&quot; is an anagram of
&quot;abdc&quot;.'''


def isanagram(str1, str2):
    dict1, dict2 = {}, {}
    for i in str1:
        if i in dict1.keys():
            dict1[i] += 1
        else:
            dict1[i] = 1

    for i in str2:
        if i in dict2.keys():
            dict2[i] += 1
        else:
            dict2[i] = 1
    return dict1 == dict2


def removeAnagrams(listt):
    i = 0
    while i in range(len(listt) - 1):
        if isanagram(listt[i], listt[i + 1]):
            listt.remove(listt[i + 1])
            i = 0
        else:
            i += 1
    return listt


# esim = ["abba", "baba", "bbaa", "cda", "esim", "cda", "acd", "dac"]
# print(removeAnagrams(esim))

# Task 23  **********************************************************************************************
'''You are given an array of strings names, and an array heights that consists of distinct
positive integers. Both arrays are of length n. For each index i, names[i] and heights[i]
denote the name and height of the ith person. Return names sorted in descending
order by the people&#39;s heights.'''


def sorting_height(list1, main_list):
    for i in range(0, len(list1) - 1):
        for j in range(len(list1) - 1):
            if list1[j] < list1[j + 1]:
                temp = list1[j]
                list1[j] = list1[j + 1]
                list1[j + 1] = temp
                temp = main_list[j]
                main_list[j] = main_list[j + 1]
                main_list[j + 1] = temp

    return main_list


# names = ["Mary", "John", "Emma"]
# heights = [180, 165, 170]
# #
# names1 = ["Alice", "Bob", "Bob"]
# heights1 = [155, 185, 150]
#
# print(sorting_height(heights, names))
# print(sorting_height(heights1, names1))


def del_dig(num):
    minn = 0
    i = 1
    while num // i:
        left = (num // (i * 10)) * i
        right = (num % i)
        temp = left + right
        i *= 10
        # print(temp)
        if temp > minn:
            minn = temp
    return minn


n = 1980
print(del_dig(n))
