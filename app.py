from flask import Flask
import os

app = Flask(__name__)

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

@app.route('/api/fib/<n>')
def index(n):
    try:
        return str(fib(int(n)))
    except Exception as e:
        print('encountered unknown behavior, shutting down server...')
        print(str(e))
        os._exit(1)

app.run(host='0.0.0.0', port=81)
