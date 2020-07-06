class Quantity:
    __counter = 0
    def __init__(self):
        cls = self.__class__
        prefix = cls.__name__
        self.name = '_{}#{}'.format(prefix, cls.__counter)
        cls.__counter += 1 # 线程安全？

    def __set__(self, instance, val):
        if val > 0:
            setattr(instance, self.name, val)
        else:
            raise ValueError('val must be > 0')

    def __get__(self, instance, owner):
        if isinstance is None:
            return self
        else:
            return getattr(instance, self.name)


class LineItem:

    weight = Quantity()
    price = Quantity()

    def __init__(self, desc, weight, price):
        self.desc = desc
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

if __name__ == '__main__':
    l = LineItem('apple', 2, 1.3)
    print(l.subtotal())
