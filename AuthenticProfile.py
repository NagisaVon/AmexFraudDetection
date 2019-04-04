import random


# The following code generates a rough profile of a potential buyer
# Future versions will have a way to find the highest and lowest purchases

profile = 0
numOfPurchases = int(input("size of profile"))
authLow = int(input("low end of purchases"))
authHigh = int(input("high end of purchases"))

for x in range (numOfPurchases):
    purchase = (random.randint(authLow,authHigh)/10)
    print (purchase)
    profile = (profile + purchase)
profile = (profile/numOfPurchases)
print (profile)

print ("")

# This is the code for the threshold

def ThresholdCheck():
    #if thresh is 5 or greater there will never be theft because the range
    #of the threshold will be larger than the price range
    thresh = 3
    signalChance = 30
    #If a purchase is outside of the threshold
    if (profile - abs(profile - newPurchase) < profile - thresh):
        #and the signal chance goes off
        if random.randint(1,100) <= signalChance:
            print ("theft")
            print()
            return 0;
    
##########

for x in range (10):
    newPurchase = (random.randint(1,100)/10)
    print (newPurchase)
    ThresholdCheck()
    

