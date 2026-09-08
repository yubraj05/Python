# Escape Sequences in Python
''' Escape sequences are special character combinations in strings that allow you to represent characters 
    that are difficult to type or display directly, such as newline characters, tabs, or even special symbols. '''

# Example 1: Printing a simple string
print("Hello World")  
# Output: Hello World
# A regular string with no escape sequences, simply printed as it is.

# Example 2: Using newline escape sequence (\n)
print("Hello \n World")  
# Output:
# Hello
# World
# The \n escape sequence is used to insert a line break between 'Hello' and 'World'.

# Example 3: Printing the escape sequence literally (escaping the backslash)
print("Hello \\n World")  
# Output: Hello \n World
# Here, '\\' escapes the backslash, printing the sequence as is, rather than triggering its special meaning.

''' Explanation:
    - In Python, the backslash (\) is used to introduce escape sequences. 
    - To display an actual backslash, we need to escape it by using a double backslash (\\).
    - For example, '\\n' will print "\n" rather than creating a new line.'''

# Example 4: Printing multiple backslashes
print("8 backslash \\\\\\\\")  
# Output: \\\\
# To print multiple backslashes, each backslash needs to be escaped, hence four backslashes in the string 
# result in two backslashes being printed.

# Example 5: Using escape sequences for quotes within a string
print("\'\"")  
# Output: '"
# We use escape sequences to print both single and double quotes inside the string. 
# The single quote (\') and double quote (\") are escaped to show them as literal characters.

# Example 6: Using raw strings to prevent escape sequence processing
''' Raw strings (denoted by prefixing the string with 'r') treat backslashes as literal characters. 
    This prevents Python from interpreting escape sequences like \n or \t. Raw strings are particularly 
    useful when working with regular expressions or file paths.'''

print(r"The escape sequence is now \n restricted")  
# Output: The escape sequence is now \n restricted
# In a raw string, the escape sequence \n is not processed as a newline, and is displayed literally as \n.
