# now we will be using the new oop concept for the beter programming to tackle the code redundancy 
class Team:
    def __init__(self,team, titles, year):
        self.team = team
        self.titles = titles
        self.year = year 
    
    def team_records(self):
        print(f"Team {self.team} has won the {self.titles} in the {self.year}")
    
# now we will be creating the objects 

team01 = Team("Peshawar Zalmi", 1, 2017)
team02 = Team("Quetta Gladiotors" , 1, 2016)

team01.team_records()
team02.team_records()