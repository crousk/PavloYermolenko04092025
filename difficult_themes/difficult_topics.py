# print
#
# some = print
#
# some(555)
# print(some, 555555555)
# print(print, 555555555)
# print(print(), 555555555)
#
# print(id(some))
# print(id(print), 55555555555)
from typing import Callable
from getpass import getpass


def foo(number: int = 6) -> int:
    print(33333333)
    return number + 5


def foo2(arg: str = "kkkk") -> str:
    print(66666666)
    return arg * 2


def foo3() -> str:
    print(100000000000000)
    return 'Hello buddy'


def foo4(arg_1: int, arg_2: int) -> int:
    print(99999999999)
    return arg_1 + arg_2


def call_callable_function(func: Callable, *args, **kwargs):
    print(4444444444444)
    print(args)
    print(kwargs)

    result = func(*args, **kwargs)  # foo()
    print(func, "---->>>", result)
    # print(int("000001D7E36EA2A0", 16))
    return result


# call_callable_function(func=foo, number=55)
# call_callable_function(foo2, 'ggggg')
# # call_callable_function(func=foo2)
# call_callable_function(foo3)
# call_callable_function(foo4, 15, 35)


# #################################################################################################

def call_callable_function_master(func: Callable) -> Callable:
    def inner(*args, **kwargs):
        print(232323232)
        print(args, kwargs)
        print(func)
        print("before call --------------------")
        result = func(*args, **kwargs)
        print("after call --------------------")
        if isinstance(result, int):
            result *= 1000
        return result

    return inner


# foo = call_callable_function_master(func=foo)
# result = foo(number=555)
# print(result)
#
#
# foo2 = call_callable_function_master(func=foo2)
# result = foo2(arg='555+++++')
# print(result)


admin = {
    'login': 'admin',
    'password': '1234'
}


def only_admin_allowed(func: Callable) -> Callable:
    def inner(*args, **kwargs):
        print("before call --------------------")
        user_login = input('Enter your login: ')
        user_password = getpass('Enter your password: ')
        if user_login == admin["login"] and user_password == admin["password"]:
            result = func(*args, **kwargs)
            print("after call --------------------")
            return result

        return {'status': 403}

    return inner


@only_admin_allowed
def final_foo(number: int = 6) -> int:
    print("function final_foo was called")
    return number + 5


@call_callable_function_master
def final_foo333(number: int = 6) -> int:
    print("function final_foo333 was called")
    return number + 6666666666


result = final_foo(23)
print(result)

# result = final_foo333(100)
# print(result)
