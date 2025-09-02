# In the previous approach programmers use to follow the same pattern

Team = "Peshawar Zalmi"
Titles = 1 
Year_won = 2017

def Peshawar_Zalmi_record():
    print(f"Team {Team} has won {Titles} in {Year_won}")

Team = "Quetta Gladiotors"
Titles = 1 
Year_won = 2016

def Quetta_Gladiotors_record():
    print(f"Team {Team} has won {Titles} in {Year_won}")

Quetta_Gladiotors_record()
Peshawar_Zalmi_record()

# so here when ever we will have to add one more team in the code there will be too much redundancy writing the 
# same lines code again and again

