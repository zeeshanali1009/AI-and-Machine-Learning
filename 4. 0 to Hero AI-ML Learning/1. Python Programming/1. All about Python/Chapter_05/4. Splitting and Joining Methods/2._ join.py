# it will be joining up the text by some particular character
text = "a,b,c"
splitted = text.split(",")
print(f'After the splitting of the text :{splitted}')

joined = ",".join(splitted)
print(f"The text after joining into: {joined}")