users = [
    {
        'name': 'Ana Silva',
        'email': 'ana@email.com',
        'age': 27
    },

    {
        'name': 'João Batista',
        'email': 'joaob@email.com',
        'age': 30
    },

    {
        'name': 'Maria Madalena',
        'email': 'madalena@email.com',
        'age': 25
    }
]
print('Total users: {}'.format(len(users)))
print()

for numero, user in enumerate(users, start = 1):
    print('User {}'.format(numero))
    print('Name:', user['name'])
    print('Email:',user['email'])
    print('Age:', user['age'])
    print()
