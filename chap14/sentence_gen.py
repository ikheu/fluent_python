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
        for word in self.words:
            yield word


if __name__ == '__main__':
    s = Sentence("you are a good girl")
    for word in s:
        print(word, end=' ')
    print()
    print(next(s))

    print(isinstance(s, abc.Iterable))
    print(isinstance(s, abc.Iterator))
    print(isinstance(it, abc.Iterator))
