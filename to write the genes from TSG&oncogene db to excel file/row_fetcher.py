import pandas as pd

data = pd.read_csv("DEGs_SRR926257.csv")
genes = pd.read_csv("TSGs_in_DEGs_SRR926257.txt", header = None).values
result = pd.DataFrame(columns=data.columns.values)

for gene in genes:
	result.loc[len(result)] = data[data.gene_id == gene[0]].values[0]
	
result.to_csv('TSGs_in_DEGs_SRR926257.csv', sep=',')