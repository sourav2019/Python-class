manas = {
    "name": "Manas",
    "age": 25,
    "city": "kolkata",
    "hobby": ["singing", "dancing", "traveling"],
    "isBachelor": True
}

# print(manas)

# manas_age = manas.get("job", "this property does not exist!");
# # print(manas_age)


# keys = manas.keys();
# print(keys);

# manas_hobby = manas.get("hobby");
# print(manas_hobby);

manas["age"] = 45

manas.pop("age")
# print(manas)

manas.clear()

manas.values()

# print(manas)

# print(manas.get("age"));

# manas.update({"age": 26, "gender": "male"})

# print(manas)


person = {
    "name": "akash",
    "age": 20
}

# del person["age"]
# person.pop("age")

update_varible = {"age": 22, "city": "kolkata"};

person.update(update_varible);

copied_person = person.copy();

# print(f"Person {person}")


print(copied_person)
