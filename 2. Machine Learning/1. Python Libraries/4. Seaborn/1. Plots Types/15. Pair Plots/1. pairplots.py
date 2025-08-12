# A pair plot is a great way to visualize relationships between multiple numerical variables in a dataset. 
# It creates a matrix of scatter plots, showing the relationship between each pair of features.

import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset("penguins")

# Basic pair plot
sns.pairplot(penguins)

# Pair plot with hue
sns.pairplot(penguins, hue="species", pallete= "Set2" ,diag_kind="kde")


plt.show()
