import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("darkgrid")
sns.stripplot(x="day", y="total_bill", data=tips)
sns.set_style("white")
sns.despine()

pallete = sns.color_palette('bright')
sns.palplot(pallete)

# Seaborn has six variations of its default color palette: deep, muted, pastel, bright, dark, and colorblind.