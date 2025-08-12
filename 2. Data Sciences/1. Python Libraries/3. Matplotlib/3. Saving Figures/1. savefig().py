# savefig() function is used to save the figure into the desired format 
# savefig("filename.extension, dpi = value, bbox_inches  = "tighti")

import matplotlib.pyplot as plt 
x= [1,2,3,4]
y = [12,34,56,67]

# create plot 
plt.plot(x,y , color = "blue" , marker   = "o")
plt.title("Simple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.savefig(r"C:\Users\Zeeshan Ali\Desktop\AI-and-Machine-Learning\2. Data Sciences\Python Libraries\3. Matplotlib\3. Saving Figures\line_plot.png", dpi=300, bbox_inches="tight")
plt.show()
