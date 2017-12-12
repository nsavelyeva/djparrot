import bottle
from helpers.app import aaa, whoami


@bottle.route('/login', method=['POST', 'GET'])
def login():
    if bottle.request.method == 'POST':
        username = bottle.request.POST.get('username', '').strip()
        password = bottle.request.POST.get('password', '').strip()
        result = aaa.login(username, password)
        if result:
            return bottle.redirect('/admin')
        return bottle.template('login', flashes=[('danger', 'Login failed. Please try again.')])
    flashes = []
    username = whoami()
    if username != 'Guest':
        flashes.append(('info', 'You are already logged in as <b>%s.</b>' % username))
    return bottle.template('login', flashes=flashes)


@bottle.route('/logout')
def logout():
    aaa.logout(success_redirect='/login', fail_redirect='/login')


@bottle.error(404)
def error404(error):
    flashes = [('danger', 'Page Not Found.')]
    return bottle.template('error', flashes=flashes)


@bottle.error(500)
def error500(error):
    flashes = [('danger', 'Internal Server Error.')]
    return bottle.template('error', flashes=flashes)