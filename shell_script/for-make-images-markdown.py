#!python3

import os
import glob
import re
import pyperclip
import textwrap

full_text = ""
i=0
for file in sorted(glob.glob('./*')):
	if re.match('.+\.(jpg|JPG|jpeg|JPEG|png|PNG)', file):
		path = os.path.abspath(file)
		xpath = re.sub('.+(images.+)', r'\1', path) #正規表現の後方参照
		text = '''
			![{p}]({p})
			<div class="img_name">
			{p}

			</div>
			\n
		'''.format(p=xpath)
		i = i + 1

		print(textwrap.dedent(text)[1:-1])
		full_text = full_text + textwrap.dedent(text)[1:-1]

mes = '{i}件のファイルを処理しました。'.format(i=i)		
print(mes)
		
pyperclip.copy(full_text)
        
