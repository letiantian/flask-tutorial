import requests

user_info = {'name': 'letian', 'password': '123'}
r = requests.post("http://127.0.0.1:5000/register", data=user_info)

print(r.text)