# plot.scatter() function is used to plot the scatter plot
# scatter plot: it is the graph in which every point represents one observation with two values.
# it is used to find the correlation between the data 
# it is also used in machine learning , clustering , regression, visualization 
# plt.scatter(x,y,color="color name", marker  = "marker style", label  = "Label name")

import matplotlib.pyplot as plt

plt.scatter([1,2,3], [34,56,6], color="blue", marker  = "o", label  = "Class A")
plt.scatter([1,2,3], [45,5,100], color="orange", marker  = "o", label  = "Class B")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.title("Comparison of two classes")
plt.legend()
plt.grid(True)
plt.show()