# A box plot (also known as a box-and-whisker plot) shows the spread and central tendency of a numeric variable, and helps identify:

# Median
# Quartiles (Q1 and Q3)
# Interquartile Range (IQR)
# Outliers


import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
penguins = sns.load_dataset("penguins")

# Box plot of body mass by species
sns.boxplot(data=penguins, x="species", y="body_mass_g", hue  ="sex")

plt.title("Box Plot: Body Mass by Penguin Species")
plt.xlabel("Species")
plt.ylabel("Body Mass (g)")
plt.show()
