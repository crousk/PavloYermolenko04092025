from project.revision.functions_utils import is_number_bigger_than_given, get_ticket_price
from project.hw11_decorators.decorator import add, greet
from project.hw12.decorator_with_options import divide_with_rounding

# def test_is_number_bigger_than_given_1():
#     given_number = 5
#     result = is_number_bigger_than_given(given_number)
#     expected_result = False
#     assert result == expected_result
#
# def test_ticket_price_child():
#     assert get_ticket_price(5) == 0.0 # free
#
# def test_ticket_price_teenager():
#     assert get_ticket_price(10) == 50.0 # 50% discount
#
# def test_ticket_price_adult():
#     assert get_ticket_price(38) == 100.0 # full price
#
# def test_ticket_price_senior():
#     assert get_ticket_price(67) == 70.0 # 30% discount
#
# def test_add():
#     assert add(1, 6) == {"result": 7}
#
# def test_greet():
#     assert greet("Pavlo") == {"result": "Hi, Pavlo!"}


def test_divide_with_rounding():
    assert divide_with_rounding(1, 3) == 0.33