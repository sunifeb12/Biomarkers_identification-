import pandas as pd
data = pd.read_csv("gene type & regulation type_SRR926257.csv")

PCUR = data[ (data['gene type'] == 'protein coding') & (data['regulation type'] == 'up regulation')]
PCDR = data[ (data['gene type'] == 'protein coding') & (data['regulation type'] == 'down regulation')]

PSEUDOCUR = data[ (data['gene type'] == 'pseudo') & (data['regulation type'] == 'up regulation')]
PSEUDOCDR = data[ (data['gene type'] == 'pseudo') & (data['regulation type'] == 'down regulation')]

SNORNAUR = data[ (data['gene type'] == 'snoRNA') & (data['regulation type'] == 'up regulation')]
SNORNADR = data[ (data['gene type'] == 'snoRNA') & (data['regulation type'] == 'down regulation')]

NCRNA = data[ data['gene type'] == 'ncRNA']


MIRNAUP = NCRNA[ (NCRNA['ncRNA type'] == 'miRNA') & (NCRNA['regulation type'] == 'up regulation')]
MIRNADR = NCRNA[ (NCRNA['ncRNA type'] == 'miRNA') & (NCRNA['regulation type'] == 'down regulation')]

LNCRNAUP = NCRNA[ (NCRNA['ncRNA type'] == 'LncRNA') & (NCRNA['regulation type'] == 'up regulation')]
LNCRNADR = NCRNA[ (NCRNA['ncRNA type'] == 'LncRNA') & (NCRNA['regulation type'] == 'down regulation')]

GUIDERNAUP = NCRNA[ (NCRNA['ncRNA type'] == 'Guide RNA') & (NCRNA['regulation type'] == 'up regulation')]
GUIDERNADR = NCRNA[ (NCRNA['ncRNA type'] == 'Guide RNA') & (NCRNA['regulation type'] == 'down regulation')]

print 'Protein Coding - Up Regulated : ', PCUR.shape[0]
print 'Protein Coding - Down Regulated : ', PCDR.shape[0]

print 'Pseudo - Up Regulated : ', PSEUDOCUR.shape[0]
print 'Pseudo - Down Regulated : ', PSEUDOCDR.shape[0]

print 'snoRNA - Up Regulated : ', SNORNAUR.shape[0]
print 'snoRNA - Down Regulated : ', SNORNADR.shape[0]

print 'Total ncRNAs : ', NCRNA.shape[0]

print 'miRNA - Up Regulated : ', MIRNAUP.shape[0]
print 'miRNA - Down Regulated : ', MIRNADR.shape[0]

print 'LncRNA - Up Regulated : ', LNCRNAUP.shape[0]
print 'LncRNA - Down Regulated : ', LNCRNADR.shape[0]

print 'Guide RNA - Up Regulated : ', GUIDERNAUP.shape[0]
print 'Guide RNA - Down Regulated : ', GUIDERNADR.shape[0]