#!python3

import os
import glob
import re
import pyperclip

full_text = ""
i=0
for file in glob.glob('./*'):
	if re.match('.+\.(jpg|JPG|jpeg|JPEG|png|PNG)', file):
		path = os.path.abspath(file)
		xpath = re.sub('.+(images.+)', r'\1', path) #正規表現の後方参照
		text = '''<figure><img src='{p}'><figcaption>{p}</figcaption></figure>\n'''.format(p=xpath)
		i = i + 1
		if i % 2 == 0:
			text = text + "\n<div style='margin: 40px;'></div>\n"
		else:
			text = text + "<div style='margin: 120px;'></div>\n"

		print(text)
		full_text = full_text + text

		
pyperclip.copy(full_text)
        
