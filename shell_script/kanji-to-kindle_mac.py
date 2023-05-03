#!python3

import pykakasi
import sys

w = sys.argv[1]

kks=pykakasi.kakasi()
result = kks.convert(w)

print(''.join([item['kana'] for item in result]))
print(''.join([item['hepburn'] for item in result]))
text = '''

金沢弁護士会の30年VS金沢地方検察庁への刑事告発
カナザワベンゴシカイノサンジュウネンバーサスカナザワチホウケンサツチョウヘノケイジコクハツ
kanazawabenngoshikaino30nennVSkanazawatihoukennsatutyouhenokeijikokuhatu

さらば弁護士鉄道
サラバベンゴシテツドウ
sarababengoshitetsudou

'''

print(text)

