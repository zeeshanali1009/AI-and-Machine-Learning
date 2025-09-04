# plot.pie() function is used to plot the pie graph
# plt.pie(values, labels  = label_list ,colors  = color_list, autopct  = "%1.1%%")    
# "%1.1%%"   means % means the format specifier 1.1 means digit before and after the decimal 
# and %% means the value will be displayed with the percentage sign

import matplotlib.pyplot as plt
cities  = ["Punjab","Sindh","Balochistan","Khyber Pakhtun Khawan","Gilgit Baltistan"]
sales  = [100,2000,3000,1222,5634]

plt.pie(sales, labels = cities, autopct  = "%1.1f%%" ,colors = ["orange", "gold", "skyblue", "lightgreen", "coral"])
plt.show()