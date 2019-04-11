import random

boolRunAgain = 1
# The following code generates a rough profile of a potential buyer
while boolRunAgain == 1:
    profile = 0
    numOfPurchases = int(input("size of profile: "))
    authLow = float(input("low end of purchases(0-50): "))
    authHigh = float(input("high end of purchases(50-100): "))
    #if thresh is 5 or greater there will never be theft because the range
    #of the threshold will be larger than the price range
    thresh = float(input("size of threshold (distance from the profile average where the detection system will trigger): "))

    # signalChance is the % at which a new purchase will be flagged as fraud
    # if it surpasses the threshold of the profile. 
    signalChance = float(input("percent chance that the system will trigger(0-100): "))

    #amount of times a purchase was a theft
    theftCount = 0

    #amount of times a theft was caught
    catchCount = 0
    
    #counter that goes off after repeated false flaggings, which increases the negative payoff
    angryCustomer = 0

    # x,1,1
    flagFraud = 5
    # x,0,1
    flagAuthentic = 0
    # x,1,0
    passFraud = -5
    # x,0,0
    passAuthentic = 0

    fraudIntelligence = input("Does fraudster have profile? Y/N")
    fraudIntelligence = fraudIntelligence[0].upper()

    for x in range (numOfPurchases):
        purchase = (random.randint(authLow,authHigh)/10)
        profile = (profile + purchase)


    # Profile is the average purchase
    profile = (profile/numOfPurchases)
    # profile should contain our all our past data
    # profileAvg should be our average.
    print ("Average purchase of the profile: " + str(profile))
    print ("")



    # This is the code for the threshold
    def ThresholdCheck(newPurchase):
        #If a purchase is outside of the threshold
        # then it has a chance to signal theft.

        # profile is the average, - (profile - newPurchase)
        # newPurchase is the new purchase, we're checking if it's 
        # if the difference between the profileAVG and the new purchase

        # Find the difference between profileAverage and new purchase
        # if this difference is less than the difference btween profileAverage and the set threshold
        # we are alerted and might flag it (randomly right now).
        if (profile - abs(profile - newPurchase[0]) < profile - thresh):

            #and the signal chance goes off
            if random.randint(1,100) <= signalChance:
                systemSaysFraud = 1
                newPurchase.append(systemSaysFraud)
                return newPurchase 
                # I need to be able to refer to his "trigger"
                # purchase being flagged must be able to be checked for payoff purposes.

                # return 0;
            else:
                systemSaysFraud = 0
                newPurchase.append(systemSaysFraud)
                return newPurchase 

        else:
            systemSaysFraud = 0
            newPurchase.append(systemSaysFraud)
            return newPurchase


        
    ##########


    systemPoints = 0
    theftPoints = 0

    for x in range (numOfPurchases):
    # we build our initial purchase and modify only if fraud is true.
        newPurchase = [(random.randint(1,100)/10)]
        #check for fraud and if fraud, pick a strategy.
        # 50/50 chance of fraud
        boolFraud = random.randint(0,1)
        # If it is fraud, then a fraud strategy is picked.
        fraudStrategy = ""
        if boolFraud == 1:
            fraudStrategy = random.randint(0,2)

        if fraudIntelligence != "Y":
            # low purchases
            if fraudStrategy == 0:
                newPurchase = [(random.randint(1,30)/10)]
            # mixed purchases 
            if fraudStrategy == 1:
                newPurchase = [(random.randint(30,70)/10)]

            # high purchases
            if fraudStrategy == 2:
                newPurchase = [(random.randint(70,100)/10)]

        if fraudIntelligence == "Y":
            # low purchases
            if fraudStrategy == 0:
                newPurchase = [(random.randint(0,authLow)/10)]
                
            # mixed purchases 
            if fraudStrategy == 1:
                newPurchase = [(random.randint(authLow,authHigh)/10)]

            # high purchases
            if fraudStrategy == 2:
                newPurchase = [(random.randint(authHigh,100)/10)]

    # We mark it fraud or not at the 1st index.
        newPurchase.append(boolFraud)

        ThresholdCheck(newPurchase)
        # Detect fraud correct (hit)
        # Detect fraud false (miss)
        # Detect authentic correct (hit)
        # Detect authentic false (miss)


        # The payoffs
        FraudDetectionSystemPayOff = 0 
        TheftPayOff = 0

        # index setup
        # 0th = purchase amount
        # 1st = purchase is fraud? bool, 1 = yes or 0 = no
        # 2nd = system flags purhcase? bool, 1 = yes or 0 = no

        if angryCustomer == 15:
            flagAuthentic = flagAuthentic - 1
            angryCustomer = 0

            # After we know it is fraud or not, and if it was caught or not, then we do payoffs
            # if the fraud tag is 1, it's fraud, otherwise it's not.
        if (newPurchase[1] == 1 and newPurchase[2] == 1):
            systemPoints += flagFraud
            theftCount = theftCount + 1
            catchCount = catchCount + 1
        elif (newPurchase[1] == 0 and newPurchase[2] == 1):
            systemPoints += flagAuthentic
            angryCustomer = angryCustomer + 1
        elif (newPurchase[1] == 1 and newPurchase[2] == 0):
            systemPoints += passFraud
            theftCount = theftCount + 1
        elif (newPurchase[1] == 0 and newPurchase[2] == 0):
            systemPoints += passAuthentic

            


    print("Detection System Payoff: " + str(systemPoints))
    print("System Catch Rate: " + str((catchCount/theftCount)*100))

    # print("Theif Payoff: " + str(theftPoints))

    inPlayAgain = input("Run again? Y/N")
    inPlayAgain = inPlayAgain[0].upper()
    if inPlayAgain == "Y":
        boolRunAgain = 1
    else:
        boolRunAgain = 0

