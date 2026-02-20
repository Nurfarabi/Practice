# Example 4: *args and **kwargs

def show_numbers(*args):
    # args is a tuple
    for num in args:
        print(num)

def show_person(**kwargs):
    # kwargs is a dictionary
    for key, value in kwargs.items():
        print(key, ":", value)

show_numbers(1, 2, 3, 4)
show_person(name="Aida", age=20, city="Almaty")