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
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


def fidelity_promo(order):
    return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0


def bulk_item_promo(order):
    discount = 0
    for item in order.cart:
        if item.quality >= 20:
            discount += item.total() * .1
    return discount


def large_order_promo(order):
    products = {item.product for item in order.cart}
    if len(products) >= 10:
        return order.total() * 0.07
    return 0


# promos = [fidelity_promo, bulk_item_promo, large_order_promo]
# globals() 返回当前模块的全局符号表
promos = [
    globals()[name] for name in globals()
        if name.endswith('_promo')
        and name != 'best_promo']

def best_promo(order):
    return max(promo(order) for promo in promos)


if __name__ == '__main__':
    joe = Customer('John Doe', 0)
    ann = Customer('Ann Smith', 1100)
    cart = [LINEITEM('banana', 4, .5),
            LINEITEM('apple', 10, 1.5),
            LINEITEM('watermellon', 5, 5.0)]
    print(Order(joe, cart, fidelity_promo))
    print(Order(ann, cart, fidelity_promo))
    banana_cart = [LINEITEM('banana', 30, .5),
            LINEITEM('apple', 10, 1.5)]
    print(Order(joe, banana_cart, bulk_item_promo))
    long_cart = [LINEITEM(str(item_code), 1, 1.0)
                    for item_code in range(10)]
    print(Order(joe, long_cart, large_order_promo))
    print(Order(joe, cart, large_order_promo))
    print(Order(joe, long_cart, best_promo))
