import random as ran
import time

class Player():
    def __init__(self, name, placement):
        self.name = name
        self.placement = placement
        self.actionCases =[[2,31],[5,35],[47,48],[50,72],[59,77],[83,86],[24,11],[37,19],[65,54],[71,41],[90,73],[99,79]]
        
    def RollDice(self):
        dice1 = ran.randint(1,6)
        dice2 = ran.randint(1,6)

        return [dice1,dice2]

    def takeTurn(self):
        roll_total = 0

        for each in self.RollDice():
            roll_total += each

        print self.name + " rolled a " + str(roll_total)
        self.placement += roll_total
        time.sleep(1)
            
        for each in self.actionCases:
            if self.placement > 100:
                self.placement -= roll_total
                print self.name + " needs a perfect 100!"
                
            if each[0] == self.placement:
                self.placement = each[1]
                if each[0] > each[1]:
                    print "Oh No! " + self.name + " found a Snake! ("+str(each[0]) + "->"+str(each[1]) +")"
                if each[0] < each[1]:
                    print "Yay! Player " + self.name +" foud a Ladder! ("+str(each[0]) + "->"+str(each[1]) +")"
                    
        print self.name + " landed on " + str(self.placement) + "\n"

    def delcareWin(self):
        print self.name + " wins!"


def addPlayers():
    players = []
    
    default_player = 0
    addMore =  True
    while addMore == True:
        add_player = raw_input("Let's add players! Submit a name of a player: ") or "PLAYER"+str(default_player)
        players.append(Player(add_player,0))

        default_player += 1

        addMorePrompt = raw_input("Add More? [Y]: ") or "y"
        if addMorePrompt.upper() == "Y":
            addMore = True
        else:
            addMore = False

    return players


GamePlayers = addPlayers()
gameOverFlag = False
while gameOverFlag == False:
    for eachPlayer in GamePlayers:
        if eachPlayer.placement == 100:
            eachPlayer.delcareWin()
            gameOverFlag = True
            break
        else:
            eachPlayer.takeTurn()
