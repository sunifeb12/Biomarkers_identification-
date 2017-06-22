import pandas as pd

data1 = pd.read_csv("DEGs_SRR926256.csv")
data2 = pd.read_csv("DEGs_SRR926257.csv")
data3 = pd.read_csv("DEGs_SRR926258.csv")
data4 = pd.read_csv("DEGs_SRR926259.csv")
data5 = pd.read_csv("DEGs_SRR926260.csv")
data6 = pd.read_csv("DEGs_SRR926261.csv")
data7 = pd.read_csv("DEGs_SRR926262.csv")

list1 = data1["gene_id"]
list2 = data2["gene_id"]
list3 = data3["gene_id"]
list4 = data4["gene_id"]
list5 = data5["gene_id"]
list6 = data6["gene_id"]
list7 = data7["gene_id"]

names1 = []
names2 = []
names3 = []
names4 = []
names5 = []
names6 = []
names7 = []

for item in list1:
	names1.append(item)

for item in list2:
	names2.append(item)

for item in list3:
	names3.append(item)

for item in list4:
	names4.append(item)

for item in list5:
	names5.append(item)

for item in list6:
	names6.append(item)

for item in list7:
	names7.append(item)


thefile = open('output7.txt', 'w')

for name in names1:
	if name in names2:
		if name in names3:
			if name in names4:
				if name in names5:
					if name in names6:
						if name in names7:
							#print name
							thefile.write("%s\n" % name)

thefile = open('output6.txt', 'w')

for name in names1:
	if name in names2:
		if name in names3:
			if name in names4:
				if name in names6:
					if name in names7:
						#print name
						thefile.write("%s\n" % name)
