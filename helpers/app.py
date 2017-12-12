import os
import uuid
import bottle
from sqlite3 import OperationalError
from beaker.middleware import SessionMiddleware
from cork import Cork, AuthException
from cork.backends import SQLiteBackend


def get_init_sql():
    folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'backup')
    with open(os.path.join(folder, 'init.sql'), 'r') as _f:
        sql = ' '.join([line.strip() for line in _f.readlines()])
    return sql


def init_db():
    try:
        b = SQLiteBackend('djparrot.db', initialize=True)
        sql = '''INSERT INTO users (username, email_addr, desc, role, hash, creation_date) VALUES \
('nsavelyeva-admin', 'admin@localhost', 'Administrator', 'admin', \
'cD+Njm6BgJsTVAlSQ3qC4loRBnSUnY5qj6W6h5yzTELk4/qMiaCtg1GFoS9EKDCxrArjwt2AmB7Lh6ds7flfWDY=', \
'2017-12-10 21:20:55.352142');
INSERT INTO roles (role, level) VALUES ('admin', 100);
INSERT INTO roles (role, level) VALUES ('user', 50);'''
        b.connection.executescript(sql)
        b.connection.executescript(get_init_sql())
    except OperationalError:  # e.g. if table users/roles/register already exists
        b = SQLiteBackend('djparrot.db', initialize=False)
    return b


dbe = init_db()
aaa = Cork(backend=dbe)
authorize = aaa.make_auth_decorator(fail_redirect='/login', role='admin')


session_opts = {'session.cookie_expires': True,
                'session.encrypt_key': str(uuid.uuid4()),
                'session.httponly': True,
                'session.timeout': 86400,  # 24 hours
                'session.type': 'cookie',
                'session.validate_key': False,
               }


app = SessionMiddleware(bottle.app(), session_opts)


def whoami():
    try:
        username = aaa.current_user.username
    except AuthException:
        username = 'Guest'
    return username
