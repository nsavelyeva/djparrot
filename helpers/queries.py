from helpers.app import dbe


def get_rows_count(table):
    sql = 'SELECT COUNT(*) FROM ' + table.replace('"', '').replace("'", '')
    result = dbe.connection.execute(sql).fetchone()[0]
    return result


def get_languages():
    sql = 'SELECT * FROM languages ORDER BY title'
    result = dbe.connection.execute(sql).fetchall()
    return result


def get_categories():
    sql = 'SELECT * FROM categories WHERE pid=0 ORDER BY title'
    result = dbe.connection.execute(sql).fetchall()
    return result


def get_subcategories(category_id):
    sql = 'SELECT * FROM categories WHERE pid = ? ORDER BY title'
    result = dbe.connection.execute(sql, (category_id,)).fetchall()
    return result


def get_category_by_title(category_title):
    sql = 'SELECT * FROM categories WHERE title="%s"' % category_title
    result = dbe.connection.execute(sql).fetchone()
    return result


def get_words_by_subcategory(subcategory, languages, raw=False):
    sql = 'SELECT ' + ', '.join(languages) + ' '
    sql += 'FROM words INNER JOIN relations on words.id=relations.wid ' + \
           'WHERE relations.sid = ? ORDER BY words.en'
    words = dbe.connection.execute(sql, (subcategory,)).fetchall()
    if not raw:
        words = [dict(zip(languages, row)) for row in words]
    return words


def get_words_by_search(entry, languages, raw=False):
    sql = 'SELECT ' + ', '.join(languages)
    sql += ", ' ' || " + ' || '.join(languages) + " || ' ' AS concatenated "
    sql += "FROM words WHERE concatenated LIKE '%" + entry + "%'"
    words = dbe.connection.execute(sql).fetchall()
    if not raw:
        words = [dict(zip(languages, row)) for row in words]
    return words


def get_word_id(en_word):
    sql = 'SELECT id FROM words WHERE en = ?'
    result = dbe.connection.execute(sql, (en_word,)).fetchone()
    if result:
        result = result[0]
    return result


def add_translations_to_db(translations):
    values = (translations['en'], translations['ru'], translations['nl'], translations['de'],
              translations['fr'], translations['es'], translations['pl'], translations['lt'],
              translations['el'], translations['hi'])
    sql = 'INSERT INTO "words" (en, ru, nl, de, fr, es, pl, lt, el, hi) VALUES '
    dbe.connection.execute(sql + '(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', values)
    dbe.connection.commit()
    word_id = get_word_id(translations['en'])
    return word_id


def link_translations_to_subcategory(word_id, subcategory):
    sql = 'INSERT INTO "relations" (wid, sid) VALUES(?, ?)'
    dbe.connection.execute(sql, (word_id, subcategory))
    dbe.connection.commit()
    return True
