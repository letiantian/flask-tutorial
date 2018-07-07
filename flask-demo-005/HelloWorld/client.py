import requests

file_data = {'image': open('Lenna.jpg', 'rb')}

user_info = {'info': 'Lenna'}

r = requests.post("http://127.0.0.1:5000/upload", data=user_info, files=file_data)

print(r.text)