import re
import reprlib
from collections import abc


RE_WORD = re.compile('\w+')


class Sentence:

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for match in RE_WORD.finditer(self.text):
            yield match.group()


if __name__ == '__main__':
    s = Sentence("you are a good girl")
    for word in s:
        print(word, end=' ')
    print()

    print(isinstance(s, abc.Iterable))
    print(isinstance(s, abc.Iterator))
