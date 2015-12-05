import os
from bottle import run, get, post, request, template


templates = [
    {
        'id': 0,
        'title': 'Christmas Tree',
        'author': 'unknown',
        'content': 'Every [month] we [verb] to a tree [place] far away. not just any '
                   '[adjective] farm, a [adjective] tree [place] . My dad and I [verb] '
                   'onto the [noun] to [verb] for the perfect [noun]. Some people live '
                   '[adjective] and [adjective] and some like them [color] and fat. We '
                   'are searching for a tall and [adjective] one! "Over there!" I '
                   'exclaim, "Dad it\'s over there!" Off we [verb], saw in hand to [verb] '
                   'this year\'s [noun] down. [Exclamation] it\'s [holiday] finally!'
    },
    {
        'id': 1,
        'title': 'More Lights!',
        'author': 'unknown',
        'content': 'Did you ever have one of those [noun] ? Well today [person] did! Mom '
                   'wanted to [verb] [nouns] up for [holiday] . Not just any lights, '
                   '[color] lights. [Adjective] [color] lights! [Adjective] bright red '
                   'lights. The only problem, they are a [verb/ed] mess! Not to mention '
                   'that there are some [vegetable], yellow and green lights [verb/ed] '
                   'in. "[person] !" I yell! This can\'t be done! She could [verb] I was '
                   'right and went out and [verb] some new shiny [color] lights!'
    },
    {
        'id': 2,
        'title': 'Turkey Dinner!',
        'author': 'unknown',
        'content': 'I spent last summer on my grandfather\'s [adjective] farm. He raises '
                   '[noun/s] for local food [noun/s] . He also grows corn on the [noun], '
                   '[adjective] lettuce and lima [noun/s] . My favorite place to [verb] '
                   'on the farm is the [adjective] house where grandfather keeps his '
                   '[noun/s] . But when I visit in November, there are no [noun/s] ! They '
                   'are all gone! I ansxiously await at the table that Thanksgiving. I '
                   'see corn on the [noun] and eve the lime [noun/s] . I am relieved when '
                   'grandma brings out a [noun] for Thanksgiving dinner!'
    },
    {
        'id': 3,
        'title': 'Pizza Pizza',
        'author': 'unknown',
        'content': 'Pizza was invented by a [adjective] [nationality] chef named [person] . '
                   'To make a pizza, you need to take a lump of [noun] , and make a thin, '
                   'round [adjective] [noun]. Then you cover it with [adjective] sauce, '
                   '[adjective] chees, and fresh chopped [noun/s] . Next you have to bake '
                   'it in a very hot [noun]. When it is done, cut it into [number] [shapes] . '
                   'Some kids like [food] pizza the best, but my favorite is the [food] pizza. '
                   'If I could, I would eat pizza [number] times a day!'
    }
]

madlibs = []


@get('/')
def get_index():
    return template('madlibs', madlibs=reversed(madlibs))

@get('/test')
def get_index():
    return template('madlibs', madlibs=reversed(templates))


@get('/template')
def get_template():
    return {'templates': templates}


@get('/template/<id:int>')
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


@get('/clear')
def get_clear():
    global madlibs
    madlibs = []


@get('/madlib')
def get_madlib():
    return {'madlibs': madlibs}


@get('/madlib/<id:int>')
def get_madlib(id):
    return madlibs[id]


@post('/madlib')
def post_madlib():
    madlib = None
    try:
        madlib = request.json
        if 'title' not in madlib or 'author' not in madlib or 'content' not in madlib:
            return {'status': 'oops, missing stuff'}
        madlibs.append(madlib)
    except Exception as e:
        return {'status': 'oops, that did not work'}
    return madlib


run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
