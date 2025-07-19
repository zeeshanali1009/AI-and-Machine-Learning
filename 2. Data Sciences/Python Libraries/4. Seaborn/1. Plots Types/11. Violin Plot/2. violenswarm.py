# this is the combination of tge violin and swarm plot 
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
penguins = sns.load_dataset("penguins")

# Create the violin plot
sns.violinplot(data=penguins, x="species", y="body_mass_g")

# Overlay with swarm plot
sns.swarmplot(data=penguins, x="species", y="body_mass_g", color="black" , size=3)

plt.title("Violin + Swarm Plot: Body Mass by Species and Sex") 
plt.xlabel("Species")
plt.ylabel("Body Mass (g)")
plt.legend(title="Sex")
plt.show()
