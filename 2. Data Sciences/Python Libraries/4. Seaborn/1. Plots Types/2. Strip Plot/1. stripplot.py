
import seaborn as sns 
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np

print(sns.get_dataset_names())


penguins  = sns.load_dataset("penguins")
print(penguins.head())



sns.scatterplot(data=penguins, x="flipper_length_mm", y="body_mass_g", hue="island")        
# hue means that the species are been scattered on the basis of islands
plt.show()