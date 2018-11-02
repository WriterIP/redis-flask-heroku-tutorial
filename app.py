from flask import Flask
import os
import redis
import random

app = Flask(__name__)

r = None


@app.route('/')
def hello():
    return 'Hello, fellow traveler! Follow white <a href="/rabbit">rabbit</a>!'


@app.route('/<name>')
def hello_name(name):
    quote = get_from_mind(name)
    if quote:
        return 'Be smart, {}: <br/>{}'.format(name, quote)
    else:
        put_in_mind(name, get_random_quote())
        return 'Hello, {}! We will remember you on your next visit!<br/>' \
               'Refresh page or follow this <a href="/{}">link</a> to see what happens'.format(
            name, name)


if __name__ == '__main__':
    app.run()


def connect_redis():
    global r
    r = redis.from_url(os.environ.get('REDIS_URL'))


def get_random_quote():
    return random.choice(quotes)


def put_in_mind(name, quote):
    if r is None: connect_redis()
    r.set(name, quote)


def get_from_mind(name):
    if r is None: connect_redis()
    return r.get(name)


quotes = ["'And what is the use of a book,' thought Alice, 'without pictures or conversation?'",
          "It would have made a dreadfully ugly child; but it makes rather a handsome pig.",
          "'Who in the world am I?' Ah, that's the great puzzle!",
          "It takes all the running you can do, to keep in the same place. If you want to get somewhere else, you must run at least twice as fast as that!",
          "I don't think -- " "Then you shouldn't talk.",
          "Curiouser and curiouser!",
          "We're all mad here.",
          "It's no use going back to yesterday, because I was a different person then.",
          "Why, sometimes I've believed as many as six impossible things before breakfast.",
          "Off with their heads!"
          ]
