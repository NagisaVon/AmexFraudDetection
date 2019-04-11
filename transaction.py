import profiles
import randomProfile
import time
import random
import csv 

profile = randomProfile.userProfile

randomProfile.randomProfile(profile)

print(profile)

def getFloat(a, b):
    return round(random.uniform(a, b), 2)

# Transaction
# UserID Date Time Category (Merchant) isOnline Amount

def randomCatagory(profile):
    rInt = randomProfile.getInt(0, 100);
    prev = 0
    for i in range(0, len(profiles.categories)):
        if rInt >= prev and rInt < prev + profile['SpendPercent'][profiles.categories[i]]:
            return profiles.categories[i]
        prev += profile['SpendPercent'][profiles.categories[i]]
    return profiles.categories[len(profiles.categories)-1] # return last one category if no return 


def randomTransaction(profile, tID):
    transaction = {}
    transaction['UserID'] = profile['ID']
    transaction['tID'] = tID
    strtime = time.strftime("%b %d %H:%M", time.localtime()) 
    transaction['Time'] = strtime
    c = randomCatagory(profile)
    transaction['Category'] = c
    transaction['isOnline'] = randomProfile.getBool()
    transaction['Amount'] = getFloat(profiles.categoryProfiles[c]['min'], profiles.categoryProfiles[c]['max'])
    return transaction

### Start generate transactions and write csv file

with open('user1.csv', mode='w') as csv_file:
    fieldnames = ['UserID', 'tID', 'Time', 'Category', 'isOnline', 'Amount']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    moneyLeft = profile['MonthSpend']
    tID = 0
    while moneyLeft > 0: # dont have to spend all 
        tID += 1
        newTransaction = randomTransaction(profile, tID)
        print(newTransaction)
        writer.writerow(newTransaction)
        moneyLeft -= newTransaction['Amount']
    

