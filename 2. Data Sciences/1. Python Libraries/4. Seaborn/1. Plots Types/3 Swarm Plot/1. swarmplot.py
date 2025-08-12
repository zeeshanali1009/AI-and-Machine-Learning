# A swarm plot is similar to a strip plot, but it automatically adjusts the position of dots so 
# they don’t overlap — giving a clearer view of the data distribution across categories.

import seaborn as sns
import matplotlib.pyplot as plt

# Load data
penguins = sns.load_dataset("penguins")

# Create swarm plot
sns.swarmplot(data=penguins, x="species", y="body_mass_g")

plt.title("Swarm Plot: Body Mass by Penguin Species")
plt.xlabel("Species")
plt.ylabel("Body Mass (g)")
sns.set_context("talk")
plt.show()

