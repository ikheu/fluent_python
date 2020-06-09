import collections


Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamons clubs hearts'.split()

    def __init__(self):
        self._card = [Card(rank, suit) for suit in self.suits
                                       for rank in self.ranks]
    
    def __len__(self):
        return len(self._card)

    def __getitem__(self, position):
        return self._card[position]


if __name__ == '__main__':
    # 支持 len
    deck = FrenchDeck()
    print(len(deck))
    # 支持 [] 操作
    print(deck[1])
    # 支持切片与迭代
    for item in deck[0:10]:
        print(item)
    # 支持迭代搜索
    print(Card('Q', 'hearts') in deck)
