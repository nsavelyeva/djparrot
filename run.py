# -*- coding: utf-8 -*-
import os
import socket
import argparse
import bottle


bottle.TEMPLATE_PATH.insert(0,
                            os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates')))


from helpers.app import app
from views.ajax import *
from views.common import *
from views.admin import *
from views.routes import * 
from views.static import * 


parser = argparse.ArgumentParser(description='Start DJ Parrot app. ' +
                                 'Navigate to the app directory and do "python run.py".')

parser.add_argument('-s', '--server', default='127.0.0.1', required=False,
                    help='IP address of a network interface for DJ Parrot to run on.')
parser.add_argument('-p', '--port', default=80, type=int, required=False,
                    help='a port number for DJ Parrot to listen on.')

args = vars(parser.parse_args())

try:
    bottle.run(app, host=args['server'], port=args['port'])
except OSError as err:
    print('Cannot start DJ Parrot app due to OS error:\n\t%s.' % err)
    print('Is the port %s already in use?' % args['port'])
    print('Try "run.py -h" to see launching options.')
except socket.gaierror as err:
    print('Cannot start DJ Parrot app due to socket error:\n\t%s.' % err)
    print('Is the network interface %s correct?' % args['server'])
    print('Try "run.py -h" to see launching options.')

