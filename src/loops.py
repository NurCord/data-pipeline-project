import os
os.system("clear")

###
# Loops in Python

print("___________Loops__________")

# Bucle while

count = 0
while count < 5:
    print("Count is:", count)
    count += 1
    if count == 3:
        continue
else:
    print("The loop has finished executing")

while True:
    print("This will run forever unless you break it")
    # The break statement will exit the loop
    break
else:
    print("This will never be printed because the loop was broken")


# Bucle for
print("___________For Loop__________")