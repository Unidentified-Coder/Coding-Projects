import requests

login = ('https://login.ourtesco.com/access/auth')
secure_url = ('https://login.ourtesco.com/access/secure')

payload = {
    'username': 'rodas.samson@tesco.com',  # replace with your username here
    'password': '20Lugia09R12'   # and password as well
}

# r = requests.post(login ,data = payload)

# print(r.text)

with requests.session() as s:
    r = s.post(login, data=payload)
    print(r.text)
