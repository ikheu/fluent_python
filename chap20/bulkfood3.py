class Quantity:
    def __init__(self, name):
        self.name = name

    def __set__(self, instance, val):
        
        if val > 0:
            instance.__dict__[self.name] = val
        else:
            raise ValueError('val must be > 0')


class LineItem:

    weight = Quantity('weight')
    price = Quantity('price')

    def __init__(self, desc, weight, price):
        self.desc = desc
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

if __name__ == '__main__':
    l = LineItem('apple', 2, 1.3)
    print(l.subtotal())
    print(l.__dict__)
    print(LineItem.__dict__)
