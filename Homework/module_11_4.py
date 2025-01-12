from pprint import pprint
import re


def get_type(obj):
    string = str(type(obj))
    pattern_1 = re.compile("<class '")
    pattern_2 = re.compile("'>")
    for i in (pattern_1, pattern_2):
        string = i.sub('', string)
    return string


def get_attr(obj):
    try:
        return [attr for attr in dict(obj.__dict__)]
    except AttributeError:
        return ['None']


def get_methods(obj):
    return [i for i in dir(obj) if i not in get_attr(obj) and '__' not in i]


def introspection_info(obj):
    results = {}
    results['type'] = get_type(obj)
    results['attributes'] = get_attr(obj)
    results['methods'] = get_methods(obj)
    # results['module'] =
    return results


class TestClass:
    def __init__(self):
        self.attr1 = 'Hello'
        self.attr2 = 'World'

    def do_sth(self):
        print('do sth')


instance = TestClass()
instance_info = introspection_info(instance)
print(instance_info)
print(dir(instance))
number_info = introspection_info(42)
print(number_info)
print(dir(42))



# {'type': 'int', 'attributes': [...], 'methods': ['__abs__', '__add__', ...],
# 'module': '__main__'}