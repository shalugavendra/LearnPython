# TypeCasting = The process of converting a variable from one data type to another
# TypeCasting functions are str(), int(), float(), bool()
name = "Bro Code"
age = 25
gpa = 3.2
is_student = True

print(type(gpa))

# typecasting  gpa to int type

gpa = int(gpa)

print(gpa)

#age = float(age)
#print(age)

age = str(age)
print(age)
print(type(age))
age += "1"
print(age)

name = bool(name) # if variable value is empty then we will get false
print(name)