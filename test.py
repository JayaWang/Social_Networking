# -*- coding: utf-8 -*-

import redis

r0 = redis.Redis(host='127.0.0.1', port=6379, db=0)
key = r0.keys()
print key[-1]