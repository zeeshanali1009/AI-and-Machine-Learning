# plot.hist() function is used to plot the histogram (distribution of the continuous data into the various ranges)
# plt.hist(data,bins = number of bins  ,colors  = colorname, edgecolor  = colorname)    

import matplotlib.pyplot as plt
scores  = [100,12,34,56,56,34,56,45,45,46,67,67,78,45,74,67,45,57,45,67,3,47]

plt.hist(scores,bins=5,color="blue", edgecolor  ="orange")
plt.show()