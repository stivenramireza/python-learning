#
# Example file for variables
#


# Declare a variable and initialize it
f: int = 0
print(f)

# Re-declaring the variable works
f: str = "abc"
print(f)

# ERROR: variables of different types cannot be combined
print("This is a string " + str(123))

# Global vs local variables in functions
def someFunction():
    global f
    f = "def"
    print(f)


del f
print(f)
