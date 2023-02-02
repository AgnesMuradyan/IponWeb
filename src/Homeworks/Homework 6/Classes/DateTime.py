from copy import deepcopy


class DateError(Exception):
    pass


class TimeError(Exception):
    pass


class DateTimeError(Exception):
    pass


class Date:
    dict_months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August',
                   9: 'September', 10: 'October', 11: 'November', 12: 'December'}

    def __init__(self, year, month, day):
        self.dict_days = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31,
                          'August': 31,
                          'September': 30, 'October': 31, 'November': 30, 'December': 31}
        if isinstance(year, int) and year > 0:
            self.__year = year
        else:
            raise DateError("Year")
        if self.is_leap_year():
            self.dict_days['February'] = 29
        if isinstance(month, int) and month in range(1, 13):
            self.__month = month
        else:
            raise DateError("Month")
        if isinstance(day, int) and day in range(1, self.dict_days[Date.dict_months[month]] + 1):
            self.__day = day
        else:
            raise DateError("Day")

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if isinstance(year, int) and year > 0:
            self.__year = year
        else:
            raise DateError("Year")
        if self.is_leap_year():
            self.dict_days['February'] = 29
        else:
            self.dict_days['February'] = 28

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month):
        if isinstance(month, int) and month in range(1, 13):
            self.__month = month
        else:
            raise DateError("Month")

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, day):
        if isinstance(day, int) and day in range(1, self.dict_days[Date.dict_months[self.__month]] + 1):
            self.__day = day
        else:
            raise DateError("Day")

    # def __init__(self, d: int, m: int, y: int):
    #     self.dict_days = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31,
    #                       'August': 31,
    #                       'September': 30, 'October': 31, 'November': 30, 'December': 31}
    #     self.year = y
    #     self.month = m
    #     self.day = d
    #     if self._is_leap_year():
    #         self.dict_days['February'] = 29

    def __repr__(self):
        return str(self.__day) + "." + str(self.__month) + "." + str(self.__year)

    def __ge__(self, other):
        if self.__year > other.__year:
            return True
        elif self.__year == other.__year:
            if self.__month > other.__month:
                return True
            elif self.__month == other.__month:
                if self.__day > other.__day:
                    return True
                elif self.__day == other.__day:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def __gt__(self, other):
        if self.__year > other.__year:
            return True
        elif self.__year == other.__year:
            if self.__month > other.__month:
                return True
            elif self.__month == other.__month:
                if self.__day > other.__day:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def __eq__(self, other):
        return self.__year == other.__year and self.__month == other.__month and self.__day == other.__day

    def add_day(self, add_day):
        self.__day += add_day
        while self.__day > self.dict_days[self.dict_months[self.__month]]:
            self.__day = self.__day - self.dict_days[self.dict_months[self.__month]]
            self.add_month(1, 1)
        if self.is_leap_year():
            self.dict_days['February'] = 29
        else:
            self.dict_days['February'] = 28

    def add_month(self, add_month, mon=0):
        self.__month += add_month
        while self.__month > 12:
            self.__month = self.__month - 12
            self.add_year(1)
        if mon == 0:
            while self.__day > self.dict_days[self.dict_months[self.__month]]:
                self.__day -= 1
        if self.is_leap_year():
            self.dict_days['February'] = 29
        else:
            self.dict_days['February'] = 28

    def add_year(self, add_year):
        self.__year += add_year
        if not self.is_leap_year() and self.__month == 2 and self.__day == 29:
            self.__day = 28
        if self.is_leap_year():
            self.dict_days['February'] = 29
        else:
            self.dict_days['February'] = 28

    def is_leap_year(self):
        if (self.__year % 4 == 0 and self.__year % 100 != 0) or (self.__year % 400 == 0):
            return True
        return False


#
# date = Date(2021, 1, 1)
# print(date)
# print(date.is_leap_year())
# date.add_day(1)
# date.add_year(90)
# date.add_month(1)
# date.add_year(4)
# date.add_month(22)
# date.add_day(19)
# date.add_day(59)
# date.add_month(40)
# print(date.is_leap_year())
# print(date)


class Time:
    def __init__(self, hour: int, minute: int, second: int):
        if isinstance(hour, int) and hour in range(0, 25):
            self.__hour = hour
        else:
            raise TimeError
        if isinstance(minute, int) and minute in range(0, 60):
            self.__minute = minute
        else:
            raise TimeError
        if isinstance(second, int) and second in range(0, 60):
            self.__second = second
        else:
            raise TimeError

    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, hour):
        if isinstance(hour, int):
            self.__hour = hour
        else:
            raise TimeError

    @property
    def minute(self):
        return self.__minute

    @minute.setter
    def minute(self, minute):
        if isinstance(minute, int):
            self.__minute = minute
        else:
            raise TimeError

    @property
    def second(self):
        return self.__second

    @second.setter
    def second(self, second):
        if isinstance(second, int):
            self.__second = second
        else:
            raise TimeError

    def __repr__(self):
        return str(self.__hour) + " hours " + str(self.__minute) + " minutes " + str(self.__second) + " seconds."

    def __ge__(self, other):
        if self.__hour > other.__hour:
            return True
        elif self.__hour == other.__hour:
            if self.__minute > other.__minute:
                return True
            elif self.__minute == other.__minute:
                if self.__second > other.__second:
                    return True
                elif self.__second == other.__second:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def __gt__(self, other):
        if self.__hour > other.__hour:
            return True
        elif self.__hour == other.__hour:
            if self.__minute > other.__minute:
                return True
            elif self.__minute == other.__minute:
                if self.__second > other.__second:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def __eq__(self, other):
        return self.__hour == other.__hour and self.__minute == other.__minute and self.__second == other.__second

    def add_seconds(self, add_sec):
        self.__second += add_sec
        while self.__second >= 60:
            self.__second = self.__second - 60
            self.add_minutes(1)

    def add_minutes(self, add_min):
        self.__minute += add_min
        while self.__minute >= 60:
            self.__minute = self.__minute - 60
            self.add_hour(1)

    def add_hour(self, add_hou):
        self.__hour += add_hou
        if self.__hour >= 24:
            self.__hour = self.__hour % 24

    def __add__(self, other):
        if isinstance(self, Time) and isinstance(other, Time):
            self.add_seconds(other.second)
            self.add_minutes(other.minute)
            self.add_hour(other.hour)
            return self
        else:
            raise TimeError('You should add two Time type objects.')


#
# time1 = Time(23, 58, 20)
# time2 = Time(0, 1, 40)
# print(time1)
# print(time2)
# time1 + time2
# print(time1)
#
# time1.add_seconds(50)
# time2.add_minutes(60)
# print(time1)
# print(time2)

class DateTime:
    def __init__(self, date: Date, time: Time):
        if isinstance(date, Date):
            self.__date = date
        else:
            raise DateTimeError
        if isinstance(time, Time):
            self.__time = time
        else:
            raise DateTimeError

    def __repr__(self):
        return f"The date is {self.__date} and the time is {self.__time}"

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value):
        if isinstance(value, Date):
            self.__date = value
        else:
            raise DateTimeError

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, value):
        if isinstance(value, Time):
            self.__time = value
        else:
            raise DateTimeError

    def __ge__(self, other):
        return self.__date > other.__date or (self.date == other.__date and self.__time >= other.__time)

    def add_year(self, years_count):
        self.__date.add_year(years_count)

    def add_month(self, months_count):
        self.__date.add_month(months_count)

    def add_day(self, days_count):
        self.__date.add_day(days_count)

    def add_hour(self, hours_count):
        if not isinstance(hours_count, int) or hours_count < 0:
            raise TimeError
        for_add = hours_count // 24
        hours_count %= 24
        self.add_day(for_add)
        if self.__time.hour + hours_count >= 24:
            self.__date.add_day(1)
        self.__time.add_hour(hours_count)

    def add_minute(self, months_count):
        if not isinstance(months_count, int) or months_count < 0:
            raise TimeError
        for_add = months_count // (60 * 24)
        months_count %= (60 * 24)
        self.add_day(for_add)
        if self.__time.hour == 23 and self.__time.minute + months_count >= 60:
            self.__date.add_day(1)
        self.__time.add_minutes(months_count)

    def add_second(self, seconds_count):
        if not isinstance(seconds_count, int) or seconds_count < 0:
            raise TimeError
        for_add = seconds_count // (60 * 60 * 24)
        seconds_count %= (60 * 60 * 24)
        self.add_day(for_add)
        if self.__time.hour == 23 and self.__time.minute == 59 and self.__time.second + seconds_count >= 60:
            self.__date.add_day(1)
        self.__time.add_seconds(seconds_count)

    def sub_year(self, years_count):
        if not isinstance(years_count, int) or years_count < 0:
            raise DateError
        self.__date.year -= years_count
        if not self.__date.is_leap_year() and self.__date.month == 2 and self.__date.day == 29:
            self.__date.day = 28

    def sub_month(self, months_count):
        if not isinstance(months_count, int) or months_count < 0:
            raise DateError
        for_months = months_count % 12
        for_add = (self.__date.month - for_months) % 12
        if for_add == 0:
            for_add = 12
        for_year = 0
        if self.__date.month - for_months != for_add:
            for_year = 1
        add_to_year = months_count // 12
        self.__date.year -= (add_to_year + for_year)
        if self.__date.day <= self.__date.dict_days[Date.dict_months[for_add]]:
            self.__date.month = for_add
        elif for_add == 2 and 29 <= self.__date.day <= 31:
            self.__date.month = for_add
            if self.__date.is_leap_year():
                self.__date.day = 29
            else:
                self.__date.day = 28
        elif self.__date.day == self.__date.dict_days[Date.dict_months[self.__date.month]]:
            self.__date.month = for_add
            self.__date.day = self.__date.dict_days[Date.dict_months[self.__date.month]]

    def sub_day(self, days_count):
        if not isinstance(days_count, int) or days_count < 0:
            raise DateError
        # k = 0
        _ = 0
        while _ < days_count:
            # k +=1
            if self.__date.is_leap_year():
                self.__date.dict_days['February'] = 29
            else:
                self.__date.dict_days['February'] = 28
            if self.__date.month == 1 and self.__date.day == 1:
                self.__date.year -= 1
                self.__date.day = self.__date.dict_days['December']
                self.__date.month = 12
            elif self.__date.day == 1:
                self.__date.month -= 1
                self.__date.day = self.__date.dict_days[Date.dict_months[self.__date.month]]
            else:
                self.__date.day -= 1
            _ += 1
        # print(k)

    def sub_hour(self, hours):
        if not isinstance(hours, int) or hours < 0:
            raise DateError
        for_add = hours // 24
        hours %= 24
        self.sub_day(for_add)
        if self.__time.hour - hours < 0:
            self.sub_day(1)
        self.__time.hour = (self.__time.hour - hours) % 24

    def sub_minute(self, months):
        if not isinstance(months, int) or months < 0:
            raise DateError
        for_add = months // 60
        minutes = months - for_add * 60
        self.sub_hour(for_add)
        self.__time.minute -= minutes
        if self.__time.minute < 0:
            self.sub_hour(1)
        self.__time.minute %= 60

    def sub_second(self, seconds):
        if not isinstance(seconds, int) or seconds < 0:
            raise DateError
        minutes = seconds // 60
        for_add = seconds - minutes * 60
        self.sub_minute(minutes)
        self.__time.second -= for_add
        if self.__time.second < 0:
            self.sub_minute(1)
        self.__time.second %= 60

    def __add__(self, other1):
        result = deepcopy(self)
        result.add_second(other1.time.second)
        result.add_minute(other1.time.minute)
        result.add_hour(other1.time.hour)
        result.add_day(other1.date.day)
        result.add_month(other1.date.month)
        result.add_year(other1.date.year)
        return result

    def __sub__(self, other):
        if self >= other:
            result = deepcopy(self)
            result.sub_second(other.time.second)
            result.sub_minute(other.time.minute)
            result.sub_hour(other.time.hour)
            result.sub_day(other.date.day)
            result.sub_month(other.date.month)
            result.sub_year(other.date.year)
            return f"{result.__date.year} years, {result.__date.month} months, {result.__date.day} days, " \
                   f"{result.__time.hour} hours, {result.__time.minute} minutes, {result.__time.second} seconds"
        else:
            raise DateTimeError

    def duration_by_days_using_time(self, other):
        result = 0
        if self >= other:
            while not self.__date == other.__date:
                other.add_day(1)
                result += 1
            if other.__time > self.__time:
                result -= 1
            return f"{result} days"
        else:
            raise DateTimeError

    def duration_by_days_not_using_time(self, other):
        days = 0
        result = deepcopy(other)
        if self >= other:
            while not result.__date == self.__date:
                days += 1
                result.add_day(1)
            if self.__time >= other.__time:
                days -= 1
        else:
            raise DateTimeError("Warning: The Start date was after the End date")
        return f"{days} days"


# date_time1 = DateTime(Date(2018, 12, 12), Time(21, 45, 45))
# date_time2 = DateTime(Date(2026, 7, 26), Time(7, 7, 7))
# date_time1.add_day(1)
# date_time1.sub_year(1)
# print(date_time1)
# print(date_time1)
# print(date_time2)
# date_time1.sub_month(103)
# date_time1.sub_month(13)
# date_time1.sub_hour(30)
# print(date_time1 + date_time2)
# print(date_time2 - date_time1)
# date_time1.sub_minute(3000)
# date_time1.add_minute(8765)
# print(date_time1)
# date_time1.sub_year(1)
# date_time1.sub_second(100)
# date_time1.sub_day(190)
# print(date_time1)
# print(date_time2.duration_by_days_not_using_time(date_time1))
# print(date_time2.duration_by_days_using_time(date_time1))