name=input("Enter your name: ")
surname=input("Enter your surname: ")

greeting=name or f"Hello, {surname}"
print(greeting)

name=input("Enter your name: ")
surname=input("Enter your surname: ")

greeting=name and f"Hello, {surname}"
print(greeting)