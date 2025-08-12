# plot() function requires the axis information within it so that we can use it for the better visualization aswell
# plt.plot (x,y , color = "color name ", linestyle  = "line style ", linewidth  = "value", marker  = "marker symbol", label = "label name ")
import matplotlib.pyplot as plt
months  = [1,2,3,4,5,6]
sales  = [100,2000,3000,1222,5634,8000]

plt.plot(months, sales, color  = "blue", linestyle = "--", linewidth  = 2, marker = "o", label  = "2012 Sales Data")
plt.xlabel("Months")                                            # it is the label of the y-axis
plt.ylabel("Sales Per Month")                                 # it is the label of the y-axis
plt.title("Monthly Sales Chart")                            # it is the title of the graph 
plt.legend(loc = "upper left", fontsize  = 12)    # it explains what the different colors are doing in the graph
plt.grid(color = "gray", linestyle  = ":", linewidth  =1)           # these are the background lines behind the graph

# plt.xlim(1,4)
# plt.ylim(0,1500)  Actually these two lines are limiting the graph

# Actually these are the ticks being marked on the x axis for the better understanding of the visualization

plt.xticks([1,2,3,4,5,6], ["M1","M2","M3","M4","M5","M6"])

plt.show()
