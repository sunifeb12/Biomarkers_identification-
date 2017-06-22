import pandas as pd

data1 = pd.read_csv("mirtarbase_miR-6892_SRR926256.csv")["Target Gene"]
data2 = pd.read_csv("DEGs_SRR926256.csv")["gene_id"]

common = set(data1).intersection(data2)
outfile = open('output_miR-6892.txt', 'w')
if bool(common):
	outfile.write("\n".join(common))
else:
	outfile.write("No Common Targets Found")
outfile.close()