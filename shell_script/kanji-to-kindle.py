#!python

import pykakasi
import sys

w = sys.argv[1]

kks=pykakasi.kakasi()
result = kks.convert(w)

print(''.join([item['hira'] for item in result]))
print(''.join([item['kana'] for item in result]))
print(''.join([item['hepburn'] for item in result]))
