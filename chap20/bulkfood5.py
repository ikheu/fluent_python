import model_v5 as model

class LineItem:

    weight = model.Quantity()
    price = model.Quantity()

    def __init__(self, desc, weight, price):
        self.desc = desc
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

if __name__ == '__main__':
    l = LineItem('apple', 2, 1.3)
    print(l.subtotal())
