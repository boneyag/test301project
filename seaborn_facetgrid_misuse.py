import seaborn as sns

df = sns.laod_dataset('tips')
sns.lmplot(data=df, x='total_bill', y='tip', col='time', row='sex')
