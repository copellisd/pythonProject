def triangle_decorator(func):
    def wrapper(n):
        for i in range(1, n + 1):
            print(" " * (n - i) + "*" * i)
    return wrapper

@triangle_decorator
def print_triangle(n):
    pass  # The decorator handles the printing

# Example usage
print_triangle(5)