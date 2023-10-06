#Football team goal manager
#Craig Ferguson
#25/11/20

def getData():
    name = input("What is you name ? ")
    team = input("What team do you play for ? ")
    number = input("What is your shirt number ? ")
    goals1 = int(input("How many goals did you score in game 1 ? "))
    goals2 = int(input("How many goals did you score in game 2 ? "))
    goals3 = int(input("How many goals did you score in game 3 ? "))
    return name, team, number, goals1, goals2, goals3

def performCalculation(goals1, goals2, goals3):
    averageGoals = round(((goals1+goals2+goals3)/3.0),0)
    return averageGoals

def displayResults(name, team, number, averageGoals):
    print ("Name: ",name)
    print ("Team: ",team)
    print ("Shirt Number: ",number)
    print ("Average goals: ",averageGoals)

name,team,number,goals1,goals2,goals3 = getData()
averageGoals = performCalculation(goals1,goals2,goals3)
displayResults(name,team,number,averageGoals)

