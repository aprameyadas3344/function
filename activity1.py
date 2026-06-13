def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
def print_fibonacci(count):
    print(f"Fibonacci sequence (first {count} numbers):")
    for i in range(count):
        print(fibonacci(i), end=" ")
    print()
print_fibonacci(10)