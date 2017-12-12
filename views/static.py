import bottle


@bottle.route('/static/css/<file_path:re:.*\.css>')
def css(file_path):
    return bottle.static_file(file_path, root='static/css')


@bottle.route('/static/fonts/<file_path:re:.*\.(otf|eot|svg|ttf|woff|woff2)>')
def fonts(file_path):
    return bottle.static_file(file_path, root='static/fonts')


@bottle.route('/static/js/<file_path:re:.*\.js>')
def js(file_path):
    return bottle.static_file(file_path, root='static/js')


@bottle.route('/static/pic/<file_path:re:.*\.png>')
def png(file_path):
    return bottle.static_file(file_path, root='static/pic')
