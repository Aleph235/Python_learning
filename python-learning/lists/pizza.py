pizzas = ['margerita','salsicia','buffalo']

for pizza in pizzas:
    print(f'{pizza} mamma mia che mi piace')

print('la pizza mi piace tantissimo')

friend_pizzas = pizzas[:]

pizzas.append('quatro_formaggi')
friend_pizzas.append('funghi')

print(pizzas)
print(friend_pizzas)

for friend_pizza in friend_pizzas:
    print(friend_pizza)
