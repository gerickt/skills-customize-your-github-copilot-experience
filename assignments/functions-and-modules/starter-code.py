def calculate_rectangle_area(width, height):
    """Return the area of a rectangle."""
    return width * height


def format_greeting(name):
    """Return a simple greeting message."""
    return f"Hello, {name}!"


def is_prime(number):
    """Return True if number is prime, otherwise False."""
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def main():
    # Example usage of the functions
    print(format_greeting("Alice"))
    print("Rectangle area:", calculate_rectangle_area(5, 3))
    print("Is 17 prime?", is_prime(17))


if __name__ == "__main__":
    main()
