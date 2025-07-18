# plot() function requires the axis information within it so that we can use it for the better visualization aswell
# plt.plot (x,y , color = "color name ", linestyle  = "line style ", linewidth  = "value", marker  = "marker symbol", label = "label name ")
import matplotlib.pyplot as plt
months  = [1,2,3,4,5,6]
sales  = [100,2000,3000,1222,5634,8000]

plt.plot(months, sales, color  = "blue", linestyle = "--", linewidth  = 2, marker = "o", label  = "2012 Sales Data")
plt.xlabel("Months")
plt.ylabel("Sales Per Month")
plt.title("Monthly Sales Chart")
plt.legend(loc = "upper left", fontsize  = 12)
plt.grid(color = "gray", linestyle  = ":", linewidth  =1)

# plt.xlim(1,4)
# plt.ylim(0,1500)  Actually these two lines are limiting the graph

plt.show()
