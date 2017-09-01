import random as rand
#candA = ["R",24,12,30,7,12,25]
candA = ["Republican Robin",(28,0),(30,1),(30,3),(17,4),(12,2),(34,1)]
candB = ["Democrat Dana",(32,1),(36,2),(36,4),(15,2),(34,1),(12,2)]

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

    if aScore > bScore:
        winner = candAname
    elif aScore < bScore:
        winner = candBname
    else:
        winner = "Independent Ida"

    #print "Candidate " + candAname + " recieved " + str(aScore) + " for the state of " + aState
    #print "Candidate " + candBname + " recieved " + str(bScore) + " for the state of " + bState

    print winner + " takes the state of " + aState

    
for each in range (0,10):
    determineWinner(determineRoll(st[each],candA),determineRoll(st[each],candB))

##for i in range (1,5):
##    print "P=[" + str(st[i][i] - candA[i]) + " (" + str(st[i][i]) + ") " + str(st[i][i]-candB[i]) + "]"
