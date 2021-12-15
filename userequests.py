import requests, chardet
# r = requests.get('https://douban.com/search', params={'q':'python', 'cat':'1001'})
# print(r.url, r.status_code, r.encoding, r.text, r.content)

# r = requests.get('http://10.123.192.169/api/v2/guest/get_custom_info', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
# print(r.encoding, r.url, r.status_code)
# print(r.json())
# #print(r.text)

# params = {"msgtype": "text", "text": {"content": "content"}}
# upload_files = {'file': open('README.txt', 'rb')}
# r =requests.post('https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=cb7ee7c0-036b-4693-b0bf-23b6a0cdcb9e', files=upload_files, timeout=0.1)
# print(r)

print(chardet.detect(b'hello,world'))
data = '离离原上草，一岁一枯荣'.encode('gbk')
print(chardet.detect(data))
data = '离离原上草，一岁一枯荣'.encode('utf-8')
print(chardet.detect(data))
data = '最新の主要ニュース'.encode('euc-jp')
print(chardet.detect(data))