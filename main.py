import random
deck=[]
playerDeck=[]
player1Deck=[]
player2Deck=[]
WarArray1=[]
WarArray2=[]
firstTime=True
bust=0
numTimes=0
sum2=0
countCards=0
CardCountArray=[]
newCardValues=[]
dealerDeck=[]
numWins=0
lost=False
sum3=0
hitWins=0
standWins=0
rounds=0
done=False
OverAllRound=[]
stands=0
hits=0
def generateDeck():
    for i in range(4):
        for x in range(10):
            deck.append(x+1)
        for x in range(3):
            deck.append(10)
def shuffleDeck():
    for i in range(1000):
        num1= random.randint(0,len(deck)-1)
        num2=random.randint(0,len(deck)-1)
        temp=deck[num1]
        deck[num1]=deck[num2]
        deck[num2]=temp
def Scenario1():
    global firstTime, bust, numTimes
    if firstTime==True:
        numCards=int(input("How many cards do you want:"))
        for i in range(numCards):
            card=int(input("Choose a card value from 1-10:"))
            playerDeck.append(card)
            deck.remove(card)
        firstTime=False
    newCard=random.randint(0,len(deck)-1)
    newCardValue=deck[newCard]
    playerDeck.append(newCardValue)
    deck.remove(newCardValue)
    print(playerDeck)
    sum=0
    for i in range(len(playerDeck)):
        sum+=playerDeck[i]
    if sum>21:
        bust+=1
    numTimes+=1
    deck.append(newCardValue)
    playerDeck.remove(newCardValue)
def Scenario2():
    global sum2, countCards, CardCountArray
    countCards=0
    done=False
    while not done:
        sum2 = 0
        newCard = random.randint(0, len(deck) - 1)
        newCardValues.append(deck[newCard])
        playerDeck.append(deck[newCard])
        deck.remove(deck[newCard])
        for i in range(len(playerDeck)):
            sum2 += playerDeck[i]
        countCards += 1
        if sum2 > 21:
            done = True
    print(playerDeck)
    for x in range(len(newCardValues)):
        deck.append(newCardValues[x])
    CardCountArray.append(countCards)
def Scenario3():
    global firstTime, done, sum2, numWins,lost, sum3
    if firstTime == True:
        numCards = int(input("How many cards do you want:"))
        for i in range(numCards):
            card = int(input("Choose a card value from 1-10:"))
            playerDeck.append(card)
            deck.remove(card)
        firstTime=False
    done=False
    newCardValues=[]
    dealerDeck=[]
    lost=False
    sum3=0
    while not done:
        sum2 = 0
        newCard = random.randint(0, len(deck) - 1)
        newCardValues.append(deck[newCard])
        dealerDeck.append(deck[newCard])
        deck.remove(deck[newCard])
        for i in range(len(dealerDeck)):
            sum2 += dealerDeck[i]
        if sum2 > 17 and sum2 <= 21:
            done = True
        elif sum2 > 21:
            lost=True
            numWins+=1
            done=True

    print(dealerDeck)
    for i in range(len(playerDeck)):
        sum3 += playerDeck[i]
    if sum3>sum2 and lost==False:
        numWins+=1
    for x in range(len(newCardValues)):
        deck.append(newCardValues[x])
def Scenario4():
    global firstTime, done, sum2, numWins, lost, sum3
    if firstTime == True:
        numCards = int(input("How many cards do you want:"))
        for i in range(numCards):
            card = int(input("Choose a card value from 1-11:"))
            if card!=11:
                playerDeck.append(card)
                deck.remove(card)
            else:
                playerDeck.append(11)
                deck.remove(1)
        firstTime = False
    done = False
    newCardValues = []
    dealerDeck = []
    lost = False
    sum3 = 0
    # to add choice 1 or 11 i need to check if 11 makes it pop and if it doesnt then i use 11 instead of 1
    while not done:
        sum2 = 0
        newCard = random.randint(0, len(deck) - 1)
        newCardValues.append(deck[newCard])
        checkSum = 0
        checkDeck = []
        if deck[newCard]==1:
            for x in range(len(dealerDeck)):
                checkDeck.append(dealerDeck[x])
            checkDeck.append(11)
            for i in range(len(checkDeck)):
                checkSum += checkDeck[i]
            if checkSum>21:
                dealerDeck.append(1)
            else:
                dealerDeck.append(11)
        else:
            dealerDeck.append(deck[newCard])
        deck.remove(deck[newCard])
        for i in range(len(dealerDeck)):
            sum2 += dealerDeck[i]
        if sum2 > 17 and sum2 <= 21:
            done = True
        elif sum2 > 21:
            lost = True
            numWins += 1
            done = True

    print(dealerDeck)
    for i in range(len(playerDeck)):
        sum3 += playerDeck[i]
    if sum3 > sum2 and lost == False:
        numWins += 1
    for x in range(len(newCardValues)):
        deck.append(newCardValues[x])
def Scenario5():
    global hitWins,standWins, hits, stands
    print("1) Simulation 1: Computer shown card = 10, player cards = 10, 6")
    print("2) Simulation 2: Computer shown card = 6, player cards = 10, 10")
    print("3) Simulation 3: Computer shown card = 8, player cards = A, A")
    hitWins=0
    standWins=0
    stands=0
    hits=0
    playerDeck=[]
    dealerDeck=[]
    choose= int(input("Choose the simulation:"))
    if choose==1:
        for i in range(1000):
            simulation(10,10,6)
    elif choose==2:
        for i in range(1000):
            simulation(6, 10, 10)
    elif choose==3:
        for i in range(1000):
            simulation(8,1,1)
def simulation(x,y,z):
    global hitWins, standWins, hits, stands
    playerBust=False
    dealerDeck=[x]
    deck.remove(x)
    playerDeck=[y,z]
    deck.remove(y)
    deck.remove(z)
    hitOrStand=random.randint(0,1)
    hit=False
    if hitOrStand==0:
        hit=True
        hits+=1
        hitCard=random.randint(0,len(deck) - 1)
        cardValue=deck[hitCard]
        playerDeck.append(deck[hitCard])
        deck.remove(deck[hitCard])
    elif hitOrStand==1:
        stands+=1
    for b in range(len(playerDeck)):
        if playerDeck[b]==1:
            checkSum = 0
            for i in range(len(playerDeck)):
                checkSum+=playerDeck[i]
            if checkSum<11:
                playerDeck[b]=11
    done=False
    checkSum=0
    for i in range(len(playerDeck)):
        checkSum+=playerDeck[i]
    if checkSum>21:
        playerBust=True
    newCardValues=[]
    while not done:
        newCard = random.randint(0, len(deck) - 1)
        newCardValues.append(deck[newCard])
        checkSum = 0
        sum2=0
        if deck[newCard] == 1:
            for i in range(len(dealerDeck)):
                checkSum += dealerDeck[i]
            if checkSum < 11:
                dealerDeck.append(11)
            else:
                dealerDeck.append(1)
        else:
            dealerDeck.append(deck[newCard])
        deck.remove(deck[newCard])
        for i in range(len(dealerDeck)):
            sum2 += dealerDeck[i]
        if sum2 > 17 and sum2 <= 21:
            done = True
        elif sum2 > 21:
            done = True
            if hit==True and playerBust==False:
                hitWins+=1
            elif hit==False and playerBust==False:
                standWins+=1
    playerSum=0
    for b in range(len(playerDeck)):
        playerSum+=playerDeck[b]
    if playerSum>sum2 and playerSum<22 and sum2<22 and hit==True:
        hitWins+=1
    if playerSum > sum2 and playerSum < 22 and sum2 < 22 and hit == False:
        standWins+=1
    deck.append(y)
    deck.append(z)
    deck.append(x)
    if hit==True:
        deck.append(cardValue)
    for x in range(len(newCardValues)):
        deck.append(newCardValues[x])
def Scenario6():
    global rounds,WarArray1,WarArray2, player1Deck, player2Deck
    deck=[]
    player2Deck=[]
    player1Deck=[]
    WarArray1=[]
    WarArray2=[]
    rounds=0
    for i in range(4):
        for x in range(13):
            deck.append(x+2)
    for i in range(1000):
        num1= random.randint(0,len(deck)-1)
        num2=random.randint(0,len(deck)-1)
        temp=deck[num1]
        deck[num1]=deck[num2]
        deck[num2]=temp
    while not len(deck)==0:
        player1Deck.append(deck[0])
        deck.remove(deck[0])
        player2Deck.append(deck[0])
        deck.remove(deck[0])
    WarFight()
def WarFight():
    global WarArray1, WarArray2, rounds, player1Deck, player2Deck
    count=30
    while len(player1Deck)>0 and len(player2Deck)>0:
        count-=1

        if count<1:
            for i in range(1000):
                num1 = random.randint(0, len(player1Deck) - 1)
                num2 = random.randint(0, len(player1Deck) - 1)
                temp = player1Deck[num1]
                player1Deck[num1] = player1Deck[num2]
                player1Deck[num2] = temp
            for i in range(1000):
                num1 = random.randint(0, len(player1Deck) - 1)
                num2 = random.randint(0, len(player1Deck) - 1)
                temp = player1Deck[num1]
                player1Deck[num1] = player1Deck[num2]
                player1Deck[num2] = temp
            count=30

        if len(player1Deck)>0 and len(player2Deck)>0:
            WarArray1.append(player1Deck[0])
            player1Deck.pop(0)
            WarArray2.append(player2Deck[0])
            player2Deck.pop(0)
        if WarArray1[len(WarArray1)-1] == WarArray2[len(WarArray2)-1] and len(player1Deck)>0 and len(player2Deck)>0:
            tieWar()

        elif WarArray1[len(WarArray1)-1] > WarArray2[len(WarArray2)-1] and len(player1Deck)>0 and len(player2Deck)>0:
            for x in range(len(WarArray1)):
                player1Deck.append(WarArray1[x])
            for x in range(len(WarArray2)):
                player1Deck.append(WarArray2[x])
            WarArray1 = []
            WarArray2 = []
        elif WarArray1[len(WarArray1)-1] < WarArray2[len(WarArray2)-1] and len(player1Deck)>0 and len(player2Deck)>0:
            for x in range(len(WarArray1)):
                player2Deck.append(WarArray1[x])
            for x in range(len(WarArray2)):
                player2Deck.append(WarArray2[x])
            WarArray1 = []
            WarArray2 = []
        rounds+=1
    OverAllRound.append(rounds)
def tieWar():
    global WarArray1, WarArray2, rounds, player1Deck, player2Deck
    for i in range(2):
        if len(player1Deck)>0 and len(player2Deck)>0:
            WarArray1.append(player1Deck[0])
            player1Deck.pop(0)
            WarArray2.append(player2Deck[0])
            player2Deck.pop(0)
    if WarArray1[len(WarArray1) - 1] == WarArray2[len(WarArray2) - 1] and len(player1Deck)>0 and len(player2Deck)>0:
        tieWar()
    elif WarArray1[len(WarArray1) - 1] > WarArray2[len(WarArray2) - 1] and len(player1Deck)>0 and len(player2Deck)>0:
        for x in range(len(WarArray1)):
            player1Deck.append(WarArray1[x])
        for x in range(len(WarArray2)):
            player1Deck.append(WarArray2[x])
        WarArray1 = []
        WarArray2 = []
    elif WarArray1[len(WarArray1) - 1] < WarArray2[len(WarArray2) - 1] and len(player1Deck)>0 and len(player2Deck)>0:
        for x in range(len(WarArray1)):
            player2Deck.append(WarArray1[x])
        for x in range(len(WarArray2)):
            player2Deck.append(WarArray2[x])
        WarArray1 = []
        WarArray2 = []

def main():
    global playerDeck,bust,numTimes, firstTime, deck, countCards, CardCountArray, dealerDeck, numWins, standWins, stands, hitWins, hits
    playerDeck = []
    deck=[]
    dealerDeck=[]
    generateDeck()
    shuffleDeck()
    print("Pick the scenario to run:")
    print("1: Given a current hand consisting of 1 or more cards, what is the probablility you will bust on your next card?")
    print("2: Given that you will draw cards until you bust, what is the average number of cards that you can draw?")
    print("3: Given a current hand consisting of 2 or more cards that add to total of 21 or less, what is the probability that you win?")
    print("4: Scenario 3 but aces can equal 1 or 11 (whichever fits better)")
    print("5: Given that the computer has 1 card shown and 1 card face down, and I have 2 cards in my hand, should I hit or stand to give me the best odds of winning?")
    print("6: How many rounds have to be played on average to win a game of War between 2 players?")
    chooseScenario=int(input())
    if chooseScenario==1:
        for i in range(1000):
            Scenario1()
        print("Number Busts:", bust)
        print("Number of Times not Bust:", numTimes - bust)
        print("Probability of busting:",bust/numTimes*100,"%")
        print("Probability of not busting:", (numTimes - bust) / numTimes*100,"%")
        bust=0
        numTimes=0
        firstTime=True
        main()
    elif chooseScenario==2:
        countCards=0
        CardCountArray=[]
        for i in range(1000):
            playerDeck = []
            Scenario2()
        average=0
        for x in range(len(CardCountArray)):
            average += CardCountArray[x]
        average /= len(CardCountArray)
        print("The average number of roles before bust is:", average)
        main()
    elif chooseScenario==3:
        numWins=0
        firstTime=True
        for i in range(1000):
            Scenario3()
            dealerDeck = []
        print("You won", numWins, "times")
        print("The probability of you winning with that deck is:",numWins/10,"%")
        main()
    elif chooseScenario==4:
        numWins = 0
        firstTime = True
        for i in range(1000):
            Scenario4()
            dealerDeck = []
        print("You won", numWins, "times")
        print("The probability of you winning with that deck is:", numWins / 10, "%")
        main()
    elif chooseScenario==5:
        Scenario5()
        print("The probability to win if you stand is:", standWins/stands*100,"%")
        print("The probability to win if you hit is:", hitWins / hits * 100, "%")
        main()
    elif chooseScenario==6:
        for i in range(100):
            Scenario6()
        average2=0
        for x in range(len(OverAllRound)):
            average2 += OverAllRound[x]
        average2 /= len(OverAllRound)
        print("The average number of rounds in war is:", average2)
        main()
main()