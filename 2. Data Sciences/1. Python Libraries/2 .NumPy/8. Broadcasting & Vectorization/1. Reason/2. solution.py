import numpy as np

prices = np.array([100, 200, 300])  # fixed here
discount = 10

finalprices = prices - (prices * discount / 100)
print(finalprices)

# Broadcasting is used for the heavy calculations as these calculations are very heavy to perform
# It saves us from heavy looped programming calculations without using the loops 
