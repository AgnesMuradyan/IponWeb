import sys

# Task 1       ***************************************************************
"""Write a Python program to create a new dictionary by extracting the mentioned keys
from the below dictionary."""


def del_dict(dictt: dict, keyss: list):
    return dict(filter(lambda elem: elem[0] in keyss, dictt.items()))


# print(del_dict({
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}, ["name", "salary"]))

# Task 2       ***************************************************************
'''Get the key of a minimum value from the following dictionary.'''


def ext_min(dictt: dict):
    # minn = min(dictt, key=lambda x: dictt[x])
    item = None
    if len(dictt) == 0:
        return "dectionary is empty"
    minn = sys.maxsize
    for i, v in dictt.items():
        if v < minn:
            minn = v
            item = i
    return item


#
# print(ext_min({
#     "Physics": 82,
#     "Math": 65,
#     "history": 72
# }))

# Task 3       ***************************************************************
'''Write a Python program to copy the contents of a file to another file'''


def copy(file1, file2):
    with open(file1, "r") as f1:
        with open(file2, "w") as f2:
            # for line in f1:
            #     f2.write(line)
            f2.write(f1.read())

    with open(file2, "r") as f2:
        for line in f2:
            print(line, end="")


# copy("esim.txt", "new.txt")

# Task 4       ***************************************************************
'''Write a Python program to count the frequency of words in a file'''


def frequency(file1):
    dictt = {}
    with open(file1, "r") as myfile:
        words = myfile.read().split()
        for word in words:
            if word in dictt:
                dictt[word] += 1
            else:
                dictt[word] = 1
    return dictt


# print(frequency("esim.txt"))


# Task 5       ***************************************************************
'''Write a Python program to read last n lines of a file'''


def n_lines(file1, n):
    with open(file1, "r") as f:
        for line in (f.readlines()[-n:]):
            print(line, end="")
        # x = f.readlines()
        # if n > len(x):
        #     print("The input is not correct")
        #     return
        # n = len(x) - n
        # for i in range(n, len(x)):
        #     print(x[i], end="")


# n_lines("esim.txt", 3)


# Task 6         ********************************************************************
'''Write class Company
Data members: company_name, founded_at, employees_count
Data methods: __init__, __repr__'''


class Company:
    def __init__(self, n, f, c):
        self.company_name = n
        self.founded_at = f
        self.employees_count = c

    def __repr__(self):
        return "Company name is " + self.company_name + ", which was founded in " + str(
            self.founded_at) + ". The count of employees is " + str(self.employees_count)


'''Write class Job.
Data members: company(Company type), salary, experience_year, position.
Data methods: __init__, __repr__, change_salary, change_experience_year,
change_postition.'''


class Job:
    def __init__(self, c, s, e, p):
        self.company = c
        self.salary = s
        self.experience_year = e
        self.position = p

    def __repr__(self):
        return self.company.company_name + " " + str(self.salary) + " " + str(
            self.experience_year) + " " + self.position

    def change_salary(self, new_salary):
        self.salary = new_salary

    def change_experience_year(self, new_experience):
        self.experience_year = new_experience

    def change_postition(self, new_position):
        self.position = new_position


'''Write class Person.
Data members: name, surname, gender(Male or Female), age, address, friends(list
of Person type), job(list of Job type)
Data methods: __init__, __repr__, add_friend, remove_friend, add_job,
remove_job, display_job'''


class Person:
    def __init__(self, n, s, g, a, ad, f, j):
        self.name = n
        self.surname = s
        self.gender = g
        self.age = a
        self.address = ad
        self.friends = f
        self.job = j

    def __repr__(self):
        esim = self.name + " " + self.surname + " " + self.gender + " " + str(
            self.age) + " " + self.address + " friends are: "
        for i in self.friends:
            esim += i.name + " "
        esim += " Jobs are: "
        for i in self.job:
            esim += i.position + " "
        return esim

    def add_friend(self, new_friend):
        self.friends.append(new_friend)
        new_friend.friends.append(self)

    def remove_friend(self, old_friend):
        self.friends.remove(old_friend)
        old_friend.friends.remove(self)

    def add_job(self, new_job):
        self.job.append(new_job)
        new_job.company.employees_count += 1

    def remove_job(self, old_job):
        self.job.remove(old_job)
        old_job.company.employees_count -= 1

    def display_job(self):
        for job in self.job:
            print(job)


# comp = Company("Agnes's Kingdom", 2002, 301)
# job1 = Job(comp, 26000, 12, "CEO")
# job2 = Job(comp, 100, 10, "Java")
# job3 = Job(comp, 2000000, 1, "SuperWiser")
#
# p2 = Person("Magda", "Gyurjyan", "Female", 21, "Yerevan", [], [])
# p1 = Person("Agnes", "Muradyan", "Female", 20, "Yerevan", [], [])
# p3 = Person("Christin", "Haarutyunyan", "Female", 20, "Yerevan", [], [])
# p1.add_friend(p2)
# p3.add_friend(p1)
# p1.add_job(job1)
# p1.add_job(job3)
# p2.add_job(job2)
#
# print(comp.employees_count)
#
# p1.remove_job(job3)
#
# print(comp.employees_count)
#
# p2.add_job(job3)
#
# print(comp.employees_count)
# # print(comp)
# # print(job1)
# print(p1)
# print(p2)

'''Some logics
When Person add job Company employees count should increase by 1.
When Person quit the job Company employees count should decrease by 1.
You can come up with other logics.'''

# Task 7        ********************************************************************

'''
Class - Date
Data members
Year - integer
Mounth - integer
Day - integer
Data methods
Constructor - 3 params for init year, mounth, day
__repr__ for print Date objet like - day.mount.year
Ex. 15.10.1950
add_day - add day to given Date object
Add_mount - add mount to given Date object
Add_year - add year to given Date object
__is_leap_year - check year is leap or not'''


class Date:
    dict_months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August',
                   9: 'September', 10: 'October', 11: 'November', 12: 'December'}

    def __init__(self, d: int, m: int, y: int):
        self.dict_days = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31,
                          'August': 31,
                          'September': 30, 'October': 31, 'November': 30, 'December': 31}
        self.year = y
        self.month = m
        self.day = d
        if self._is_leap_year():
            self.dict_days['February'] = 29

    def __repr__(self):
        return str(self.day) + "." + str(self.month) + "." + str(self.year)

    def add_day(self, add_day):
        self.day += add_day
        while self.day > self.dict_days[self.dict_months[self.month]]:
            self.day = self.day - self.dict_days[self.dict_months[self.month]]
            self.add_month(1, 1)
        if self._is_leap_year():
            self.dict_days['February'] = 29
        else:
            self.dict_days['February'] = 28

    def add_month(self, add_month, mon=0):
        self.month += add_month
        while self.month > 12:
            self.month = self.month - 12
            self.add_year(1)
        if mon == 0:
            while self.day > self.dict_days[self.dict_months[self.month]]:
                self.day -= 1
        if self._is_leap_year():
            self.dict_days['February'] = 29
        else:
            self.dict_days['February'] = 28

    def add_year(self, add_year):
        self.year += add_year
        if not self._is_leap_year() and self.month == 2 and self.day == 29:
            self.day = 28
        if self._is_leap_year():
            self.dict_days['February'] = 29
        else:
            self.dict_days['February'] = 28

    def _is_leap_year(self):
        if (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0):
            return True
        return False


date = Date(29, 2, 2004)
print(date)
# date.add_month(1)
date.add_month(25)
# date.add_year(1)
# date.add_day(2)
# print(date)
# date.add_day(1)

print(date)
print(date._is_leap_year())

'''
Class - Time
Data members
Hour - int
Minute - int
Second - int
Data methods

__init__ constructor
__repr__
3. add_second(s)
2. add_minute(m)
1.add_hour(h)
sum() - Գումարել երկու Time տիպի օբյեկտ(հաշվի առնել, որ վայրկյանները
գումարելուց կարող է փոխվել նաև րոպեն, րոպեները փոխվելուց նաև ժամը)
sum 2 Time objects (take into account that, when add seconds, minutes can be
changed, when add minutes hour can be changed, when add hours, can get value &gt;
24, that case should take hour%24 as hour)'''


class Time:
    def __init__(self, h: int, m: int, s: int):
        self.hour = h
        self.minute = m
        self.second = s

    def __repr__(self):
        return str(self.hour) + " hours " + str(self.minute) + " minutes " + str(self.second) + " seconds."

    def add_seconds(self, add_sec):
        self.second += add_sec
        while self.second >= 60:
            self.second = self.second - 60
            self.add_minutes(1)

    def add_minutes(self, add_min):
        self.minute += add_min
        while self.minute >= 60:
            self.minute = self.minute - 60
            self.add_hour(1)

    def add_hour(self, add_hou):
        self.hour += add_hou
        if self.hour >= 24:
            self.hour = self.hour % 24

    def sum(self, time2):
        self.add_seconds(time2.second)
        self.add_minutes(time2.minute)
        self.add_hour(time2.hour)

# time1 = Time(23, 58, 20)
# time2 = Time(0, 1, 40)
# print(time1)
# print(time2)
# time1.sum(time2)
# print(time1)
#
