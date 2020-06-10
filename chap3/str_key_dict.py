class strKeyDict0(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()


import collections


class strKeyDict(collections.UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]
    
    def __contains__(self, key):
        return str(key) in self.data 

    def __setitem__(self, key, item):
        self.data[str(key)] = item


if __name__ == '__main__':
    d = strKeyDict([('2', 'two'), ('4', 'four')])
    print(d[2])
    print(d[4])
    print(d.get(2))
    print(2 in d)
