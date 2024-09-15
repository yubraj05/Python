
age = '5' 
age: int #expected value
name: str = "Alice"

print(type(age))
def greet(name: str) -> str:
    return f"Hello, {name}"

def add(a: int, b: int) -> int:
    return a + b
# if the function gets or returns a unexpected value then it will raise error

