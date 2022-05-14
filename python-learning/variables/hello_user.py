name = input("What's your name?\n")
birth_year = input("What's your birth year?\n")
age = 2022 - int(birth_year)
print("Hello " + name)
print("your age is" + age)
# checking the age of the user
if (age > 18)
    is_eligible = True
    print("You are eligible")
else
    is_eligible = False 
    print("You are too young")
    
