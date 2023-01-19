# 9.1
def good():
    return ['Harry', 'Ron', 'Hermione']
print(good())


# 9.2
def get_odds():
    for i in range(10):
        if i % 2 == 1:
            yield i

odds = get_odds()
counts = 0

for i in odds:
    counts += 1
    if counts == 3:
        print(i)


# 9.3
# 함수 시작과 끝에 문장을 추가하는 데커레이터
def func():
    print('원본 함수이다')


def test(func):
    def new_function(*args, **kwargs):
        print('start!')
        result = func(*args, **kwargs)
        print('end')
        return result
    return new_function


test(func)()


# 9.4
class OopsExeption():
    pass

try:
    raise OopsException()
except OopsException as exc:
    print('Caught an oops')