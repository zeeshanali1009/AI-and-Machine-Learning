# the ways of styling the themes are as follow:
# white 
# dark
# whitegrid
# darkgrid
# ticks

# sns.get.style() function is used to get the style of the graph like the background design of the graph like the designing 
# of the grid

# set_context() allows us to override the default parameters.This affects the things like the 
# paper     (for the paper the dots will be small)
# notebook   (for the notebook use as the dots size will be less too)
# talk         (for the talk purposes like for the explaination the dot size will also be less)
# poster         (for the greater use the dot size will be large as well)

# sns.despine(left = true or right  = true)  ----> it turns the spines ON or OFF


# Scatter plot is a type of data visualization used to show the relationships between two numerical variables 
# Each point represents the observation with two values which are as the x-axis and y-axis aswell
# It is used to find the correlation between the data
# now understanding it with the help of the example 
# 
import seaborn as sns 
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np

print(sns.get_dataset_names())


penguins  = sns.load_dataset("penguins")
print(penguins.head())

print(penguins["species"].value_counts())
print(penguins["island"].value_counts())


sns.scatterplot(data=penguins, x="flipper_length_mm", y="body_mass_g", hue="island")        
# hue means that the species are been scattered on the basis of islands
sns.set_style("whitegrid")
sns.set_context("poster")
plt.show()



