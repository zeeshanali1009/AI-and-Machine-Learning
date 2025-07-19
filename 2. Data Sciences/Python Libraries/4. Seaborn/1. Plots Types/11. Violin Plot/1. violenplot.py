# A violin plot combines:
# A box plot: showing median, quartiles, and potential outliers.
# A KDE (Kernel Density Estimate): showing the distribution shape (like a smoothed histogram, mirrored on both sides).
# width of the violen plot represents the density at the different values 
# middle line  = median


import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
penguins = sns.load_dataset("penguins")

# Violin plot of body mass by species
sns.violinplot(data=penguins, x="species", y="body_mass_g", hue  ="sex", split  = True)


plt.title("Violin Plot: Body Mass by Penguin Species")
plt.xlabel("Species")
plt.ylabel("Body Mass (g)")
plt.show()
