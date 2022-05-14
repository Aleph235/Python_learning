fizz_buzz = []

for value in range(1, 101):
    if (value % 15 == 0):
        value = 'fizzbuzz'
        fizz_buzz.append(value)
    elif (value % 5 == 0):
        value = 'buzz'
        fizz_buzz.append(value)
    elif (value % 3 == 0):
        value = 'fizz'
        fizz_buzz.append(value)
    else:
        fizz_buzz.append(value)

print(fizz_buzz)

test1 = 3 in fizz_buzz
print(test1)

test2 = test1 and 100 in fizz_buzz
print(test2)

test3 = 0 not in fizz_buzz
print(test3)
