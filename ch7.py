# 7.1~7.3
# year = int(input("year: "))
# year_lists = [year, year+1, year+2, year+3, year+4]
# print(year_lists)

# year = int(input("year: "))
# year_list = []
# for year in range(year, year+6):
#     year_list.append(year)
# print(year_list)
# print(year_list[2])
# print(year_list[5])


# 7.4~7.7
# things = ['mozzarella', 'cinderella', 'salmonella']
# things[-2] = things[-2].title()
# print(things)
#
# things[0] = things[0].upper()
# print(things)
#
# print(f' Delete the {things.pop()} from things')
# print(things)


# 7.8~7.9
surprise = ['Groucho', 'Chico', 'Harpo']
surprise[2] = surprise[2].lower()
print(surprise)
harpo = surprise[2]
print(harpo[::-1].title())


# 7.10
list = [number for number in range(10) if number % 2 == 0]
print(list)

# 7.11
start1 = ['fee', 'fie', 'foe']
rhymes = [
    ('flop', 'get a mop'),
    ('fope', 'turn the rope'),
    ('fa', 'get your ma'),
    ('fudge', 'call the judge'),
    ('fat', 'pet the cat'),
    ('fog', 'walk the dog'),
    ('fun', "say we're done"),
]
start2 = "Someone better"

for i in range(0, 3):
    start1[i] = start1[i].title() + '!'

#for word, sen in rhymes:
for rhy in range(0, 7):
    print(''.join(start1), end=' ')
    print(rhymes[rhy][0].title() + '!')
    print(start2 + ' ' + rhymes[rhy][1] + '.\n')










