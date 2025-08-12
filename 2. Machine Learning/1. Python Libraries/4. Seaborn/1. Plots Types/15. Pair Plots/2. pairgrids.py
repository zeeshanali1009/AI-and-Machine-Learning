# A PairGrid is a more customizable and flexible version of pairplot. 
# While pairplot is a shortcut that does everything automatically, 
# PairGrid allows manual control over how each plot in the grid is drawn.
import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset("penguins")


graph = sns.PairGrid(data=penguins, hue  = "sex", palette="Set2")
graph.map_upper(sns.scatterplot)    # upper triangle 
graph.map_lower(sns.scatterplot)    # lower triangle 
graph.map_diag(sns.histplot)        # diagonal
graph.add_legend()


plt.show(   )