import requests

# get Request:
x = requests.get('https://w3schools.com/python/demopage.htm')
print(x.text)
print(x.status_code)

# Get Request:
url = 'https://www.w3schools.com/python/demopage.php'
myobj = {'somekey': 'somevalue'}
y = requests.post(url = url, json = myobj)
print(y.text)