import contextlib

@contextlib.contextmanager
def looking_glass():
    import sys
    origin_write = sys.stdout.write
    def reverse_write(text):
        origin_write(text[::-1])
    sys.stdout.write = reverse_write
    msg = ''
    try:
        yield 'hi'
    except ZeroDivisionError:
        msg = 'do not divide by zero'
    finally:
        sys.stdout.write = origin_write
        if msg:
            print(msg)

if __name__ == '__main__':
    with looking_glass() as l:
        print(l)
        print('hello')
        s[1] = 10
        1/0
    print('hello')
    