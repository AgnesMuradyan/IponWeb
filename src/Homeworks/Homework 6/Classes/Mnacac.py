import DateTime
import Money


class CompanyError(Exception):
    pass


class JobError(Exception):
    pass


class PersonError(Exception):
    pass


class DoctorError(Exception):
    pass


class CityError(Exception):
    pass


class UniversityError(Exception):
    pass


class TeacherError(Exception):
    pass


class StudentError(Exception):
    pass


class Company:
    def __init__(self, c_m, f_a, e_c):
        if isinstance(c_m, str) and isinstance(f_a, DateTime.Date) and isinstance(e_c, int) and e_c >= 0:
            self.__company_name = c_m
            self.__founded_at = f_a
            self.__employees_count = e_c
        else:
            raise CompanyError("Input data is not correct")

    def __repr__(self):
        return f"Company name : {self.__company_name}, Founded at : {self.__founded_at}, Employees count : {self.__employees_count}"

    @property
    def company_name(self):
        return self.__company_name

    @company_name.setter
    def company_name(self, value):
        if isinstance(value, str):
            self.__company_name = value
        else:
            raise CompanyError("Company name should be string")

    @property
    def founded_at(self):
        return self.__founded_at

    @founded_at.setter
    def founded_at(self, value):
        if isinstance(value, DateTime.Date):
            self.__founded_at = value
        else:
            raise CompanyError("This should be Date")

    @property
    def employees_count(self):
        return self.__employees_count

    @employees_count.setter
    def employees_count(self, value):
        if isinstance(value, int) and value >= 0:
            self.__employees_count = value
        else:
            raise CompanyError("Employees count should be integer")


c = Company("Agnes's Kingdom", DateTime.Date(2002, 6, 5), 1200)


# print(c)


class Job:
    def __init__(self, c, s, e_y, p):
        if isinstance(c, Company) and isinstance(s, Money.Money) and isinstance(e_y, int) and e_y >= 0 and isinstance(p,
                                                                                                                      str):
            self.__company = c
            self.__salary = s
            self.__experience_year = e_y
            self.__position = p
        else:
            raise JobError

    @property
    def company(self):
        return self.__company

    @company.setter
    def company(self, value):
        if isinstance(value, Company):
            self.__company = value
        else:
            raise JobError("Type of Company should be Company")

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if isinstance(value, Money.Money):
            self.__salary = value
        else:
            raise JobError("Type of salary should be Money")

    @property
    def experience_year(self):
        return self.__experience_year

    @experience_year.setter
    def experience_year(self, value):
        if isinstance(value, int) and value >= 0:
            self.__experience_year = value
        else:
            raise JobError("Type of Salary should be integer")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, str):
            self.__position = value
        else:
            raise JobError("Type of Position should be String")

    def __repr__(self):
        return f"Company : {self.__company.__repr__()} \nSalary : {self.__salary}, Experience year : " \
               f"{self.__experience_year}, Position : {self.__position}"

    def change_salary(self, newSalary):
        self.__salary = newSalary

    def change_experience_year(self, new_year):
        self.__experience_year = new_year

    def change_position(self, new_position):
        self.__position = new_position


j1 = Job(c, Money.Money(2000, "USD"), 2020, "Supervisor")
j2 = Job(c, Money.Money(100, "USD"), 2010, "DB Developer")


# print(j1)
# print(j2)


class Person:
    def __init__(self, n, s, a, g, add, fr, j):
        if isinstance(n, str):
            self.__name = n
        else:
            raise PersonError("wrong input for name")
        if isinstance(s, str):
            self.__surname = s
        else:
            raise PersonError("wrong input for surname")
        if g == "Male" or g == "Female":
            self.__gender = g
        else:
            raise PersonError("wrong input for gender")
        if a >= 0:
            self.__age = a
        else:
            raise PersonError("wrong input for age")
        if isinstance(add, str):
            self.__address = add
        else:
            raise PersonError("wrong input for address")
        if isinstance(fr, list) and all(isinstance(x, Person) for x in fr):
            self.__friends = fr
        else:
            raise PersonError("wrong input for friends")
        if isinstance(j, list) and all(isinstance(x, Job) for x in j):
            self.__job = j
        else:
            raise PersonError("wrong input for Jobs")

    def __repr__(self):
        esim = self.__name + " " + self.__surname + " " + self.__gender + " " + str(
            self.__age) + " " + self.__address + " friends are: "
        for i in self.__friends:
            esim += i.name + " "
        esim += " Jobs are: "
        for i in self.__job:
            esim += i.position + " "
        return esim

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.__name = value
        else:
            raise PersonError("wrong input for name")

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value):
        if isinstance(value, str):
            self.__surname = value
        else:
            raise PersonError("wrong input for surname")

    def add_friend(self, newFriend):
        self.__friends.append(newFriend)
        newFriend.__friends.append(self)

    def remove_friend(self, oldFriend):
        self.__friends.remove(oldFriend)
        oldFriend.__friends.remove(self)

    def add_job(self, newJob):
        self.__job.append(newJob)
        newJob.company.employees_count += 1

    def remove_job(self, oldJob):
        if oldJob in self.__job:
            self.__job.remove(oldJob)
            oldJob.company.employees_count -= 1

    def display_job(self):
        return self.__job


# print(c.employees_count)
p1 = Person("Agnes", "Muradyan", 19, "Female", "Yerevan", [], [j1])
p2 = Person("Magda", "Gyurjyan", 21, "Female", "Yerevan", [], [])
p3 = Person("Ani", "Arzumanyan", 19, "Female", "Yerevan", [], [j2])
p1.add_friend(p2)
p3.add_friend(p1)
p2.add_job(j2)


# print(p1)
# print(p2)
# print(p3)
# print(c.employees_count)
# p3.remove_job(j2)
# print(c.employees_count)


class Doctor(Person):
    def __init__(self, name, surname, age, gender, address, friends, job, department: str, profession: str,
                 patronymic: str, salary: Money):
        super().__init__(name, surname, age, gender, address, friends, job)
        if isinstance(department, str):
            self.__department = department
        else:
            raise DoctorError("Department should be a string")
        if isinstance(profession, str):
            self.__profession = profession
        else:
            raise DoctorError("Profession should be a string")
        if isinstance(patronymic, str):
            self.__patronymic = patronymic
        else:
            raise DoctorError("Patronymic should be a string")
        if isinstance(salary, Money.Money):
            self.__salary = salary
        else:
            raise DoctorError("Salary should be a Money")

    def __repr__(self):
        return super(Doctor,
                     self).__repr__() + "\n" + f"Department : {self.department}, Profession : {self.profession}, Patronymic : {self.patronymic}, Salary : {self.salary}"

    @property
    def department(self):
        return self.__department

    @department.setter
    def department(self, value):
        if isinstance(value, str):
            self.__department = value
        else:
            raise DoctorError("Department should be a string")

    @property
    def profession(self):
        return self.__profession

    @profession.setter
    def profession(self, value):
        if isinstance(value, str):
            self.__profession = value
        else:
            raise DoctorError("Profession should be a string")

    @property
    def patronymic(self):
        return self.__patronymic

    @patronymic.setter
    def patronymic(self, value):
        if isinstance(value, str):
            self.__patronymic = value
        else:
            raise DoctorError("Patronymic should be a string")

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if isinstance(value, Money.Money):
            self.__salary = value
        else:
            raise DoctorError("Salary should be a Money")


d = Doctor("Agnes", "Muradyan", 19, "Female", "Yerevan", [], [j1], "depart1", "psychologist", "patr1",
           Money.Money(10, "USD"))


# print(d)


class City:
    def __init__(self, name: str, major: Person, population: int, language: str):
        if isinstance(name, str):
            self.__name = name
        else:
            raise CityError("City name should be a string")
        if isinstance(major, Person):
            self.__major = major
        else:
            raise CityError("Major should be Person")
        if isinstance(population, int):
            self.__population = population
        else:
            raise CityError("Population should be integer")
        if isinstance(language, str):
            self.__language = language
        else:
            raise CityError("Language should be a string")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.__name = value
        else:
            raise CityError("City should be a string")

    @property
    def major(self):
        return self.__major

    @major.setter
    def major(self, value):
        if isinstance(value, Person):
            self.__major = value
        else:
            raise CityError("Major should be Person")

    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, value):
        if isinstance(value, int):
            self.__population = value
        else:
            raise CityError("Population should be integer")

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, value):
        if isinstance(value, str):
            self.__language = value
        else:
            raise CityError("Language should be a string")

    def __repr__(self):
        return f" Name : {self.__name}, Major : {self.__major.name}, Population : {self.__population}, Language : {self.__language}"


city1 = City("Sevan", p1, 30000, "Armenian")


# print(city1)


class University:
    def __init__(self, name: str, founded_at: DateTime.Date, rector: Person, city: City):
        if isinstance(name, str):
            self.__name = name
        else:
            raise UniversityError("Name should be a string")
        if isinstance(founded_at, DateTime.Date):
            self.__founded_at = founded_at
        else:
            raise UniversityError("This should be a Date")
        if isinstance(rector, Person):
            self.__rector = rector
        else:
            raise UniversityError("Rector should be Person")
        if isinstance(city, City):
            self.__city = city
        else:
            raise UniversityError("City should be a City")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.__name = value
        else:
            raise UniversityError("Name should be a string")

    @property
    def founded_at(self):
        return self.__founded_at

    @founded_at.setter
    def founded_at(self, value):
        if isinstance(value, DateTime.Date):
            self.__founded_at = value
        else:
            raise UniversityError("This should be a Date")

    @property
    def rector(self):
        return self.__rector

    @rector.setter
    def rector(self, value):
        if isinstance(value, str):
            self.__rector = value
        else:
            raise UniversityError("Rector should be a string")

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, value):
        if isinstance(value, City):
            self.__city = value
        else:
            raise UniversityError("City should be a City")

    def __repr__(self):
        return f"Name : {self.__name}, Founded in : {self.__founded_at}, Rector : {self.__rector.name}, City : {self.__city.name}"


u = University("YSU", DateTime.Date(1919, 1, 1), p1, city1)


# print(u)


class Teacher(Person):

    def __init__(self, name, surname, age, gender, address, friends, jobs, university1: University, faculty1: str,
                 experience1: int,
                 start_work_at1: DateTime.Date, subject1: str, salary1: Money.Money):
        super().__init__(name, surname, age, gender, address, friends, jobs)
        if isinstance(university1, University):
            self.__university = university1
        else:
            raise TeacherError("University should be a university")
        if isinstance(faculty1, str):
            self.__faculty = faculty1
        else:
            raise TeacherError("Faculty should be a string")
        if isinstance(experience1, int):
            self.__experience = experience1
        else:
            raise TeacherError("Experience should be an integer")
        if isinstance(start_work_at1, DateTime.Date):
            self.__start_work_at = start_work_at1
        else:
            raise TeacherError("This should be a Date")
        if isinstance(subject1, str):
            self.__subject = subject1
        else:
            raise TeacherError("Subject should be a string")
        if isinstance(salary1, Money.Money):
            self.__salary = salary1
        else:
            raise TeacherError("Salary should be a Money")

    @property
    def university(self):
        return self.__university

    @university.setter
    def university(self, value):
        if isinstance(value, University):
            self.__university = value
        else:
            raise TeacherError("University should be a university")

    @property
    def faculty(self):
        return self.__faculty

    @faculty.setter
    def faculty(self, value):
        if isinstance(value, str):
            self.__faculty = value
        else:
            raise TeacherError("Faculty should be a string")

    @property
    def experience(self):
        return self.__experience

    @experience.setter
    def experience(self, value):
        if isinstance(value, int):
            self.__experience = value
        else:
            raise TeacherError("Experience should be an integer")

    @property
    def start_work_at(self):
        return self.__start_work_at

    @start_work_at.setter
    def start_work_at(self, value):
        if isinstance(value, DateTime.Date):
            self.__start_work_at = value
        else:
            raise TeacherError("This should be a Date")

    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, value):
        if isinstance(value, str):
            self.__subject = value
        else:
            raise TeacherError("Subject should be a string")

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if isinstance(value, Money.Money):
            self.__salary = value
        else:
            raise TeacherError("Salary should be a Money")

    def __repr__(self):
        return super(Teacher,
                     self).__repr__() + "\n" + f"University : {self.__university.name}, Faculty : {self.__faculty}, Experience : {self.__experience}, Start work at : {self.__start_work_at}, Subject : {self.__subject}, Salary : {self.__salary}"


t = Teacher("Agnes", "Muradyan", 19, "Female", "Yerevan", [], [j1], u, "IAM", 2, DateTime.Date(2020, 1, 1), "Calculus",
            Money.Money(300, "AMD"))


# print(t)
# t.salary.conversation("USD")
# print(t)

class Student(Person):
    def __init__(self, name, surname, age, gender, address, friends, jobs, university: University, faculty: str,
                 course: int,
                 started_at: DateTime.Date):
        super().__init__(name, surname, age, gender, address, friends, jobs)
        if isinstance(university, University):
            self.__university = university
        else:
            raise StudentError("university should be a University")
        if isinstance(faculty, str):
            self.__faculty = faculty
        else:
            raise StudentError("Faculty should be a string")
        if isinstance(course, int):
            self.__course = course
        else:
            raise StudentError("Course should be a string")
        if isinstance(started_at, DateTime.Date):
            self.__started_at = started_at
        else:
            raise StudentError("This should be a Date")

    @property
    def university(self):
        return self.__university

    @university.setter
    def university(self, value):
        if isinstance(value, University):
            self.__university = value
        else:
            raise StudentError("university should be a University")

    @property
    def faculty(self):
        return self.__faculty

    @faculty.setter
    def faculty(self, value):
        if isinstance(value, str):
            self.__faculty = value
        else:
            raise StudentError("Faculty should be a string")

    @property
    def course(self):
        return self.__course

    @course.setter
    def course(self, value):
        if isinstance(value, int):
            self.__course = value
        else:
            raise StudentError("Course should be Integer")

    @property
    def started_at(self):
        return self.__started_at

    @started_at.setter
    def started_at(self, value):
        if isinstance(value, DateTime.Date):
            self.__started_at = value
        else:
            raise StudentError("This should be a Date")

    def __repr__(self):
        return super(Student,
                     self).__repr__() + "\n" + f"University : {self.__university.name}, Faculty : {self.__faculty}, Course : {self.__course}, Start at : {self.__started_at}"


s = Student("Agapi", "Muradyan", 22, "Female", "Yerevan", [], [j1], u, "IAM", 3, DateTime.Date(2020, 1, 1))
# print(s)