print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter choice: "))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
    print("sum =", num1 + num2 )
elif choice == 2:
    print("Difference =", num1 - num2 )
elif choice == 3:
    print("Product =", num1 * num2 ) 
elif choice == 4:
    if num2 != 0:
        print("Qoutient =", num1/num2)
    else:
        print("Error: Division by Zero")
else:
    print("Invalid choice")
