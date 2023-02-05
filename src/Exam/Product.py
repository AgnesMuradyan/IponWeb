class ProductError(Exception):
    pass


class InventoryError(Exception):
    pass


# products = {}


class Product:
    id_list = []

    def __init__(self, id, price, quantity):

        if not isinstance(id, int) or id in Product.id_list:
            raise ProductError
        else:
            self.__id = id
            Product.id_list.append(id)
        if isinstance(price, int) and price > 0:
            self.__price = price
        else:
            raise ProductError
        if isinstance(quantity, int) and quantity >= 0:
            self.__quantity = quantity
        else:
            raise ProductError

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if not isinstance(value, int) or value in Product.id_list:
            raise ProductError
        else:
            self.__id = value
            Product.id_list.append(value)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if isinstance(value, int) and value > 0:
            self.__price = value
        else:
            raise ProductError

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        if isinstance(value, int) and value >= 0:
            self.__quantity = value
        else:
            raise ProductError

    def __repr__(self):
        return f"Id : {self.__id}, Price : {self.__price}, Quantity : {self.__quantity} "

    def buy(self, count):
        if count > self.__quantity:
            raise ProductError
        else:
            self.__quantity -= count

    # def get_by_id(self, my_int):
    #     if my_int not in Product.id_list:
    #         raise ProductError
    #     else:
    #         return


class Inventory:
    def __init__(self, my_list=None):
        if my_list is None:
            self.__my_list = []
        else:
            if isinstance(my_list, list) and all(isinstance(x, Product) for x in my_list):
                self.__my_list = my_list
        self.__id_list = {}
        for i in self.__my_list:
            self.__id_list[i.id] = i

    @property
    def id_list_inv(self):
        return self.__id_list

    @property
    def my_list(self):
        return self.__my_list

    @my_list.setter
    def my_list(self, value):
        if isinstance(value, list) and all(isinstance(x, Product) for x in value):
            self.__my_list = value
            # self.

    def __repr__(self):
        curr = "Products in inventory are : " + "\n"
        for i in self.__my_list:
            curr += f"Id : {i.id}, Price : {i.price}, : Quantity: {i.quantity}" + "\n"
        return curr

    def sum_of_products(self):
        sum = 0
        for i in self.__my_list:
            sum += i.price * i.quantity
        return sum

    def get_by_id(self, new_id):
        if new_id in self.__id_list.keys():
            return self.__id_list[new_id]
        else:
            raise InventoryError

    # extra
    def add_item(self, new_prod):
        if isinstance(new_prod, Product):
            self.__my_list.append(new_prod)
            self.__id_list[new_prod.id] = new_prod
        else:
            raise ProductError

    # extra
    def all_items_count(self):
        count = 0
        for i in self.__my_list:
            count += i.quantity
        return count


p1 = Product(1, 200, 3)
p2 = Product(2, 300, 2)
p3 = Product(3, 400, 1)
p4 = Product(4, 100, 5)
# print(p1)
# print(p2)
# print(p3)
# print(p4)
inv = Inventory([p1, p2, p3])
inv.add_item(p4)

print(inv)
print(inv.id_list_inv)
print(inv.all_items_count())
# print(inv.sum_of_products())
# print(inv.get_by_id(3))
