#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functools import partial
from itertools import cycle, islice, izip
from qc import integers, unicodes
from requests.api import request
import sys, urlparse, yaml

MAX_NUM = 10

types = { 
    'str' : partial(unicodes, size=(0,10), minunicode=0, maxunicode=127),
    'int' : partial(integers, low=0, high=100000),
}

with open(sys.argv[1]) as fn:
    data = yaml.load(fn.read())
    base = data['base']
    for view in data['views']:
        for parameters in zip(*[list(islice(izip(cycle([f['name']]), types[f['expected']]()), 0, MAX_NUM)) for f in view['fields']]):
            r = request(view['method'], urlparse.urljoin(base, view['url']), data=dict(parameters))
            print r.url, r.status_code, dict(parameters), r.text



