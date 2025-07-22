subjects = ["Bengali", "English", "Physics", "Math", "Coding", "Singing",
            "Football", "Chess"];

new_subject = ["Guiter", "Business", "Karate", "Accounts",
            "SpokenEnglish","Swiming"];

subjects = subjects + new_subject + ["Painting", "Geography"];

# print(subjects)

subjects.remove("Physics");

# print(subjects);

subjects.insert(10,"French");
# print(subjects)

# print(subjects);
# print(subjects[0]);
# print(subjects[1]);
# print(subjects[2]);
# print(subjects[3]);

# print(subjects[2:]);

# isQuerySubjectAvailable = "Cricket" in subjects;

# print(isQuerySubjectAvailable);



# jokhon amra right to left index cont kori then -1 theke start hoi and -2, -3 evabe barte thake
# print(subjects[-1])


numbers = [7, 4, 2, 0, 7, 5,298, 2, 7];

copy_numbers = numbers.copy();


index_of_value = numbers.index(298);

print(index_of_value);
# print(f"copy numbers: {copy_numbers}");

numbers.sort();

# print(f"choto_theke_boro: {numbers}");

# numbers.reverse();

# print(f"boro_theke_choto: {numbers}");

# numbers.clear(); 

# count_number = numbers.count(7);
# print(count_number)

# print(numbers);



# assending order (choto theke boro)
# decending order (boro theke choto)

