"""Things I'll be importing."""


def addition(x: int, y: int) -> int:
    """Returning sum of arguments."""
    return x + y


my_variable: str = "Hello!"

if __name__ == "__main__":
    print("This should only print when running my_functions")
else: 
    print("My_functions is being imported")