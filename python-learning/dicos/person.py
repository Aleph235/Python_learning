person_1 = {'first_name': 'mike', 'last_name': 'russo', 'age': 32, 'city': 'montreal'}
person_2 = {'first_name': 'angela', 'last_name': 'patri', 'age': 73, 'city': 'brazilia'}
person_3 = {'first_name': 'patrizzia', 'last_name': 'dipietro', 'age': 22, 'city': 'roma'}
person_4 = {'first_name': 'franco', 'last_name': 'russo', 'age': 42, 'city': 'zurich'}
person_5 = {'first_name': 'jimmy', 'last_name': 'zappa', 'age': 32, 'city': 'new-york'}

persons = [person_1, person_2, person_3, person_4, person_5]

for person, info in persons:
    print(person)
    print(f"{info['first_name']}")
