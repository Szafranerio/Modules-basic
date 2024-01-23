def make_pizza (size, *toppings):
    print(f'\nI am creating pizza with the size of {size} cm with the following ingredients:')
    for topping in toppings:
        print(f'-{topping}')