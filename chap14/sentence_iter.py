import re
import reprlib
from collections import abc


RE_WORD = re.compile('\w+')


class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        return SentenceIterator(self.words)


class SentenceIterator():
    
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word

    def __iter__(self): # 这个例子中 __iter__ 也可以不实现，但这样就通不过 abc.Iterator 检查了
        return self


if __name__ == '__main__':
    s = Sentence("you are a good girl")
    for word in s:
        print(word, end=' ')
    print()
    it = iter(s)
    print(isinstance(s, abc.Iterable))
    print(isinstance(s, abc.Iterator))
    print(isinstance(it, abc.Iterator))
