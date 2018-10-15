import requests

json_data = {'a': 1, 'b': 2}

r = requests.post("http://127.0.0.1:5000/add", json=json_data)

print(r.text)