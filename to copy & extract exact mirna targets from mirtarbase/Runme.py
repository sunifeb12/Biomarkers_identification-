import pandas as pd
data = pd.read_csv("Mirtarbase_human_interactions_database.csv")
result = pd.DataFrame()
match  = 'hsa-miR-6807-'== data.miRNA.values
result = data[match]
result.to_csv('mirtarbase_miR-6807_SRR926257.csv', sep=',')
#print data.miRNA.values
