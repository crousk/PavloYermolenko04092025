from functions_utils import is_number_bigger_than_given, add_salt_to_list

def main():
    result = is_number_bigger_than_given(candidate_number=5)
    print(result)

    result = is_number_bigger_than_given(candidate_number=5, threshold=1)
    print(result)

    given_list = []
    add_salt_to_list(given_list)
    print(given_list)

if __name__ == "__main__":
    main()
