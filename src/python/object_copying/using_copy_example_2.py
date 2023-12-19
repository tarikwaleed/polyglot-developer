from copy import copy

print("copying using copy()")
favourite_colors = ["grey", "navy", "tan"]
original = {
    "name": "tarik",
    "age": 28,
    "address": {"city": "october", "state": "giza", "postal_code": 78964},
    "favourite_colors": favourite_colors,
}

the_copy = copy(original)
print(id(favourite_colors))
print(id(original["favourite_colors"]))
print(id(favourite_colors)==id(original["favourite_colors"]))

