# 8.1~8.5
e2f = {'dog':'chine', 'cat':'chat', 'walrus':'morse'}
key_list = list(e2f)  # keys만 추출
value_list = [value for value in e2f.values()]

print(e2f)
print(f"walrus는 프랑스어로 {e2f['walrus']}")
f2e = {v:k for k,v in e2f.items()}
print(f'f2e는 {f2e.items()}')
print(f"chien은 영어로 {key_list[0]}")
print(key_list)


# 8.6~8.9
life = {'animals': {
                    'cats': ['Henri', 'Grumpy', 'Lucy'],
                    'optopi': {},
                    'emus': {}
                },
'plants': {},
'other': {}
}
print(life.keys())
print(life['animals'].keys())
print(life['animals']['cats'])

# 8.10
# directory
squares = {x: x*x for x in range(10)}
print(squares)
# set
squares = {x*x for x in range(10)}
print(squares)


# 8.11
numbers = {x for x in range(10) if x % 2 == 1}
print(numbers)

# 8.12
# 제너레이터 표현식은 ()
gen = (x for x in range(10))
print(type(gen))
for value in gen:
    print(value)


# 8.13
keys = ('optimist', 'pessimist', 'troll')
values = ('The glass is half full', 'The glass is half empty', 'How did you get a glass?')
print(dict(zip(keys, values)))

# 8.14
titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a mon ster', 'A haunted yarn shop']
movie = dict(zip(titles, plots))
print(movie)