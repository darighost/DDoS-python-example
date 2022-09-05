import requests

target = 'http://127.0.0.1:5000/api/fib/'

while True:
    try:
        r = requests.get(target + '100000000')
        r2 = r = requests.get(target + 'hiiii')
    except:
        print('Down!')
