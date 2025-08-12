# A bar plot displays the mean (by default) of a numerical variable for each category of a categorical variable.

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load dataset
penguins = sns.load_dataset("penguins")

# Bar plot: average body mass per species
sns.barplot(data=penguins, x="species", y="body_mass_g", pallete = ["pink" , "skyblue"], estimator=np.sum())


plt.title("Average Body Mass per Penguin Species")
plt.xlabel("Species")
plt.ylabel("Body Mass (g)")
plt.show()
