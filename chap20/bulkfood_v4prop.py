def quantity():
    try:
        quantity.counter += 1
    except AttributeError:
        quantity.counter = 0
    name = '_{}#{}'.format('quantity', quantity.counter)

    def qty_getter(instance):
        return getattr(instance, name)

    def qty_setter(instance, value):
        if value > 0:
            setattr(instance, name, value)
        else:
            raise ValueError('value must > 0')

    return property(qty_getter, qty_setter)
