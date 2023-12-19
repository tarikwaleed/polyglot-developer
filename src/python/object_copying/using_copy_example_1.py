from copy import copy

print("copying using copy()")
original = {
    "name": "tarik",
    "age": 28,
    "address": {"city": "october", "state": "giza", "postal_code": 78964},
    "favourite_colors": ["navy", "tan", "grey"],
}

print(f"original location in memory:{id(original)}")
the_copy = copy(original)
print(f"the_copy location in memory:{id(the_copy)}")
print(f"same locaiton? {id(original)==id(the_copy)}")

# ? changes in top-level structure
print("changes in top-level structure")
original["name"] = "not tarik"  # will affect the copy
print(f'==>> original["name"]: {original["name"]}')
print(f'==>> the_copy["name"]: {the_copy["name"]}')

# ? changes in nested structure
print("changes in nested structure")
original["address"]["city"] = "not october"  # will affect the copy
print(f'==>> original["address"]["city"]: {original["address"]["city"]}')
print(f'==>> the_copy["address"]["city"]: {the_copy["address"]["city"]}')

# copying dictionries using assignment operator will create a shallow copy
# so changes in origianl will affect the copy
# whether you are changing in the top-level or the nested elements
