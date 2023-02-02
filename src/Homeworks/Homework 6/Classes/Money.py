class MoneyError(Exception):
    pass


class Money:
    exchange = {"AMD": 1, "RUB": 5.8, "USD": 400, "EUR": 430}

    def __init__(self, amount: int, currency: str):
        if isinstance(amount, (int, float)) and amount >= 0 and currency in Money.exchange.keys():
            self.__amount = amount
            self.__currency = currency
        else:
            raise MoneyError

    def __repr__(self):
        return str(self.__amount) + " " + self.__currency

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        if isinstance(value, (int, float)) and value >= 0:
            self.__amount = value
        else:
            raise MoneyError(f"Amount can't be negative {value}")

    @property
    def currency(self):
        return self.__currency

    @currency.setter
    def currency(self, value):
        if value in Money.exchange.keys():
            self.__currency = value
        else:
            raise MoneyError(f"There is no such currency {value}")

    def conversation(self, new_curr: str):
        curr = self.currency
        self.currency = new_curr
        self.amount = (self.amount / Money.exchange[self.currency]) * Money.exchange[curr]
        return self

    def __add__(self, other):
        x = Money(other.amount, other.currency)
        x.conversation(self.currency)
        self.amount += x.amount

    def __sub__(self, other):
        x = Money(other.amount, other.currency)
        x.conversation(self.currency)
        self.amount -= x.amount

    def __truediv__(self, other):
        x = Money(other.amount, other.currency)
        x.conversation(self.currency)
        self.amount /= x.amount

    def __eq__(self, other):
        x = Money(other.amount, other.currency)
        x.conversation(self.currency)
        return self.amount == x.amount

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        x = Money(other.amount, other.currency)
        x.conversation(self.currency)
        return self.amount < x.amount

    def __gt__(self, other):
        x = Money(other.amount, other.currency)
        x.conversation(self.currency)
        return self.amount > x.amount

    def __le__(self, other):
        x = Money(other.amount, other.currency)
        x.conversation(self.currency)
        return self.amount <= x.amount

    def __ge__(self, other):
        x = Money(other.amount, other.currency)
        x.conversation(self.currency)
        return self.amount >= x.amount


# m = Money(2, "AMD")
# k = Money(600, "USD")
# #
# print(m <= k)
# print(m >= k)
# print(m > k)
# print(m < k)
# print(m == k)
# k.conversation("EUR")
# print(k)
# print("yay")
# print(m)
# # m.amount = -125
# m / k
# print(m)
# m + k
# print(m)