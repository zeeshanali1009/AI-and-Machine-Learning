# A histogram is used to visualize the distribution of a single numeric variable by grouping the values
#  into bins (intervals) and showing how many observations fall into each bin.

import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
penguins = sns.load_dataset("penguins")

# Create histogram of body mass
sns.histplot(data=penguins, x="body_mass_g", bins=20, hue  ="sex", multiple="stack")
# hue "sex" means that the histogram interplotation is based on the sex and the bars are been stacked 
# differntly aswell

plt.title("Histogram of Penguin Body Mass")
plt.xlabel("Body Mass (g)")
plt.ylabel("Frequency")
sns.set_context("notebook")
plt.show()
