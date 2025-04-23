print("Hello World")
# Variable creation
# JS - let, const, var
# let x = 5;
# const y = "Hello";
x = 5
y = "Hello"
x = False
y = 10.5 
print(x, y)

# Variable types
# PY - Number, String, Boolean, Object, List, Tuple, Set, Dictionary
# list = [1, 2, 3, 4, 5]
list = [1, 2, 3, 4, 5]
print(list)
# add 6 to the list
list.append(6)
print(list)
# remove 1 from the list
list.remove(1)
print(list)
# remove last element from the list
list.pop()
print(list)
# remove all elements from the list
list.clear()
print(list)
# create a dictionary
# dict = {key: value}
dict = {"name": "John", "age": 30, "city": "New York"}
print(dict)
# add a key to the dictionary  
dict["country"] = "USA"
print(dict)
# remove a key from the dictionary
dict.pop("name")    
print(dict)
# remove all keys from the dictionary
dict.clear()
print(dict)

# for loop
for i in range(20):
    print(i)
# JS - for (let i = 0; i < 5; i++) { console.log(i); }
# while loop
i = 0
while i <= 5:
    print(i)
    i += 1
# JS - while (i < 5) { console.log(i); i++; }

# if else statement
x = 0
if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")
# JS - if (x > 0) { console.log("x is positive"); } else if (x < 0) { console.log("x is negative"); } else { console.log("x is zero"); }

# function creation
def add(a, b):
    return a + b
# JS - function add(a, b) { return a + b; }
print(add(5, 10))

# create an input from the user


# Mini challenge -- Create a calculator that takes two numbers 
# use this operators (+, -, *, /) and returns the result.

# fucntion
def print_menu():
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

print_menu()

# take input from the user
choice = input("Enter choice: ")
num1 = float(input("Enter first number: ")) 
num2 = float(input("Enter second number: "))
result = 0  
if choice == "1":
    result = num1 + num2
elif choice == "2":
    result = num1 - num2
elif choice == "3": 
    result = num1 * num2
elif choice == "4":
    if num2 == 0:
        print("Cannot divide by zero")
        exit(1)
    else:
        result = num1 / num2
elif choice == "5":
    print("Exiting...")
else:
    print("Invalid choice")
    exit(1)
print("Result: ", result)


for i in range(10):
    print(i)
    i += 2
    
