import requests

data = requests.get('https://64be73225ee688b6250c6c9c.mockapi.io/quan_ly_hoc_vien').json()

#print(data)
#print(data[1])
print(data[1]['name'])