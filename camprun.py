import random as rand
import time
#candA = ["R",24,12,30,7,12,25]
candA = ["Republican Rudy",(36,0),(36,0),(36,0),(36,0),(36,0),(36,0)]
candB = ["Democrat Dana",(36,0),(36,0),(36,0),(36,0),(36,0),(36,0)]

st=[('Nevada',17,23,20,18,30,14),('Iowa',17,23,20,18,30,14),\
    ('California',17,23,20,18,30,14),('Delaware',17,23,20,18,30,14),\
    ('Georgia',17,23,20,18,30,14),('Florida',17,23,20,18,30,14),\
    ('Texas',17,23,20,18,30,14),('Hawaii',17,23,20,18,30,14),\
    ('Illinois',17,23,20,18,30,14),('Kentucky',17,23,20,18,30,14)]

def determineRoll(state,candidate):
    outVal = 0
    resultVal = [(state[0],candidate[0])]
    for attrScore in range(1,len(state)):
        outVal = state[attrScore] - candidate[attrScore][0]
        if outVal< 0:
            outVal = outVal * -1
        resultVal.append(rand.randint(0,outVal + candidate[attrScore][1]))

    #print resultVal

    return resultVal

def determineWinner(candAresults,candBresults):
    candAname = candAresults[0][1]
    candBname = candBresults[0][1]
    aState = candAresults[0][0]
    bState = candBresults[0][0]
    
    compareCandidates = zip(candAresults,candBresults)

    aScore = 0
    bScore = 0
    winner = ""

    for each in compareCandidates[1:]:
        if each[0] == each[1]:
            aScore += 1
            bScore += 1
        elif each[0] > each[1]:
            aScore += 1
        else:
            bScore +=1
            
    #print "R:" + str(aScore)
    #print "D:" + str(bScore)
    #print "\n"

    if aScore > bScore:
        winner = candAname
    elif aScore < bScore:
        winner = candBname
    else:
        winner = "Independent Ida"

    #print "Candidate " + candAname + " recieved " + str(aScore) + " for the state of " + aState
    #print "Candidate " + candBname + " recieved " + str(bScore) + " for the state of " + bState

    #print winner + " takes the state of " + aState
    return winner + " takes the state of " + aState


for year in range(1960,2020,4):
    ballot = []
    for each in range (0,10):
        ballot.append(determineWinner(determineRoll(st[each],candA),determineRoll(st[each],candB)))

    totals = [0,0,0]
    #print ballot

    for each in ballot:
        if each[0] == "R":
            totals[0]+= 1
        if each[0] == "D":
            totals[1]+= 1
        if each[0] == "I":
            totals[2] += 1

    #print totals
    #print totals.index(max(totals))
    winnerScore = -1
    president = ""
    for idx, value in enumerate(totals):
       #print str(value) + " vs. " + str(winnerScore)
       if value > winnerScore:
           winnerScore = value
           president = idx

    candidateDict = {0:"Republican Rudy",1:"Democrat Dana",2:"Independent Ida"}
    print candidateDict[president] + " IS THE NEW PRESIDENT OF "+str(year) + "!\n"
    time.sleep(2)


##for i in range (1,5):
##    print "P=[" + str(st[i][i] - candA[i]) + " (" + str(st[i][i]) + ") " + str(st[i][i]-candB[i]) + "]"
