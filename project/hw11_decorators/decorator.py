def as_dict(func):
    def wrapper(*args, **kwargs):
        function_result = func(*args, **kwargs)
        return {"result": function_result}
    return wrapper


@as_dict
def add(a, b):
    return a + b


@as_dict
def greet(name):
    return f"Hello, {name}!"


print(add(1, 6))
print(greet("Pavlo"))