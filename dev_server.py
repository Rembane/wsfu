#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import abort, default_app, request, route, run

@route('/test1', method='POST')
def test1():
    try:
        int(request.forms.test1)
    except ValueError:
        abort(400, 'Please set test1 to an integer.')

    if not type(request.forms.test2) == type(''):
        abort(400, 'Please set test2 to a string.')

    return ''

if __name__ == "__main__":
    run()

# To make gunicorn play nice with bottle.
app = default_app()
