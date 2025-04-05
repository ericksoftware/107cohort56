print("Hello wordld")

x= 5
y = "hello"
x = False
y= 10.5
print(x, y)

list = [1, 2, 3, 4, 5]
print(list)
list.append(6)
list.remove(2)
list.pop()
print(list)
list.clear()
print(list)

dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

print(dict)

dict["country"] = "USA"
print(dict)

dict.pop("name")
print(dict)

dict.clear()
print(dict)

for i in range(5):
    print(i)

if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")

def add(a, b):
    return a + b

print(add(5, 10))

def menu():
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

menu()

choice = input("Enter your choice (1-5): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
result = 0
if choice == '1':
    result = add(num1, num2)
elif choice == '2':
    result = num1 - num2
elif choice == '3':
    result = num1 * num2
elif choice == '4':
    if num2 != 0:
        result = num1 / num2
    else:
        print("Cannot divide by zero")
elif choice == '5':
    print("Exiting...")
    exit(1)
print("Result:", result)

