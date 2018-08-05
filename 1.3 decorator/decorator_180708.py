# -*- coding: utf-8 -*-

import functools

# decorator with no args
def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('call %s' % func.__name__)
        return func(*args, **kwargs)
    return wrapper


# decorator with args
def decorator_args(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('call %s' % func.__name__)
            return func(*args, **kwargs)
        return wrapper
    return decorator