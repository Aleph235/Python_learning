car = input('What kind of car would you rent?')

if car == 'bmw':
    print(f'Let me see if we have the {car.upper()}')
else:
    print(f'Let me see if we have the {car.title()}')
