# subplot() basically divides the the figure into rows and columns
# plt.subplot(nrows, ncols, index)
# fig, ax  = plt.subplots(nrows, ncols , figsize  = (width , height))
import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [12, 34, 45, 62, 34]

# Subplots: 1 row, 2 columns
fig, ax = plt.subplots(1, 2, figsize=(10, 5))

# First subplot: Line Plot
ax[0].plot(x, y, color = "green")
ax[0].set_title("Line Plot")

# Second subplot: Bar Chart
ax[1].bar(x, y, color = "blue")
ax[1].set_title("Bar Chart")

fig.suptitle("Comparison of Line and Bar charts")
# Adjusting the layout before showing the plots
plt.tight_layout()
plt.show()
