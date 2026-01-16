#input = A function that prompts the user to enter data and returns the entered data as a string

name = input("What is your name?: ")
age = int(input("How old are you?: "))
age +=1

print(f"Hello {name}!")
print("Happy Birthday!")
print(f"You are {age} years old.")

#Example 1 for User-Input

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width
print(f"The area is {area}cm")

#Example 2 for User-Input

item = input("What item would like to buy?: ")
price = int(input("What is the price? :"))
quantity = int(input("How many items would you like to buy?: "))
total = price * quantity

print(f"The total is ₹{total}")
