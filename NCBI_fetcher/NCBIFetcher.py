import pandas as pd
import numpy as np
import requests
import time
import re

genes = np.loadtxt('all DEGs_IDs_SRR926256.txt')
col = ['id', 'attribute']
result = pd.DataFrame(columns = col)
link = 'https://www.ncbi.nlm.nih.gov/gene/?term='

for gene in genes:

	page = requests.get(link+str(int(gene)))
	if page.status_code == 200:
		content = page.content
		if content.find('Gene type'):
			location = content.find('Gene type')
			term = content[location:location+100]
			term = term.replace('\n','')
			if re.search('(Gene type)(</dt>)(\s+)(<dd>)(.*)(</dd>)(.*)', content):
				name =re.search('(Gene type)(</dt>)(\s+)(<dd>)(.*)(</dd>)(.*)', content)
				attribute = name.group(5)
			else:
				attribute = 'multiple hits'
		else:
			attribute = 'nofield'
	else:
		attribute = 'NA'

	result.loc[len(result)] = [gene, attribute]
	print gene, attribute	
	time.sleep(5)
result.to_csv('genetype_SRR926256_DEGs.csv', sep=',', index = False)






