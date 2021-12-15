import re

# test = input('shuru:')
# i =  re.match(r'^\d{3}\-\d{3,8}$', test)
# if i:
#     print('ok')
# else:
#     print('failed')

# t = '19:05:30'
# m = re.match(r'^(\d{2})\:(\d{2})\:(\d{2})$', t)
# print(m.groups())

# re_telephone = re.compile(r'^(\d{3})\-(\d{3,8})$')
# print(re_telephone.match('010-12345').groups())
# print(re_telephone.match('010-3039').groups())

def name_of_email(addr):

    re_email = re.compile(r'^\<?([0-9a-zA-Z\s\.]+)\>?[0-9a-zA-Z\s]*\@([0-9a-zA-Z]+)\.[a-zA-Z]+$')
    i = re_email.match(addr)
    if i:
        return i.group(1) 
    else:
        return False

if name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris':
    if name_of_email('tom@voyager.org') == 'tom':
        print('ok')





