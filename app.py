from flask import Flask
import os
import redis

app = Flask(__name__)
r = None


@app.route('/')
def hello():
    return 'Hello, fellow traveler!. Follow white <a href="/rabbit">rabbit</a>!'


@app.route('/<name>')
def hello_name(name):
    quote = get_from_mind(name)
    if quote:
        return 'Be smart, {}: <br/>{}'.format(name, quote)
    else:
        put_in_mind(name, get_random_quote())
        return 'Hello, {}! We will remember you on your next visit!' \
               'Refresh page or follow this <a href="/{}"></a>to see what happens'.format(
            name, name)


if __name__ == '__main__':
    app.run()
    # global r
    r = redis.from_url(os.environ.get('REDIS_URL'))


def get_random_quote():
    return 'ha-ha-ha'


def put_in_mind(name, quote):
    r.set(name, quote)


def get_from_mind(name):
    return r.get(name)
