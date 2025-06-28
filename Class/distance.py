distance = int(input("Enter distance: "))
print(f"your enter:{distance}")

if distance <= 2 or distance == 1:
    print("hete jabo")
elif distance > 2 and distance < 5:
    print("cycle e jabo")
elif distance > 5 and distance < 10:
    print("bike e jabo")
elif distance > 10 and distance < 15:
    print("gari te jabo")
elif distance > 15:
    print("train e jano")
else:
    print("ami ajbona")
