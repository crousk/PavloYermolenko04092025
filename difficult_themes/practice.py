from functools import lru_cache
import time


@lru_cache(maxsize=2)
def get_number_powered(number: int) -> int:
    time.sleep(1)
    result = number ** 2
    print(f"get_number_powered was called: {number=};{result=}")
    return result




print(get_number_powered(2))
print(get_number_powered(2))
print(get_number_powered(2))
print(get_number_powered(2))
print(get_number_powered(2))
print(get_number_powered(2))
print(get_number_powered(5))
print(get_number_powered(2))
print(get_number_powered(2))
print(get_number_powered(3))
print(get_number_powered(5))
print(get_number_powered(2))

