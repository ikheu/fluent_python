from collections import abc
import keyword
from osconfeed import load

class FrozenJson:

    def __init__(self, mapping):
        self.__data = {}
        for k, v in mapping.items():
            if keyword.iskeyword(k):
                k += '_'
            self.__data[k] = v

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            return FrozenJson.build(self.__data[name])

    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        return obj

class FrozenJson2:
    def __new__(cls, arg):
        if isinstance(arg, abc.Mapping):
            return super().__new__(cls)
        elif isinstance(arg, abc.MutableSequence):
            return [cls(item) for item in arg]
        return arg


    def __init__(self, mapping):
        self.__data = {}
        for k, v in mapping.items():
            if keyword.iskeyword(k):
                k += '_'
            self.__data[k] = v

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            return FrozenJson.build(self.__data[name])


if __name__ == '__main__':
    raw_feed = load()
    feed = FrozenJson(raw_feed)
    print(len(feed.Schedule.speakers))
    talk = feed.Schedule.events[40]
    print(type(talk))
    print(talk.name)
    print(talk.speakers)
    print(talk.flavor)

