# A line plot displays information as a series of data points connected by a line. It’s typically used when:

# Show a trend over time (e.g., sales, temperature).
# Compare multiple trends using color or style

import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
penguins = sns.load_dataset("penguins")

# Create a line plot
sns.set_style("whitegrid")
sns.lineplot(data=penguins, x="flipper_length_mm", y="body_mass_g", hue  = "island" , style  = "sex")

plt.title("Line Plot: Flipper Length vs Body Mass")
plt.xlabel("Flipper Length (mm)")
plt.ylabel("Body Mass (g)")
plt.show()
