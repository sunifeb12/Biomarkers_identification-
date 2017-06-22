import pandas as pd
data1 = pd.read_csv("mirtarbase_miR-98_SRR926262.csv")
data2 = pd.read_csv("DEGs_SRR926262.csv")

list1 = data1["Target Gene"]
list2 = data2["gene_id"]

names1 = []
names2 = []

for item in list1:
	names1.append(item)

for item in list2:
	names2.append(item)

thefile = open('output_miR-98.txt', 'w')

for name in names1:
	if name in names2:
		#print name
		thefile.write("%s\n" % name)

