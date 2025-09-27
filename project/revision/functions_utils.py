def is_number_bigger_than_given(candidate_number: float, threshold: float = 10) -> bool:
    """according to the task #327U4183247892134879127894"""
    return candidate_number > threshold

def add_salt_to_list(given_list: list) -> None:
    """WARNING! list is being modified globally"""


def get_ticket_price(age:int) -> float:
    base_price = 100

    if age < 6:
        base_price = 0
        return base_price
    elif 6 <= age <= 17:
        base_price = base_price / 2
        return base_price
    elif 18 <= age <= 59:
        return base_price
    else:
        return base_price * 0.7

