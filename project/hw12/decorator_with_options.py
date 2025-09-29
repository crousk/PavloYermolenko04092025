def round_result(ndigits: int):
    def decorator(func):
        def wrapper(*args, **kwargs):
                result = func(*args, **kwargs)
                if isinstance(result, (int, float)):
                    return round(result, ndigits)
                return result
        return wrapper
    return decorator

@round_result(2)
def divide_with_rounding(a, b):
    return a / b


print(divide_with_rounding(1, 3))