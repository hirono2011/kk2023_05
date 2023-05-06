#!python3

import re
import pyperclip

path = input("path:") #対話で文字入力を促す
path.strip()
xpath = re.sub('.+(images.+)', r'\1', path) #正規表現の後方参照
text = """
<figure><img src='{p}'><figcaption>{p}</figcaption></figure>
""".format(p=xpath)

pyperclip.copy(text)
print(text)

