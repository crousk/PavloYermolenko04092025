from uuid import uuid4



def is_number_bigger_than_given(candidate_number: float, threshold: float = 10) -> bool:
    """according to the task #327U4183247892134879127894"""
    return candidate_number > threshold


def add_salt_to_list(given_list: list) -> None:
    """WARNING! list is being modified globally"""
    identifier = uuid4().hex
    print(identifier)
    given_list.append(identifier)





