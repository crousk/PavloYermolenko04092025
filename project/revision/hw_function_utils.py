from logtail import LogtailHandler
import logging

handler: LogtailHandler = LogtailHandler(
    source_token= "8G8mYATdJUPLTB9nf994yaic",
    host= "s1516019.eu-nbg-2.betterstackdata.com",
)

logger: logging.Logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.handlers = []
logger.addHandler(handler)


def hello_buddy():
    return "Hello, Buddy!"

print(hello_buddy())


def the_biggest_number(lst):
    nums = []
    for x in lst:
        nums.append(x)
    return max(nums) if nums else 0

print("The biggest number is", the_biggest_number([1, 2, 3, 4, 5, 10, 15, 17, 83]))


def multiply_nums(a: float, b: float) -> float:
    result = a * b
    logger.info(f"Multiplying {a} by {b}. Result: {result}")
    return result








