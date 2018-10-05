# 策略模式 ==================================================================
from abc import ABC, abstractmethod
from collections import namedtuple
Customer = namedtuple('Customer', 'name fidelity')

class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
    def total(self):
        return self.quantity * self.price

class Order:
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion
    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = 'order total: {:.2f}, due: {:.2f}'
        return fmt.format(self.total(), self.due())

class Promotion(ABC):
    @abstractmethod
    def discount(self, order):
        pass

class FidelityPromo(Promotion):
    def discount(self, order):
        return order.total() * .05 if order.customer.fidelity >= 1000 else 0

class BulkItemPromo(Promotion):
    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * .1
        return discount
class LargeOrderPromo(Promotion):
    def discount(self, order):
        distinct_items = {item.name for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * .07
        return 0

joe = Customer('John Doe', 0)
zcx = Customer('zhaochenxi', 1100)
zsx = Customer('zhangshuxia', 999)
cart = [
    Product('banana', 4, .5),
    Product('apple', 10, 1.5),
    Product('orange', 5, 5.0)
]
# print(Order(joe, cart, FidelityPromo()))
# print(Order(zcx, cart, FidelityPromo()))

banana_cart = [
    Product('banana', 30, .5),
    Product('apple', 10, 1.5)
]
# print(Order(joe, banana_cart, BulkItemPromo()))

long_order = [Product(str(item_code), 1, 1.0) for item_code in range(10)]
print(Order(joe, long_order, LargeOrderPromo()))
print(Order(joe, cart, LargeOrderPromo()))
