list_of_items = [66, 55, 99,         55, 666, 33      ]
#                                   [            ]

# first = list_of_items[0]
# second = list_of_items[1]
# third = list_of_items[2]

first, second, third, *rest = list_of_items

print(first, second, third, rest)
print(first, second, third, *rest)
print(first)
