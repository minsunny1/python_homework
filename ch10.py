# 10.1
class Thing():
    pass


example = Thing()
print(example)
print(Thing())


# 10.2
class Thing2():
    letters = 'abc'  # 클래스 속성 변경


choice = Thing2()
print(choice.letters)


# 10.3
class Thing3():
    def letters(self):  # 인스턴스 속성 변경
        return 'xyz'


cho = Thing3()
print(cho.letters())
print(Thing3().letters())  # 객체를 생성하지 않아도 출력이 됨


# 10.4
class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number


a = Element('Hydrogen', 'H', 1)
print(a.name)
print(a.symbol)
print(a.number)


# 10.5
el_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
hydrogen = Element(**el_dict)
print(hydrogen.name)
print(hydrogen.symbol)
print(hydrogen.number)


# 10.6
class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):
        print(f'name: {self.name}, symbol: {self.symbol}, number: {self.number}')


hydrogen = Element('Hydrogen', 'H', 1)
hydrogen.dump()


# 10.7
class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def __str__(self):  # __str__은 문자열을 반환한다
        print(f'name: {self.name}, symbol: {self.symbol}, number: {self.number}')


hydrogen = Element('Hydrogen', 'H', 1)
hydrogen.__str__()


# 10.8
class Element():
    def __init__(self, name, symbol, number):
        self.hidden_name = name
        self.hidden_symbol = symbol
        self.hidden_number = number

    def get_name(self):
        return self.hidden_name
    def get_symbol(self):
        return self.hidden_symbol
    def get_number(self):
        return self.hidden_number
    name = property(get_name)
    symbol = property(get_symbol)
    number = property(get_number)


hydrogen = Element('Hydrogen', 'H', 1)
print(hydrogen.get_name())
print(hydrogen.get_symbol())
print(hydrogen.get_number())


# 10.9
class Bear():
    def __init__(self, food):
        self.food = food
    def eats(self):
        return f'{self.food} (Bear)'


class Rabbit():
    def __init__(self, food):
        self.food = food
    def eats(self):
        return f'{self.food} (Rabiit)'


class Octothorpe():
    def __init__(self, food):
        self.food = food
    def eats(self):
        return f'{self.food} (Octothorpe)'

B = Bear('berries')
R = Rabbit('clover')
O = Octothorpe('campers')

print(B.eats())
print(R.eats())
print(O.eats())


# 10.10
class Laser():
    def does(self):
        return 'disintegrate'


class Claw():
    def does(self):
        return 'crush'


class SmartPhone():
    def does(self):
        return 'ring'

class Robot():
    laser = Laser()
    claw = Claw()
    smartphone = SmartPhone()
    def does(self):
        print(f'Laser: {Robot.laser.does()}, Claw: {Robot.claw.does()}, Smartphone: {Robot.smartphone.does()}')
        # self.이랑 Robot.으로 두는 것릉 개념이 다르다 공부하자

robot = Robot()
robot.does()




