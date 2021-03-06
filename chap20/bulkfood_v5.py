import model_v5 as model


class LineItem:
    description = model.NonBlank()
    weight = model.Quantity()
    price = model.Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.price * self.weight

if __name__ == '__main__':
    item = LineItem('apple', 1.4, 2)
    print(item.subtotal())
    print(LineItem.price.storage_name)
