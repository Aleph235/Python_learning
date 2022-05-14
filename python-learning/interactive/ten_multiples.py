prompt = 'Gimmi a number\n'
active = True

while active:
    number = input(prompt)
    message = ""
    if int(number) % 10 == 0:
        message = 'You win'
    elif prompt == -1:
        active = False
    else:
        message = 'You loose try again'
    print(message)
