# Scatter plot is a type of data visualization used to show the relationships between two numerical variables 
# Each point represents the observation with two values which are as the x-axis and y-axis aswell
# It is used to find the correlation between the data

import seaborn as sns 
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np

print(sns.get_dataset_names())


penguins  = sns.load_dataset("penguins")
print(penguins.head())

print(penguins["species"].value_counts())
print(penguins["island"].value_counts())


sns.scatterplot(data=penguins, x="flipper_length_mm", y="body_mass_g", hue="island")        
# hue means that the species are been scattered on the basis of islands
plt.show()