# input() = A function that prompts the user to enter data
#           Returns the entered data as a string

name = input("What is your name? ")
age = int(input("What's your age? "))

print(name)
print(f"Hi {name}")

#age = int(age)
age = age + 1
# print(age)  // it will give error because input function saves value in str()


print(age)