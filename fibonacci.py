def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def print_fibonacci(n):
    for i in range(1, n+1):
        print(f"Fibonacci number {i} is: {fibonacci(i)}")

n = int(input("Enter the number of terms: "))
print_fibonacci(n)