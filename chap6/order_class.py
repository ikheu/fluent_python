from abc import ABC, abstractmethod
from collections import namedtuple


Customer = namedtuple('Customer', 'name fidelity')


class LINEITEM:
    def __init__(self, product, quality, price):
        self.product = product
        self.quality = quality
        self.price = price

    def total(self):
        return self.quality * self.price


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
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


# 即使不继承 ABC，不使用 abstractmethod 也不会出错。之所以这样做是为了表明所使用的模式 @1
class Promotion(ABC):
    @abstractmethod
    def discount(self, order):
        """ 折扣金额 """


class FidelityPromo(Promotion):
    def discount(self, order):
        return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0


class BulkItemPromo(Promotion):
    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quality >= 20:
                discount += item.total() * .1
        return discount


class LargeOrderPromo(Promotion):
    def discount(self, order):
        products = {item.product for item in order.cart}
        if len(products) >= 10:
            return order.total() * 0.07
        return 0

class FooPromo(Promotion): 
    def discount(self, order): # 不实现 discount 方法会报错
        pass


if __name__ == '__main__':
    joe = Customer('John Doe', 0)
    ann = Customer('Ann Smith', 1100)
    cart = [LINEITEM('banana', 4, .5),
            LINEITEM('apple', 10, 1.5),
            LINEITEM('watermellon', 5, 5.0)]
    print(Order(joe, cart, FidelityPromo()))
    print(Order(ann, cart, FidelityPromo()))
    banana_cart = [LINEITEM('banana', 30, .5),
            LINEITEM('apple', 10, 1.5)]
    print(Order(joe, banana_cart, BulkItemPromo()))
    long_cart = [LINEITEM(str(item_code), 1, 1.0)
                    for item_code in range(10)]
    print(Order(joe, long_cart, LargeOrderPromo()))
    print(Order(joe, cart, LargeOrderPromo()))

    foo = FooPromo()
    