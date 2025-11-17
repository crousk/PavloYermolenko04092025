from revision.functions_utils import is_number_bigger_than_given, add_salt_to_list
from services.logger import logger


def main():
    result = is_number_bigger_than_given(candidate_number=5)
    logger.info(f"Function is_number_bigger_than_given was called", extra={
        "candidate_number": 5,
        "result": result

    })
    logger.debug(f"Function is_number_bigger_than_given was called", extra={
        "candidate_number": 5,
        "result": result

    })
    logger.error(f"Function is_number_bigger_than_given was called", extra={
        "candidate_number": 5,
        "result": result

    })

    result = is_number_bigger_than_given(candidate_number=66, threshold=1)


    given_list = []
    add_salt_to_list(given_list)
    add_salt_to_list(given_list)
    add_salt_to_list(given_list)
    add_salt_to_list(given_list)
    add_salt_to_list(given_list)


if __name__ == "__main__":
    main()
