import pandas as pd
data1 = pd.read_csv("mirtarbase_miR-7-1_SRR926258.csv")
data2 = pd.read_csv("DEGs_SRR926258.csv")

list1 = data1["Target Gene"]
list2 = data2["gene_id"]

names1 = []
names2 = []

for item in list1:
	names1.append(item)

for item in list2:
	names2.append(item)

thefile = open('output_miR-7-1.txt', 'w')

for name in names1:
	if name in names2:
		#print name
		thefile.write("%s\n" % name)

