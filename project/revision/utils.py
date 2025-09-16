def greet_person(name: str = "Guest") -> str:
    return f"Hello, {name}!"

print(greet_person())


def is_even(number: int) -> bool:
    return number % 2 == 0

print(is_even(4))

def reverse_string(string: str) -> str:
    return string[::-1]

print(reverse_string("Hello"))

def calculate_average(numbers: list[float]) -> float:
    return sum(numbers) / len(numbers)

print(calculate_average([1, 2, 3]))

def add_person_to_list(people: list[str], person: str) -> list[str]:
    new_list = people.copy()
    new_list.append(person)
    return new_list

original = ["Jim", "Katya", "Pavlo"]
updated = add_person_to_list(original, "Anton")

print("Original list:", original)
print("Updated list:", updated)

def count_vowels(text: str) -> int:
    eng_vowels = ["a", "e", "i", "o", "u","A", "E", "I", "O", "U"]
    uk_vowels = ["а", "е", "є", "и", "і", "ї", "о", "у", "ю", "я","А", "Е", "Є", "И", "І", "Ї", "О", "У", "Ю", "Я"]
    count = 0
    for char in text:
        if char in eng_vowels or char in uk_vowels:
            count += 1
    return count

print(count_vowels("Привіт!" "Hello!"))

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5 / 9

print(round(fahrenheit_to_celsius(79), 2))
