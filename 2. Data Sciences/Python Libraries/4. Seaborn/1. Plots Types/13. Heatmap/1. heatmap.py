# heatmap  is a 2-d color matrix that shows the relationships or pattern between two variables 
# it is commonly used for the 
# show the correlation between features 
# visualize the confusion matrices 
# highlights the missing data like sns.heatmap(df.isnull())

import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
penguins = sns.load_dataset("penguins")

# Drop non-numeric columns
penguins_numeric = penguins.select_dtypes(include='number')

# Create correlation matrix
corr_matrix = penguins_numeric.corr()

# Plot heatmap
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")

plt.title("Correlation Heatmap of Penguin Features")
plt.show()
 