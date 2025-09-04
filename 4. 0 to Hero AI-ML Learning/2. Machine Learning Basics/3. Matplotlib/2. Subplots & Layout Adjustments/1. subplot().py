# subplot() basically divides the the figure into rows and columns
# plt.subplot(nrows, ncols, index)
# it is also said to be the object oriented approach as well as we have the control of our graphs in our own hand

import matplotlib.pyplot as plt 
x = [1,2,3,4,5]
y = [12,34,45,62,34]

plt.subplot(1,2,1)       # 1 row, 2 columns , 1st subplot
plt.plot(x,y)
plt.title("Line Chart")

plt.subplot(1,2,2)       # 1 row, 2 columns , 1st subplot
plt.bar(x,y)
plt.title("Bar Chart")


# this statement is for the better adjustments od the graphs 
plt.tight_layout()
plt.show()
