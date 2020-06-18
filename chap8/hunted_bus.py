class Bus:
    def __init__(self, passengers=[]):
        self.passengers = passengers
        
    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


if __name__ == '__main__':
    bus1 = Bus(['alice', 'bill'])
    print(bus1.passengers)

    bus2 = Bus()
    bus2.pick('carrie')
    print(bus2.passengers)

    bus3 = Bus()
    print(bus2.passengers) # 诡异的事情发生了
