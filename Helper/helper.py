yes_count = 0
for i in range(4):
    answer = input("Yes or no: ")
    if answer == "yes":
        yes_count += 1
        
if yes_count >= 3:print("Well done!")