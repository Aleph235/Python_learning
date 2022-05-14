print('pastrami is no more available')

sandwich_orders = ['pastrami', 'the_special','pastrami',  'maklou','pastrami',  'tunisian', 'mexican', 'scandinavian']
print(sandwich_orders)
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    if current_sandwich == 'pastrami':
        continue
    else:
        print(f'I made {current_sandwich}')
        finished_sandwiches.append(current_sandwich)
print(finished_sandwiches)
