import types
import enum
"""
class Student:
    __slots__ =('name','age')
    def __init__(self):
        pass

def set_age(self, age):
    self.age = age

s = Student()
s.name = 'tongrui'
print(s.name)

s.set_age = types.MethodType(set_age, s)
s.set_age(25)
print(s.age)

s2 = Student()
#s2.set_age(25)

def set_score(self, score):
    self.score = score

Student.set_score = set_score
s.set_score(100)
s2.set_score(99)
print(s.score, s2.score)
"""
"""
class Student:
    __slots__ =('name','age')
    def __init__(self):
        pass
class Student1(Student):
    # __slots__ =('score')
    pass

s = Student1()
s.name = 'Student'
s.age = 26
s.score = 100
s.baba = 100
"""
# property创造类属性
"""
class Student(object):

    __slots__ =('name','_score','_birth','_age')

    def __init__(self,name):
        self.name = name

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    @property
    def birth(self):
        return self._birth
    
    @birth.setter
    def birth(self, value):
        self._birth = value
    
    @property
    def age(self):
        return 2021 - self._birth

s = Student('xiaoming')
s.score = 99
print(s.score)
# s.score = 999
s.birth = 2000
print(s.birth, s.age)
"""
"""
class Screen:

    __slots__ =('name','_width','_height','_resolution')

    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, value):
        self._width = value
    
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self.width * self.height
    
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
"""
# 多重继承
"""
class Animal:
    pass
class RunnableMixIn:
    def run(self):
        print('Running...')
class FlyableMixIn:
    def fly(self):
        print('Flying')
class CarnivorousMixIn:
    pass
class HerbivoresMixIn:
    pass
class Mammal(Animal):
    pass
class Bird(Animal):
    pass
class Dog(Mammal,RunnableMixIn,CarnivorousMixIn):
    pass
class Bat(Mammal,FlyableMixIn):
    pass
class Parrot(Bird):
    pass
class Ostrich(Bird):
    pass

d = Dog()
d.run()
"""
"""
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' %self.name
    __repr__ = __str__
    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        raise AttributeError("'Student' object has no attribute '%s'" %attr)

print(Student('Michael').score)


class Fib:
    def __init__(self):
        self.a, self.b = 0, 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a

    def __getitem__(self, key):
        if isinstance(key, int):
            a,b = 1,1
            for x in range(key):
                a,b = b, a+b
            return a
        if isinstance(key, slice):
            start = key.start
            stop = key.stop
            if start is None:
                start = 0
            a,b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a,b = b, a+b
            return L

f = Fib()

for n in f:
    print(n)

print(f[0:5])
"""

class Chain(object):

    def __init__(self,path=''):
        self._path = path
    
    def __getattr__(self,path):
        return Chain('%s/%s' %(self._path,path))
    
    def __str__(self):
        return self._path
    
    __repr__ = __str__


print(Chain().status.user.timelin.list)

# GET /users/:user/repos
# print(Chain().users('tongrui').repos)

class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

s = Student('tongrui')

Month = enum.Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May','Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov','Dec'))
for name,menber in Month.__members__.items():
    print(name,'->',menber,',',menber.value)

@enum.unique
class Weekday(enum.Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1 = Weekday.Mon
print(day1)

# print(Weekday(7))

Gender = enum.Enum('Gender',('Male', 'Female'))

class Student(object):
    
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
    
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')


    