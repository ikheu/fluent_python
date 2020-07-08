class LookingGlass:
    
    def __enter__(self):
        import sys
        self.origin_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return 'hi'

    def reverse_write(self, text):
        self.origin_write(text[::-1])

    def __exit__(self, exc_type, exc_value, traceback):
        import sys
        sys.stdout.write = self.origin_write
        if exc_type is ZeroDivisionError:
            print('please do not divide zero')
            return True

if __name__ == '__main__':
    with LookingGlass() as l:
        print(l)
        print('hello')
        1/0
    print('hello')
    