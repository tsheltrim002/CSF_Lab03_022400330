def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "odd"
    
def print_numbers(n):
    for i in range(1, n + 1):
        print(f"{i} -> {check_even_odd(i)}")

n = int(input("Enter n: "))
print_numbers(n)