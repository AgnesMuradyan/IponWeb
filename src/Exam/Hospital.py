from datetime import timedelta, datetime


class PersonError(Exception):
    pass


class DoctorError(Exception):
    pass


class PatientError(Exception):
    pass


class Person:
    def __init__(self, n, s, a, g):
        if isinstance(n, str):
            self.__name = n
        else:
            raise PersonError("wrong input for name")
        if isinstance(s, str):
            self.__surname = s
        else:
            raise PersonError("wrong input for surname")
        if g == "M" or g == "F":
            self.__gender = g
        else:
            raise PersonError("wrong input for gender")
        if 18 <= a <= 100:
            self.__age = a
        else:
            raise PersonError("wrong input for age")

    def __repr__(self):
        return f"{self.__name} {self.__surname} - {self.__gender}, {self.__age} years old. "

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

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value):
        if value == "M" or value == "F":
            self.__gender = value
        else:
            raise PersonError("wrong input for gender")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if 18 <= value <= 100:
            self.__age = value
        else:
            raise PersonError("wrong input for age")


class Patient(Person):
    def __init__(self, name, surname, age, gender):
        super().__init__(name, surname, age, gender)

    def __repr__(self):
        return super(Patient, self).__repr__()

    def __ne__(self, other):
        return self.name == other.name and self.surname == other.surname and self.gender == other.gender and self.age == other.age


class Doctor(Person):
    def __init__(self, name, surname, age, gender):
        super().__init__(name, surname, age, gender)
        self.__schedule = {}

    def __repr__(self):
        curr = super(Doctor,
                     self).__repr__() + "\n" + f"Schedule : "
        for i, v in self.schedule.items():
            curr += f"{i.name}, {v} " + "\n"
        return curr

    @property
    def schedule(self):
        return self.__schedule

    # @schedule.setter
    # def schedule(self, value):
    #     pass

    @staticmethod
    def coincide(d1, d2):
        d1_end = d1 + timedelta(minutes=30)
        d2_end = d2 + timedelta(minutes=30)
        if d1 < d2_end and d1 > d2:
            return False
        if d2 < d1_end and d2_end > d1_end:
            return False
        if d1 == d2 and d1_end == d2_end:
            return False
        else:
            return True

    def is_free(self, date_time: datetime):
        # end_time = date_time + timedelta(minutes=30)
        # st = True
        # en = True
        for i in self.__schedule.values():
            if not self.coincide(date_time, i):
                return False
        return True

    def whoo(self, date_time):
        for i, v in self.__schedule.items():
            if not self.coincide(date_time, v):
                return i

    def is_registered(self, patient):
        if isinstance(patient, Patient):
            if patient in self.__schedule.keys():
                return True
            else:
                return False
        else:
            raise DoctorError

    def register_patient(self, patient, date_time):
        if isinstance(patient, Patient) and isinstance(date_time, datetime):
            if date_time.hour < 9 or date_time.hour >= 17 or (date_time.hour == 16 and date_time.minute > 30):
                print("Working hour is 9-17")
                return
            if self.is_registered(patient):
                print(f"Patient {patient.name} already registered")
            elif not self.is_free(date_time):
                x = self.whoo(date_time)
                print(f"Datetime {date_time} is already taken by {x.name}")
            elif len(self.__schedule) >= 16:
                print(f"Maximum capacity of patients is 16")
            else:
                self.__schedule[patient] = date_time
                print(f"Patient {patient.name} successfully registered at {date_time}")
        else:
            raise DoctorError


p1 = Patient("Ani", "Arzumanyan", 20, "F")
# p = Patient("Magda", "Gyurjyan", 21, "F")
d = Doctor("Agnes", "Muradyan", 20, "F")
p2 = Patient("Martin", "Yan", 18, "M")
p3 = Patient("Gegham", "Yan", 19, "M")
p4 = Patient("Ashkhen", "Yan", 20, "F")
p5 = Patient("Ashkhen", "Yan", 20, "F")
p6 = Patient("Ashkhen", "Yan", 20, "F")
p7 = Patient("Ashkhen", "Yan", 20, "F")
p8 = Patient("Ashkhen", "Yan", 20, "F")
p9 = Patient("Ashkhen", "Yan", 20, "F")
p10 = Patient("Ashkhen", "Yan", 20, "F")
p11 = Patient("Ashkhen", "Yan", 20, "F")
p12 = Patient("Ashkhen", "Yan", 20, "F")
p13 = Patient("Ashkhen", "Yan", 20, "F")
p14 = Patient("Ashkhen", "Yan", 20, "F")
p15 = Patient("Ashkhen", "Yan", 20, "F")
p16 = Patient("Ashkhen", "Yan", 20, "F")
p17 = Patient("Ashkhen", "Yan", 20, "F")

# # print(p)
# # print(d)
# d.register_patient(p1, datetime(2020, 3, 2, 9))
# d.register_patient(p2, datetime(2020, 3, 2, 9, 30))
# d.register_patient(p3, datetime(2020, 3, 2, 10))
# d.register_patient(p4, datetime(2020, 3, 2, 10, 30))
# d.register_patient(p5, datetime(2020, 3, 2, 11))
# d.register_patient(p6, datetime(2020, 3, 2, 11, 30))
# d.register_patient(p7, datetime(2020, 3, 2, 12))
# d.register_patient(p8, datetime(2020, 3, 2, 12, 30))
# d.register_patient(p9, datetime(2020, 3, 2, 13))
# d.register_patient(p10, datetime(2020, 3, 2, 13, 30))
# d.register_patient(p11, datetime(2020, 3, 2, 14))
# d.register_patient(p12, datetime(2020, 3, 2, 14, 30))
# d.register_patient(p13, datetime(2020, 3, 2, 15))
# d.register_patient(p14, datetime(2020, 3, 2, 15, 30))
# d.register_patient(p15, datetime(2020, 3, 2, 16))
# d.register_patient(p16, datetime(2020, 3, 2, 16, 30))
# d.register_patient(p17, datetime(2020, 3, 2, 17, 00))
# d.register_patient(p2, datetime(2020, 3, 2, 12))
# d.register_patient(p3, datetime(2020, 3, 2, 12, 40))
# d.register_patient(p4, datetime(2020, 3, 2, 12, 25))
# # print()
# #
# d.register_patient(p4, datetime(2020, 3, 2, 18, 30))
# print(d)
# print(d.is_free(datetime(2020, 3, 2, 12, 35)))
