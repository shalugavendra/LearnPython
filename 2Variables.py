# Variable = A container for a value (string, integer, float, boolean)
#            A variable behaves as if it was the value it contains
# Strings
first_name = "Singh"
email = "qwe123@fake.xom"
print(first_name)

print(f"Hello {first_name}")

print(f"My email is: {email}")

# Integers
age = 24
num_of_students = 30
print(f"Your are {age} year old")
print(f"Your class has {num_of_students} students")

# Float
price = 10.25

print(f"The price is ${price}")

# Boolean
is_student = False

print(f"Are you a student ?: {is_student}")

if is_student:
    print("You are a student")
else:
    print("You are not a stident")

user_name = "Bro Code"
year = 2024
pi = 3.14
is_admin = False
print(f"Your username is {user_name} and current year is {year} where value for pi is {pi} and it's {is_admin}")
if is_admin:
    print("You are admin")
else:
    print("You are not admin")


