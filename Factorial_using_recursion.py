def factorial_recursive(n):
    if n==1:
        return 1
    else:
       return n*factorial_recursive(n-1)
print(f"factorial of  ",factorial_recursive(5))