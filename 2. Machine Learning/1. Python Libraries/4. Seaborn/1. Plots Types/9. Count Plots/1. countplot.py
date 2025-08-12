# A count plot is a bar chart that shows the number of occurrences (frequency) of each category
#  in a categorical variable.
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
penguins = sns.load_dataset("penguins")

# Count how many penguins belong to each species
sns.countplot(data=penguins, x="species")

plt.title("Count of Penguins by Species")
plt.xlabel("Species")
plt.ylabel("Count")
plt.show()
