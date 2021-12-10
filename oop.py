"""
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' %(self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


# bart = Student('Bart Simpson', 59)
# print(bart)
# print(Student)
# bart.name = 'Bart Simpson'
# print(bart.name)
# bart.print_score()

lisa = Student('Lisa', 99)
bart = Student('Bart', 59)
print(lisa.name, lisa.get_grade())
print(bart.name, bart.get_grade())
lisa.name = 'LISA'
print(lisa.name, lisa.get_grade())


class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name
    
    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <=100:
            self.__score = score
        else:
            raise ValueError('bad score')
    def print_score(self):
        print('%s: %s' %(self.__name, self.__score))

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'


bart = Student('Bart Simpson', 59)
print(bart.get_name(), bart.get_score())
bart.set_score(111)
print(bart.get_name(), bart.get_score())
"""
"""
class Animal:
    def run(self):
        print('Animal is running')

class Dog(Animal):
    def eat(self):
        print('Dog is eating')
    
    def run(self):
        print('Dog is running')

class Cat(Animal):
    pass

class Husky(Dog):
    pass

dog = Dog()
dog.run()
dog.eat()

a = list() # a是list类型
b = Animal() # b是Animal类型
c = Dog() # c是Dog类型

print(isinstance(c,Animal))

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(c)


print(type(123)==int)
print(int)

import types
def fn():
    pass

print(type(fn)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x: x)==types.LambdaType)
print(type((x for x in range(10)))==types.GeneratorType)
print(type(dog))

a = Animal()
d = Dog()
h = Husky()

print(isinstance(h, Dog))
print(dir(types))
print(dir('ABC'))
print(len('abc'))
print('abc'.__len__())

class Myobj():
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = Myobj()

print(hasattr(obj, 'x'))
print(obj.x)
print(hasattr(obj, 'y'))
setattr(obj, 'y', 19)
print(hasattr(obj, 'y'))
print(getattr(obj, 'y'))
# print(obj.z)
print(getattr(obj,'z',404))
"""
"""
class Student:
    name = 'Student'

s = Student() # s是Student类型
print(s.name)
s.name = 'Michael'
print(s.name)
print(Student.name)
del s.name
print(s.name)
"""

class Student:
    count = 0
    def __init__(self, name):
        self.name = name
        Student.count = Student.count + 1

if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')