import pandas as pd

# Subject gaps

sents = []
with open('fgd_subject.txt', 'r') as f:
    item = 1
    for line in f:
        line = line.strip()
        sents.append(line)

data = {'sent': sents}
data = pd.DataFrame.from_dict(data)
data.to_csv('fgd_subject.tsv', index=False, sep='\t')
