# It draws small vertical (or horizontal) lines (like tiny "rugs") along an axis.

# Each line represents one data point.
# Good for showing distribution of values.

import seaborn as sns
import matplotlib.pyplot as plt

# Load data
penguins = sns.load_dataset("penguins")

# Rug plot on flipper length
sns.rugplot(data=penguins, x="body_mass_g", hue   = "species", palette="Set2", height= 0.2)

plt.show()
