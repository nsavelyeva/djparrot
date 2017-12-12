import os
import bottle
from helpers import queries
from helpers.forms import SearchForm, WordsForm


@bottle.route('/')
@bottle.route('/home')
def home():
    return bottle.template('home')


@bottle.route('/words', method=['POST', 'GET'])
def words():
    flashes = []
    languages = queries.get_languages()
    categories = queries.get_categories()
    category = subcategory = lang_checkbox = None
    if bottle.request.method == 'POST':
        flashes = WordsForm().validate(bottle.request) 
        if not flashes:
            category = bottle.request.forms.get('category').strip()
            subcategory = bottle.request.forms.get('subcategory').strip()
            lang_checkbox = bottle.request.forms.getall('lang_checkbox')
    category = category or categories[0][0]
    subcategories = queries.get_subcategories(category)
    subcategory = subcategory or subcategories[0][0]
    lang_checkbox = lang_checkbox or ['en']
    words = queries.get_words_by_subcategory(subcategory, lang_checkbox)
    flashes.append(('info', 'Found %s items' % len(words)))
    return bottle.template('words', flashes=flashes, languages=languages, words=words,
                           categories=categories, subcategories=subcategories,
                           category=category, subcategory=subcategory, lang_checkbox=lang_checkbox)


@bottle.route('/search', method=['POST', 'GET'])
def search():
    flashes = []
    languages = queries.get_languages()
    entry, words, lang_checkbox = '', [], ['en']
    if bottle.request.method == 'POST':
        flashes = SearchForm().validate(bottle.request)
        entry = bottle.request.forms.get('search').strip()  # keep entry even if validation failed
        if not flashes:
            lang_checkbox = bottle.request.forms.getall('lang_checkbox') or ['en']
            word = entry.decode('utf8').encode('ascii', 'xmlcharrefreplace').replace("'", "''")
            words = queries.get_words_by_search(word, lang_checkbox, True)
    words = [dict(zip([item for item in lang_checkbox], row)) for row in words]
    flashes.append(('info', 'Found %s items' % len(words)))
    return bottle.template('search', flashes=flashes, languages=languages, words=words, entry=entry,
                           lang_checkbox=lang_checkbox)


@bottle.route('/story')
def story():
    languages = queries.get_languages()
    folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'readings')
    files = [item[:item.rfind('.')] for item in os.listdir(folder) if item.endswith('.txt')]
    stories = {}
    for story in files:
        description = ' '.join(item.title() for item in story.replace('__', '_-_').split('_'))
        stories.update({story: ('[%s]' % description[:2].upper()) + description[2:]})
    return bottle.template('story', languages=languages, stories=stories)
