import seaborn as sns 
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np

print(sns.get_dataset_names())


penguins  = sns.load_dataset("penguins")
print(penguins.head())


sns.scatterplot(data=penguins, x="species", y="body_mass_g", hue="island", style  = "sex", alpha  = 0.5 )        
# hue means that the species are been scattered on the basis of islands
# alpha will decrease the opacity by 0.5 
# style means the on what base the plot has been scattered and here style is the sex like sex means the
#  scattering has been completed base on the sex 
plt.show()