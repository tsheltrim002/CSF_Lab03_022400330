numbers = [4, 9, 6, 10, 3]
search = int(input("Enter number to search: "))

found = False 
for num in numbers:
    if num == search:
        print("Number found")
        found = True 
        break 
if not found:
    print("Number not found")


