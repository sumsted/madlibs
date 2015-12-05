import os
from bottle import run, get, post, request


templates = [
    {
        'id': 0,
        'name': 'Christmas Tree',
        'content': 'Every [month] we [verb] to a tree [place] far away. not just any '
                   '[adjective] farm, a [adjective] tree [place]. My dad and I [verb] '
                   'onto the [noun] to [verb] for the perfect [noun]. Some people live '
                   '[adjective] and [adjective] and some like them [color] and fat. We '
                   'are searching for a tall and [adjective] one! "Over there!" I '
                   'exclaim, "Dad it\'s over there!" Off we [verb], saw in hand to [verb] '
                   'this year\'s [noun] down. [Exclamation] it\'s [holiday] finally!'
    },
    {
        'id': 1,
        'name': 'More Lights!',
        'content': 'Did you ever have one of those [noun]? Well today [person] did! Mom '
                   'wanted to [verb] [nouns] up for [holiday]. Not just any lights, '
                   '[color] lights. [Adjective] [color] lights! [Adjective] bright red '
                   'lights. The only problem, they are a [verb/ed] mess! Not to mention '
                   'that there are some [vegetable], yellow and green lights [verb/ed] '
                   'in. "[person]!" I yell! This can\'t be done! She could [verb] I was '
                   'right and went out and [verb] some new shiny [color] lights!'
    },
    {
        'id': 2,
        'name': 'Turkey Dinner!',
        'content': 'I spent last summer on my grandfather\'s [adjective] farm. He raises '
                   '[noun/s] for local food [noun/s]. He also grows corn on the [noun], '
                   '[adjective] lettuce and lima [noun/s]. My favorite place to [verb] '
                   'on the farm is the [adjective] house where grandfather keeps his '
                   '[noun/s]. But when I visit in November, there are no [noun/s]! They '
                   'are all gone! I ansxiously await at the table that Thanksgiving. I '
                   'see corn on the [noun] and eve the lime [noun/s]. I am relieved when '
                   'grandma brings out a [noun] for Thanksgiving dinner!'
    },
    {
        'id': 3,
        'name': 'Pizza Pizza',
        'content': 'Pizza was invented by a [adjective] [nationality] chef named [person]. '
                   'To make a pizza, you need to take a lump of [noun], and make a thin, '
                   'round [adjective] [noun]. Then you cover it with [adjective] sauce, '
                   '[adjective] chees, and fresh chopped [noun/s]. Next you have to bake '
                   'it in a very hot [noun]. When it is done, cut it into [number] [shapes]. '
                   'Some kids like [food] pizza the best, but my favorite is the [food] pizza. '
                   'If I could, I would eat pizza [number] times a day!'
    }
]

madlibs = []


@get('/')
def get_index():
    return 'welcome to madlib'


@get('/template')
def get_template():
    return {'templates': templates}


@get('/template/<id>')
def get_template(id):
    return templates[id]


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
