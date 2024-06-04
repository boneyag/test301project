import seaborn as sns

df = sns.laod_dataset('tips')
g = sns.FacetGrid(data='tips', col='time', row='sex')
g.map(sns.lmplot, 'total_bill', 'tip')
