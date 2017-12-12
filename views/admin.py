import os
import json
import urllib2
import requests
import bottle
from helpers import queries
from helpers.db import db_export, db_import, db_reset, collect_backups
from helpers.app import authorize, whoami
from helpers.forms import TranslateForm


@bottle.route('/admin', method=['POST', 'GET'])
@authorize()
def manage():
    flashes = []
    folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'backup')
    if bottle.request.method == 'POST':
        admin_action = bottle.request.forms.get('admin_action')
        if admin_action == 'backup':
            flashes.extend(db_export(folder))
        elif admin_action == 'reset':
            flashes.extend(db_reset(folder))
        elif admin_action == 'restore':
            flashes.extend(db_import(folder, bottle.request.forms.get('backup')))
    backups = collect_backups(folder)
    flashes.append(('info', 'Found %s backup(s)' % len(backups)))
    return bottle.template('admin', flashes=flashes, username=whoami(), backups=backups)


@bottle.route('/translate', method=['POST', 'GET'])
@authorize()
def translate():
    flashes = []
    entry, src_language, translation = '', 'en', {}
    languages = queries.get_languages()
    if bottle.request.method == "POST":
        flashes = TranslateForm().validate(bottle.request)
        if not flashes:
            src_language = bottle.request.forms.get('src_language')
            entry = bottle.request.forms.get('entry')
            translation = {src_language: entry}
            for lang in [item[1] for item in languages]:
                url = 'https://translate.googleapis.com/translate_a/single'
                url += '?ie=UTF-8&oe=UTF-8&client=gtx'
                url += '&sl=%s&tl=%s&dt=t&q=%s' % (src_language, lang, urllib2.quote(entry))
                response = requests.get(url)
                if response.status_code == 200:
                    response_text = response.text.encode('ascii', 'xmlcharrefreplace')
                    try:
                        # response.text: [[["brave hond","good dog",null,null,1]],null,"en"]
                        translation.update({lang: json.loads(response_text)[0][0][0]})
                    except IndexError:
                        flashes.append(('danger', 'Unexpected response data: %s' % response.text))
                else:
                    flashes.append(('danger', 'Unexpected response: %s %s' % (response.status_code,
                                                                              response.reason)))
    category_id = queries.get_category_by_title('Workout - customized!')[0]
    subcategories = queries.get_subcategories(category_id)
    return bottle.template('translate', flashes=flashes, username=whoami(), languages=languages,
                           src_language=src_language, subcategories=subcategories,
                           entry=entry, translation=translation)

