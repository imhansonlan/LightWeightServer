#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import logging
from tornado import ioloop
from tornado import web
import socket
import argparse
import sys
import os


if os.name == 'nt':
    reload(sys)
    sys.setdefaultencoding('gb18030')

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def server(host, port, site_dir):
    # Importing here to seperate the code paths from the --livereload
    # alternative.
    application = web.Application([
        (r"/(.*)", web.StaticFileHandler, {
            "path": site_dir,
            "default_filename": "index.html"
        }),
    ])
    try:
        application.listen(port=int(port), address=host)
    except socket.error:
        log.info('Error: Port %s is Exists, Use another one.' % port)
        sys.exit()

    log.info('Running at: http://%s:%s/', host, port)
    log.info('Hold ctrl+c to quit.')
    try:
        ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        log.info('Stopping server...')


def main():
    desc = '''Simple http server with tornado'''
    port_help = 'The site port(default: 8080), ignore this option if site_addr is not empty'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('-a', '--addr',
                        metavar='site_addr',
                        type=str,
                        help='The site addr, host:port')
    parser.add_argument('-p', '--port',
                        metavar='port',
                        type=int,
                        default=8080,
                        help=port_help)
    parser.add_argument('dir',
                        metavar='site_dir',
                        nargs='?',
                        help='The site dir')

    args = parser.parse_args()
    site_dir = args.dir
    site_addr = args.addr
    port = args.port
    host = '0.0.0.0'

    if site_dir is None:
        parser.print_help()
        sys.exit()

    if not os.path.isdir(site_dir):
        log.info('Please set the site dir')
        sys.exit()

    if site_addr is not None:
        host, port = site_addr.split(':', 1)

    # Bootstrap
    server(host, port, site_dir)

if __name__ == "__main__":
    main()
