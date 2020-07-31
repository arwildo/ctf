#!/usr/bin/python3
import requests

url = 'http://two.jh2i.com:50018/mail.php'
myobj = {'name': 'fsdkfkjs', 'email': 'dfjskjsf', 'subject': 'dfdfs', 'message': 'dfssf'}

x = requests.post(url, data = myobj)

print(x.text)
