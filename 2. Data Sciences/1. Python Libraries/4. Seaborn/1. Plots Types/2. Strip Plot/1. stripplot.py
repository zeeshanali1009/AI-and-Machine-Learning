# Strip plot in Seaborn is used to display the distribution of a categorical variable against a numeric variable — like a scatter plot,
#  but aligned along a category axis.

import seaborn as sns
import matplotlib.pyplot as plt

# Load data
penguins = sns.load_dataset("penguins")

# Basic strip plot
sns.stripplot (data=penguins, x="species", y="body_mass_g" , dodge= True, jitter = True )
# dodge will spread my datapoints based on the hue
# jitter has been added for the better readability as the jitter spreads the datapoints on the far

plt.title("Body Mass Distribution by Penguin Species")
plt.xlabel("Species")
plt.ylabel("Body Mass (g)")
plt.show()
