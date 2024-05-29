# df has format:
#      x_val    y_val    col
# 0    0.200    0.333    1.0
# 1    0.003    0.231    2.0
# ...  ...      ...      ...
# 7    0.025    0.361    1.0
df = ...
           #violet    #green     #orange
colors = ['#747FE3', '#8EE35D', '#E37346']
sns.scatterplot(data=df, x=x_val, y=y_val, hue=col, palette=colors)
