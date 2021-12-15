import base64, struct, hashlib, random, hmac, itertools

"""
n = 10240099
b = bin(n)
b1 = (n & 0xff000000) >> 24
b2 = (n & 0x00ff0000) >> 16
b3 = (n & 0x0000ff00) >> 8
b4 = (n & 0x000000ff)
bs = bytes([b1,b2,b3,b4])
print(bs)
bs1 = struct.pack('>I', n)
print(bs1)
n1 = struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\xf0\xf0')
print(n1)

s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'

s1 = struct.unpack('<ccIIIIIIHH', s)
print(s1)
"""

"""md5 = hashlib.md5()
md5.update('hwo to use md5 in python hashlib?'.encode('utf-8'))
#md5.update('hwo to use md5 in python hashlib??'.encode('utf-8'))
print(md5.hexdigest())

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())



db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def login(username, password):
    if db[username] == calc_md5(password):
        return True
    else:
        return False

assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')
"""
"""def calc_md5(password):
    return hashlib.md5(password.encode('utf-8')).hexdigest()

# def register(username,password):
#     db[username] = calc_md5(password+username+'the-Salt')

class User(object):
    def __init__(self,username,password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48,122)) for i in range(20)])
        self.password = calc_md5(password+self.salt)

db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def login(username, password):
    user = db[username]
    print('1' if user.password == calc_md5(password+) else '0')
        

login('michael', '123456')
login('bob', 'abc999')
login('alice', 'alice2008')
login('michael', '1234567')
login('bob', '123456')
login('alice', 'Alice2008')

message = b'Hello, world!'
key = b'secret'
h = hmac.new(key, message, digestmod='md5')
print(h.hexdigest())
"""

# natuals = itertools.count(1)
# for n in natuals:
#     print(n)

# cs = itertools.cycle('ABC')
# for c in cs:
#     print(c)

# ns = itertools.repeat('A')
# for n in ns:
#     print(n)

# natuals = itertools.count(1)
# ns = itertools.takewhile(lambda x: x<=10, natuals)
# print(list(ns))

# for c in itertools.chain('ABC', 'XYZ'):
#     print(c)

# for key, group in itertools.groupby('AAABBBCCAAA'):
#     print(key, list(group))

# for key, group in itertools.groupby('AaaBBbcCAAa', lambda x: x.upper()):
#     print(key, list(group))
import datetime
def pi(N):
    I = []
    sum = 0
    natuals = itertools.count(1,2)
    start = datetime.datetime.now()
    ns = list(itertools.takewhile(lambda x:x<=2*N-1, natuals))
    print(datetime.datetime.now()-start)
    for n in ns:
        if ((n//2+1)%2)==0:
            c = -4/n
        else:
            c = 4/n
        I.append(c)
    for i in I:
        sum = i + sum
    return sum

print(pi(10000000))




