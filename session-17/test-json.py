import json
import termcolor

f= open('person.json', 'r')

person = json.load(f)

print()

termcolor.cprint('Name: ', 'green', end='')
print(person['firstname'], person['lastname'])
termcolor.cprint('age: ', 'green', end='')
print(person['age'])

for i, num in enumerate(person['phonenumber']):
    termcolor.cprint('Phone {}: '.format(i))

    termcolor.cprint('    Type: ', 'red', end='')
    print(num['type'])

    termcolor.cprint('    Number {}: '.format(i), 'blue', end='')
    print(num['number'])


