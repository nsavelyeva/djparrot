import os
import re
import datetime
from app import dbe


def backup_alias(file_name):
    """Transform: 'djparrot_2017-12-11_15-05-25-167.sql' --> '2017-12-11 15-05-25-167'."""
    return file_name.split(os.sep)[-1].replace('djparrot_', '').replace('_', '').replace('.sql', '')


def collect_backups(folder):
    pattern = r'djparrot_[0-9\-_]{23,26}\.sql'
    backups = [item for item in os.listdir(folder)
               if re.match(pattern, item) and os.path.isfile(os.path.join(folder, item))]
    return sorted(backups, reverse=True)


def remove_old_backups(folder, max_backups=10):
    flashes = []
    backups = collect_backups(folder)
    for file_name in backups[max_backups:]:
        try:
            os.remove(os.path.join(folder, file_name))
        except OSError as err:
            msg = '"%s" due to OS error: %s' % (backup_alias(file_name), err)
            flashes.append(('danger', 'Could not delete backup %s.' % msg))
    return flashes


def restore_db_from_file(file_name):
    tables = ['languages', 'categories', 'words', 'relations']
    try:
        with open(file_name, 'r') as _f:
            sql = [line.strip() for line in _f.readlines()]
        # 1st line is 'BEGIN TRANSACTION;' - need to insert 'DROP TABLE' before 'CREATE TABLE'
        sql[0] += ' ' + '; '.join('DROP TABLE IF EXISTS %s' % table for table in tables) + ';'
        dbe.connection.executescript(' '.join(sql))
        msg = 'reset' if 'init' in file_name else 'restored from "%s"' % backup_alias(file_name)
        flashes = [('success', 'Database has been %s.' % msg)]
    except Exception as err:
        flashes = [('danger', 'Failed to %s the database due to error: %s.' %
                   ('reset' if 'init' in file_name else 'restore', err))]
    return flashes


def db_reset(folder):
    flashes = restore_db_from_file(os.path.join(folder, 'init.sql'))
    return flashes


def db_import(folder, file_name):
    flashes = restore_db_from_file(os.path.join(folder, file_name))
    return flashes


def db_export(folder):
    file_name = 'djparrot_%s.sql' % datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')[:-3]
    with open(os.path.join(folder, file_name), 'w') as _f:
        for line in dbe.connection.iterdump():
            # authentication queries will be skipped (tables: users, roles, register)
            parts = line.split(' ')
            if len(parts) < 3 or parts[2].replace('"', '') not in ['users', 'roles', 'register']:
                _f.write('%s\n' % line)
    flashes = [('success', 'Backup "%s" has been created.' % backup_alias(file_name))]
    flashes.extend(remove_old_backups(folder))
    return flashes
