# there are these important steps being used to have multiple functionalities out there
# 1.... break       (to end the loop immediately )
# 2.... continue       (to skip the current iteration)
# 3.... pass        (used to pass the current logic )

for i in range(1,100,1):
    if (i==10):
        break
    else:
        print(i)


for i in range(1, 100):
    if i % 2 == 0:
        continue
    else:
        print(i)

for i in range(1, 10):
    if i % 2 == 0:
        pass
    else:
        print(i) 
