# A regression plot in Seaborn is used to show the linear relationship between two continuous
#  (numeric) variables — along with the best-fit regression line.

# It’s very useful for predictive analysis and identifying trends in your data.

import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
penguins = sns.load_dataset("penguins")

# Create a regression plot
sns.regplot(data=penguins, x="flipper_length_mm", y="body_mass_g" , scatter = False , color="blue")
# scatter means the scattering of the dots as the dots scattering can also be controlled
# color means what will be the color of the plot

plt.title("Regression Plot: Flipper Length vs Body Mass")
plt.xlabel("Flipper Length (mm)")
plt.ylabel("Body Mass (g)")
plt.show()
