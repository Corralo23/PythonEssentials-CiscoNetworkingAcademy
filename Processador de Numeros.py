line = input('Enter a line of numbers - seprate them with spaces: ')
string = line.split()
total = 0
try:
    for substr in strings:
        total += float(substr)
    print(f'The total is: {total}')
except:
    print(f'{substr} is not a number')
