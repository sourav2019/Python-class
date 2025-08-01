manas = {
    "name": "Manas",
    "age": 25,
    "city": "kolkata",
    "hobby": ["singing", "dancing", "traveling"],
    "isBachelor": True
}

print(manas)

# manas_age = manas.get("job", "this property does not exist!");
# # print(manas_age)


# keys = manas.keys();
# print(keys);

# manas_hobby = manas.get("hobby");
# print(manas_hobby);

manas["age"] = 45;

manas.pop("age");
print(manas);

manas.clear();

manas.values();

print(manas)

# print(manas.get("age"))
