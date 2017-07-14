import random as ran
import time
from threading import Timer


global gameOn
global totalSales

totalSales = float(0.00)
gameOn = True

def timeout():
    global gameOn
    global totalSales
    
    print "\n\n\nShift's over Pizza Punk!"
    print "You made a grand total of: $" + str(totalSales)
    
    quit()
    
def randomPizza(level=3):
    toppingsOnPizza = []
    
    toppingNum = ran.randint(1,level)
    
    for topping in range(0,toppingNum):
        newTopping = ran.randint(0,toppingNum)
        
        if newTopping not in toppingsOnPizza:
            toppingsOnPizza.append(newTopping)
    
    if len(toppingsOnPizza) == 0:
        toppingsOnPizza.append(0)
    
    return sorted(toppingsOnPizza)

def makePizza(strGuess):
    ListDistinct = []

    for each in strGuess:
        try:
            if int(each) not in ListDistinct:
                ListDistinct.append(int(each))
        except:
            ListDistinct.append(1)
            
    return sorted(ListDistinct)
    
def pizzaCheck():
    
    gameAnswer = randomPizza(6)
    print "\nNEW ORDER!"
    orderComplete = False
    pizzaPrice = float(len(gameAnswer) * 5.00)
    global totalSales
    
    while orderComplete == False:
        presentOrder = raw_input("\nMake me a pizza, Punk!: " ) or "0"
        userGuess = makePizza(presentOrder)
            
        if gameAnswer == userGuess:
            print "THAT'S IT! THAT'S MY PIZZA!"
            orderComplete = True
            print  "$" +str(pizzaPrice) + " sale."
            totalSales += pizzaPrice
            
        else:
            if len(gameAnswer) > len(userGuess):
                print "\nI came in hungry! Now you want me starving!"
            elif len(gameAnswer) < len(userGuess):
                print "\nAre you trying to give me a heart attack?!"
            
        orderScore = float(len(set(gameAnswer) & set(userGuess)))/float(len(gameAnswer))

        if orderScore == 0:
            print "There's nothing I like about that pizza."
        else:
            if orderScore >= 0.1 and orderScore <=0.39:
                print "Needs more flavor."
            if orderScore >= 0.4 and orderScore <=0.79:
                print "Nearly halfway there but still lacking."
            if orderScore >= 0.8 and orderScore <> 1.0:
                print "Amazing but not perfect! Try again."
                
        pizzaPrice -= 0.25
                
        #print "Your answer: " + str(userGuess) + " vs. the answer " + str(gameAnswer) + "\n"

t = Timer(240 * 60, timeout)
t.start()

try:
    while gameOn == True:
        pizzaCheck()
except:
    print "\r\r\nThanks for Playing!"
    
