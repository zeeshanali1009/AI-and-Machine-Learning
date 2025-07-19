# palletes basically explains the color impact on the plot graphing process as it involves the three sets 
# set1 = bright and high contrast colors 
# set2 = softer or paster colors 
# set3  = mix of soft and bold colors

# There is three types of data as:
# 1. Qualitative (dark colors , color blinds , set1 , set2, set3)   9
# 2. Sequential  (blue , green , purples )     8
# 3. Diverging   (coolwarm color)           12

import seaborn as sns 
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np

print(sns.get_dataset_names())


penguins  = sns.load_dataset("penguins")
print(penguins.head())

print(penguins["species"].value_counts())
print(penguins["island"].value_counts())


sns.scatterplot(data=penguins, x="flipper_length_mm", y="body_mass_g", hue="island", palette="Dark2")        
# hue means that the species are been scattered on the basis of islands
sns.set_style("whitegrid")
plt.show()



