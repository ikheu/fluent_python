import re
import reprlib
from collections import abc


RE_WORD = re.compile('\w+')

"""
实现了 __iter__ 的对象是可迭代的。实现了 __getitem__ 但未实现 __iter__ 的对象，会在使用时特殊处理：遍历该对象时创建一个迭代器，按顺序获取元素。
"""

class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __iter__(self):
        return iter(self.words)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

if __name__ == '__main__':
    s = Sentence("you are a good girl")
    print(len(s))
    print(s[0])
    for word in s:
        print(word, end=' ')
    
    # print()
    print(iter(s))
    print(dir(iter(s)))
    print(isinstance(s, abc.Iterable))
