import os
from bottle import run, get, post, request


messages = []


@get('/')
def get_index():
    return 'welcome to madlib'

@get('/template')
def get_template():
    pass

@post('/template')
def post_template():
    template = None
    hash_key = {'hash': -1}
    try:
        template = request.json
    except Exception as e:
        return hash_key
    return hash_key


@post('/madblib')
def post_madlib():
    madlib = None
    hash_key = {'hash': -1}
    try:
        madlib = request.json
    except Exception as e:
        return hash_key
    return hash_key



@get('/messages')
def get_messages():
    return {'messages': messages}


@get('/clear')
def get_messages():
    global messages
    messages = [{'name': 'echo', 'message': 'make what you want of this'}]
    return {'messages': messages}


@post('/message')
def post_message():
    global messages
    message = None
    try:
        message = request.json
        if message is None:
            message = {'user': 'echo', 'message': 'Huh, say something?'}
    except Exception as e:
        message = {'user': 'echo', 'message': 'Huh, what?'}
    messages.append(message)
    messages = messages[-10:]
    return {'messages': messages}


run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
