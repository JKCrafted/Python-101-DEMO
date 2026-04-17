
target_loops = int(input("How many loops do you want to perform?\n"))

for new_number in range(target_loops):
    print("For loop no."+str(new_number+1))
    
print("")

current_number = 1
    
while current_number <= target_loops:
    print("While loop no."+str(current_number))
    current_number += 1