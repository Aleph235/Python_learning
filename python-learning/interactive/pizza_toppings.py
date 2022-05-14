prompt = 'please pick a topping\n'

active = True

while active:
    topping = input(prompt)

    if topping == 'quit':
        active = False
    else:
        print(f'we add {topping}')
