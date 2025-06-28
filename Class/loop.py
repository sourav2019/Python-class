for i in range(10):
    print(f"{5 * i + 1} Hello");


# user_table = int(input("Enter the table number you want: "));

# for i in range(10):
#     print(f"{user_table} X {i + 1} = {user_table * (i + 1)}");

number_calculate_max = int(input("Enter the range value: "));
number_divide_by = int(input("Enter the the number you want to divide with: "))
    
for i in range(number_calculate_max):
    if(i+1) % number_divide_by == 0: print(i+1);
    else: print("Divition is not possible");
