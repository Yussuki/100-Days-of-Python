def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")


my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing?
# Looping the code with i's values from 1 to 19
# 2. When is the function meant to print "You got it"?
# When i == 20, in other words, never
# 3. What are your assumptions about the value of i?
# It will never print the "You got it" text, fix would be change the range from range(1,20) to range(1,21)