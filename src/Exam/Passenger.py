class PassengerError(Exception):
    pass


class HotelError(Exception):
    pass


class Hotel:
    list_room = ["penthouse", "single", "double"]

    def __init__(self, city, rooms=None):
        if isinstance(city, str):
            self.__city = city
        else:
            raise HotelError
        if rooms is None:
            rooms = {}
        else:
            if isinstance(rooms, dict) and all(x in Hotel.list_room for x in rooms.keys()):
                self.__rooms = rooms
            else:
                raise HotelError

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, value):
        if isinstance(value, str):
            self.__city = value
        else:
            raise HotelError

    @property
    def rooms(self):
        return self.__rooms

    @rooms.setter
    def rooms(self, value):
        if isinstance(value, dict) and all(x in Hotel.list_room for x in value.keys()):
            self.__rooms = value
        else:
            raise HotelError

    def __repr__(self):
        curr = f"City : {self.__city}" + "\n"
        for i, v in self.__rooms.items():
            curr += f"room : {i}, count : {v}" + "\n"
        return curr

    def free_room_list(self, typee):
        if typee in self.__rooms.keys():
            return self.__rooms[typee]
        else:
            raise HotelError

    def reserve_rooms(self, typee, countt):
        if typee not in self.__rooms.keys():
            print("Room doesn't exist")
            return False
        elif self.__rooms[typee] < countt:
            print("There is not so many free rooms")
            return False
        else:
            self.__rooms[typee] -= countt
            if self.__rooms[typee] == 0:
                del self.__rooms[typee]


class Passenger:
    def __init__(self, name, city, rooms=None):
        if isinstance(name, str):
            self.__name = name
        else:
            raise PassengerError
        if isinstance(city, str):
            self.__city = city
        else:
            raise PassengerError
        if rooms is None:
            self.rooms = {}
        else:
            if isinstance(rooms, dict):
                self.__rooms = rooms
            else:
                raise PassengerError

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            raise PassengerError

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city):
        if isinstance(city, str):
            self.__city = city
        else:
            raise PassengerError

    @property
    def rooms(self):
        return self.__rooms

    @rooms.setter
    def rooms(self, rooms):
        if isinstance(rooms, dict):
            self.__rooms = rooms
        else:
            raise PassengerError

    def __repr__(self):
        curr = f"Name : {self.__name}, City :  {self.__city} " + "\n"
        for i, v in self.__rooms.items():
            curr += f"room : {i}, count : {v}" + "\n"
        return curr

    def add_room(self, typee, count):
        if typee in Hotel.list_room:
            if typee in self.__rooms.keys():
                self.__rooms[typee] += count
            else:
                self.__rooms[typee] = count


def book(passenger, hotel, room_count):
    if room_count[0] in hotel.rooms.keys():
        if hotel.free_room_list(room_count[0]) >= room_count[1]:
            hotel.reserve_rooms(room_count[0], room_count[1])
            passenger.add_room(room_count[0], room_count[1])
        else:
            raise PassengerError
    else:
        raise PassengerError


p1 = Passenger("Agnes", "yerevan")
p2 = Passenger("Magda", "Gyumri")
p3 = Passenger("Ani", "Kapan")
h = Hotel("yerevan", {"single": 4, "penthouse": 10, "double": 2})

book(p1, h, ["single", 2])
book(p2, h, ["penthouse", 2])


print(p1)
print(p2)
print(h)
