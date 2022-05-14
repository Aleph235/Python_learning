favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

persons = ('sarah', 'kiel', 'edward', 'paty', 'jef')
print(persons)

for person in persons:
    if person in favorite_languages:
        print(f'{person.title()} is in the poll')
    else:
        print(f'{person.title()} is not in the poll')
