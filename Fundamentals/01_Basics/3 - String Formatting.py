# String Formatting Methods
''' This code demonstrates different ways to format strings in Python using the `.format()` method, f-strings, and the `center()` method. '''

# Example 1: Using the `.format()` method for string formatting
var = "Hello my name is {} ".format('Yubraj')
# Explanation:
# - The `.format()` method is used to insert values into a string where placeholders (i.e., curly braces `{}`) are specified.
# - In this case, 'Yubraj' is inserted into the string at the placeholder.
# - The .format() method is versatile and can handle multiple placeholders, variable types, and more.

print(var)
# Expected Output: Hello my name is Yubraj

# Example 2: Using f-strings (formatted string literals) for string interpolation
name = "Yubraj"
var = f"Hello my name is {name}"
# Explanation:
# - f-strings, introduced in Python 3.6, provide a concise and readable way to embed expressions inside string literals.
# - The expression `{name}` is evaluated, and the result is inserted into the string at that location.
# - f-strings are often preferred due to their simplicity and performance advantages over `.format()` in many cases.

print(var)
# Expected Output: Hello my name is Yubraj

# Example 3: Using the `center()` method to align text in the center of a string
# The `center()` method pads the string with a specified character until the total length of the string matches the given width.
# Here, '*' is used as the padding character, and the total width is 8 characters.

print(name.center(8, "*"))
# Expected Output: *Yubraj*
# Explanation:
# - The `center()` method ensures that the string is centered within the specified width. 
# - If the string is shorter than the width, it will be padded with the specified character ('*' in this case).
# - If the width is smaller than the string's length, the string is returned as-is.

name = "Yubraj"
age = 20
print("My name is %s and I am %d years old." % (name, age))
# Format Specifiers:
# %s → String
# %d → Integer
# %f → Float
# %x → Hexadecimal
# %o → Octal
# %e → Scientific notation