def func_decorator(func):
    def wrapper(*args, **kwargs):
        print('---Что-то делаем перед вызовом функции---')
        res = func(*args, **kwargs)
        print('---Что-то делаем после вызова функции---')
        return res
    return wrapper


@func_decorator
def some_func(title, tag):
    # print(f'Вызов функции {some_func.__name__}')
    print(f'Title = {title}, tag = {tag}')
    return f'<{tag}>{title}</{tag}>'


# some_func = func_decorator(some_func)
print(some_func('111', '222'))
