# plot.scatter() function is used to plot the scatter plot
# scatter plot: it is the graph in which every point represents one observation with two values.
# it is used to find the correlation between the data 
# it is also used in machine learning , clustering , regression, visualization 
# plt.scatter(x,y,color="color name", marker  = "marker style", label  = "Label name")

import matplotlib.pyplot as plt
hours_studied  = [1,2,3,4,5,6,7,8,9,10]
exam_score = [56,34,4,34,56,34,56,34,23,45]

plt.scatter(hours_studied, exam_score,color="blue", marker  = "o", label  = "Students Analysis Data")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.title("Relationship between study time and exam score")
plt.legend()
plt.grid(True)
plt.show()