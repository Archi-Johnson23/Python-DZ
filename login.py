creds = {'Саша': '11', 'Петя': '22'}
def auth_required(func):
    def wrapper_decorator(*args, **kwargs):
        name = input('Введите логин:')
        password = input('Введите пароль:')
        if name in creds and password == creds[name]:
            print('верно')
        else:
            print('Неверно')
        #  key in creds
        # d = creds.items()
        #     print(d)
        # value = func(*args, **kwargs)
        # return value
        value = func(*args, **kwargs)
        return value
    return wrapper_decorator
@auth_required
def some_func(a, b):
    return(a + b)
print(some_func)
      

