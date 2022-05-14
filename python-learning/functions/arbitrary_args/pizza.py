def make_pizza(size, *toppings):
    """Prints the list of toppings that have been requested."""
    print(f"\nMaking a pizza of {size} cm with the following toppings:")
    for topping in toppings:
        print(f'-{topping}')
