#!/usr/bin/env python


import json
import gzip
import redis

price_obj = redis.Redis("localhost", port=6379, db=1)

def parse(path):
  g = gzip.open(path, 'r')
  for l in g:
    yield json.dumps(eval(l))

print 'Starting loading to Redis !'

for l in parse("data/metadata.json.gz"):
  price_obj.set(l.get('asin'), l.get('price'))

print 'Loaded to Redis !'