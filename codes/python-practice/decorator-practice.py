"""
Practice code for decorators in python
"""

from boltons.funcutils import wraps


def modify_function_method(input_one=None):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            print('omg, we are hitting ' + str(input_one) + "s now")
            f(*args, **kwargs)
        return wrapper
    return decorator


@modify_function_method(3)
def goofy():
    print('mama mia')


goofy()
