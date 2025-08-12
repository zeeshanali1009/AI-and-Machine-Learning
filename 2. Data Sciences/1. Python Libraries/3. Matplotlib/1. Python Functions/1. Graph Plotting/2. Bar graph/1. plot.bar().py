# plot.bar() functio is used to plot the bar graph
# plt.bar(x,height , color = "color name", width  = value, label  = "label name")

import matplotlib.pyplot as plt
product  = ["A","B","C","D","E"]
sales  = [100,2000,3000,1222,5634]

plt.bar(product, sales, color  = "orange", label  = "2012 Sales Data")
plt.xlabel("Product")                               # it is the label of the y-axis
plt.ylabel("Sales")                                 # it is the label of the y-axis
plt.title("Monthly Sales Comparison")               # It is the title of the graph
plt.legend()                                        # it explains that what are the different colors are doing in the graph
plt.show()