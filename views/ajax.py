import os
import json
import bottle
from helpers import queries


@bottle.get('/_get_statistics/')
def statistics():
    categories_count = len(queries.get_categories())
    statistics = {"words": None, "relations": None, "languages": None,
                  "categories": categories_count,
                  "subcategories": queries.get_rows_count("categories") - categories_count}
    for table in ["words", "relations", "languages"]:
        statistics.update({table: queries.get_rows_count(table)})
    return json.dumps(statistics)


@bottle.get('/_get_subcategories/<cid:int>')
def subcategories(cid):
    subcategories = queries.get_subcategories(cid)
    result = [list(item) for item in subcategories]
    return json.dumps(result)


@bottle.post('/_get_story/')
def get_story():
    folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'readings')
    longtext = bottle.request.forms.get('longtext')
    with open(os.path.join(folder, '%s.txt' % longtext), 'rb') as _f:
        longtext = _f.read()
    return longtext


@bottle.post('/_add_to_db/')
def add_to_db():
    flashes = []
    subcategory = int(bottle.request.forms.get('subcategory').strip())
    translations = json.loads(bottle.request.forms.get('translations'))
    translations = {key: value.encode('ascii', 'xmlcharrefreplace')
                    for key, value in translations.items()}
    word_id = queries.get_word_id(translations['en'])
    if word_id:
        flashes.append(('info', 'The translations are already in the database.'))
    else:
        word_id = queries.add_translations_to_db(translations)
        if word_id:
             flashes.append(('success', 'Translations have been added to the database.'))
        else:
            flashes.append(('danger', 'Could not add translations to the database.'))
            return json.dumps(flashes)
    if queries.link_translations_to_subcategory(word_id, subcategory):
        flashes.append(("success", "Translations have been linked to the category."))
    else:
        flashes.append(("danger", "Could not link translations to the subcategory."))
    return json.dumps(flashes)
