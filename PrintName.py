# First, ask the user for their name. Then, print out the greeting "Hello, NAME"
# Remember the uppercase H, the comma, and the space between words!

# Secondly, ask the user for their age and convert it into a number.
# Then, print out how many months that equals to (you'll have to multiply the age by 12).
name=input("What is your name:")
print("Hello, {}".format(name))
age=int(input("Enter your age:"))
print("You have lived {} months".format(age*12))