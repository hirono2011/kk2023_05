#!python3

import re
import pyperclip

path = input("path:") #対話で文字入力を促す
path.strip()
xpath = re.sub('.+(images.+)', r'\1', path) #正規表現の後方参照
text = """
<div style="page-break-before:always"></div>
<figure><img src='{p}' width='80%' height='80%'><figcaption>{p}</figcaption></figure>
<div style="page-break-before:always"></div>
""".format(p=xpath)

pyperclip.copy(text)
print(text)

