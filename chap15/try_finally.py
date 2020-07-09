def run():
    try:
        print('ok')
        return 1
        print('not run')
    except ZeroDivisionError:
        msg = 'do not divide by zero'
        print('ZeroDivisionError accurs')
    finally:
        print('always run')
    print('not run')

run()
