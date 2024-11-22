def right_triangle_decorator(func):
    def wrapper(n):
        for i in range(1, n + 1):
            print("*" * i)
    return wrapper

@right_triangle_decorator
def print_triangle(n):
    pass  # This function does nothing, as the decorator handles the printing

# Example usage:
print_triangle(5)