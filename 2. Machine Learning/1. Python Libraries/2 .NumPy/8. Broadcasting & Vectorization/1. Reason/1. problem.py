prices  = [100,200,300]
discount  = 10
finalprices  = []

for price in prices:
    finalprice = price - (prices * discount/100)
    finalprices.append(finalprice)

print(finalprices)

