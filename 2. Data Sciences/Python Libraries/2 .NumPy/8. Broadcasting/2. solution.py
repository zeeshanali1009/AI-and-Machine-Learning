import numpy as np

prices = np.array([100, 200, 300])  # fixed here
discount = 10

finalprices = prices - (prices * discount / 100)
print(finalprices)
