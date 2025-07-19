# KDE plots are used for the estimating of the probability density functions of continuous and parametric data 
# A smooth curve that shows the distribution of the data 
# it helps to see where the data is being concentrated and how it spreads

import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
penguins = sns.load_dataset("penguins")

# KDE plot for body mass
sns.kdeplot(data=penguins, x="body_mass_g" , hue  = "species"
            , palette="pastel", fill=True)

plt.title("KDE Plot of Penguin Body Mass")
plt.xlabel("Body Mass (g)")
plt.ylabel("Density")
plt.show()
