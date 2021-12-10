from io import StringIO, BytesIO
import os
import pickle
import json
"""
try:
    f = open('./debug.py', 'r')
    print(f.read())
finally:
    if f:
        f.close()
"""

# with open('./debug.py', 'r') as f:
#     for line in f.readlines():
#         print(line.strip())

# f = open('./cool-background.png', 'rb')
# print(f.read())

# f = open('./debug.py', 'r', encoding='gbk')
# print(f.read())

# with open('./debug.py', 'r', encoding='utf-8') as f:
#     s = f.read()
#     print(s)

# f = StringIO('hello!\nhi!\ngoodbye')
# # print(f.write('hello'))
# # print(f.write(' '))
# # print(f.getvalue())
# while True:
#     s = f.readline()
#     if s == '':
#         break
#     print(s.strip())

# f = BytesIO()
# f.write('中文'.encode('utf-8'))
# print(f.getvalue())


"""
def findStrInFile(str,file_path='.'):
    
    L = [x for x in os.listdir(file_path) if os.path.isfile(x)]
    # print(L)
    for x in L:
        if x.find(str)!=-1:
            print(os.path.join(file_path,x))
        else:
            pass
    Y = [x for x in os.listdir(file_path) if os.path.isdir(x)]
    for x in Y:
        file_path = os.path.join(file_path, x)
        findStrInFile(str,file_path)

findStrInFile('io','D:\Feishu')
"""

d = dict(name='bob', age=20, score=88)
# print(pickle.dumps(d))

# f = open('dump.txt', 'wb')
# pickle.dump(d, f)
# f.close()

# f = open('dump.txt', 'rb')
# d1 = pickle.load(f)
# f.close()
# print(d1)
j = json.dumps(d)

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def strudent2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

s = Student('Bob', 20, 88)
print(json.dumps(s, default=lambda obj: obj.__dict__))

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))

obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
print(s)