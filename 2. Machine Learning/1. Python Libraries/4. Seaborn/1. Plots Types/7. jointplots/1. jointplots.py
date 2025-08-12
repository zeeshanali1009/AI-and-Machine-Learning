# A joint plot in Seaborn combines:
# A scatter plot (or another type) showing the relationship between two variables.
# Marginal histograms (or KDEs) on the top and right of the main plot to show univariate distributions.

import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
penguins = sns.load_dataset("penguins")

# Create a jointplot
sns.jointplot(data=penguins, x="flipper_length_mm", y="body_mass_g", hue  = "sex", kind  ="regression")

plt.show()
