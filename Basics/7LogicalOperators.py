# logical operators = evaluate multiple conditions (and, or, not)
#                     or = at least one condition must be true
#                     and = all conditions must be true
#                     not = reverse boolean value(true -> false, false -> true)

# Examples and notes about logical operators in Python

# and, or, not operate on booleans but accept any values (truthiness)
a, b, c = True, False, None

print("a and b ->", a and b)      # False (both must be True)
print("a or b ->", a or b)        # True  (either True)
print("not a ->", not a)          # False (negation)

temp = 28
is_raining = False
is_sunny = False

if temp > 35 or temp < 0 or is_raining:
    print("Stay inside!")
elif temp >= 28 and is_sunny:
    print("It's sunny.")
elif temp >= 28 and not is_sunny:
    print("It's hot.")
else:
    print("Go outside!")


'''
# Short-circuiting: evaluation stops as soon as result is known
def left():
    print("left evaluated")
    return True

def right():
    print("right evaluated")
    return False

print("\nShort-circuit examples:")
print("left() or right() ->")
print(left() or right())   # right() not called because left() is True

print("\nleft() and right() ->")
print(left() and right())  # right() called because left() True, result depends on right()

# Truthiness examples: non-boolean values
print("\nTruthiness:")
print("0 is", bool(0))
print("1 is", bool(1))
print("'' is", bool(""))
print("'text' is", bool("text"))
print("[] is", bool([]))
print("[1] is", bool([1]))

# and/or return one of the operands (not strictly booleans)
print("\nand/or return operands:")
print("'a' and 'b' ->", 'a' and 'b')   # returns 'b' because 'a' is truthy
print("'' or 'fallback' ->", '' or 'fallback')  # returns 'fallback'

# Precedence: not > and > or
print("\nPrecedence (not > and > or):")
print("not False and False or True ->", not False and False or True)
# Equivalent grouping: ((not False) and False) or True

# De Morgan's laws (useful for negating compound conditions)
# not (A and B) == (not A) or (not B)
# not (A or B) == (not A) and (not B)

A, B = True, False
print("\nDe Morgan checks:")
print("not (A and B) == (not A) or (not B):", not (A and B) == (not A) or (not B))
print("not (A or B) == (not A) and (not B):", not (A or B) == (not A) and (not B))
'''