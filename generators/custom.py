def get_sequence(start: int = 0):
    while True:
        yield start
        print('bla bla')
        start += 1


sequence = get_sequence(25)
print(sequence)

print(next(sequence))
print(next(sequence))
print(next(sequence))
print(next(sequence))
print(next(sequence))
print(next(sequence))
print(next(sequence))
print(next(sequence))
print(next(sequence))

print('do something')
print(next(sequence))
print(next(sequence))
print(next(sequence))
print(next(sequence))
print(next(sequence))
print(next(sequence))
print(next(sequence))
print(next(sequence))
print(next(sequence))
