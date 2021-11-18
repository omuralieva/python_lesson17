def our_decorator(function_to_decorate):
    def wrapper_around_our_function(*args):
        print('Привет!')
        function_to_decorate(*args)
        print('Конец функции, пока!')
    return wrapper_around_our_function


@our_decorator
def our_function(x, y):
    print(x + ' ' + y)


our_function('Dont Worry!', 'Be Happy!')
