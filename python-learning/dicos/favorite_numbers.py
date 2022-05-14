favorite_numbers = {'mike': 7, 'frank': 9, 'peter': 0, 'ilda': 3}

if favorite_numbers:
    for member in favorite_numbers:
        if favorite_numbers[member] % 2 == 0:
            print(member.title() ,':', favorite_numbers[member])
        else:
            print(f'{member.title()} favorite number is odd')
