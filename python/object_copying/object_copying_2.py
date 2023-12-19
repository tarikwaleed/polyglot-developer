from pprint import pprint
person = {
    "name": "tarik",
    "age": 28,
    "address": {"city": "october", "state": "giza", "postal_code": 78964},
    "favourite_colors": ["navy", "tan", "grey"],
}
person2=person
person["address"]["city"]="not october"
pprint(f"==>> person2: {person2}")

