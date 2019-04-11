import random
import profiles

# The following code generates a rough profile of a potential buyer

# A User profile :
# Category percentage of all cost 
# 

# new User, AutoCreateProfile(), printProfile() 

### Some func for random 
def getInt(a, b):
    return random.randint(a, b)

def getBool():
    if(random.randint(0,1)):
        return True
    else:
        return False

def getDate():
    pass

def getTime():
    pass

### Init user profile 

userProfile = {
        "ID": 1,
        "MonthSpend": 0,
        "SpendPercent": {},
        "FavoriteMerchant": [],
        "ActiveTimePeriod": 0
    }

### Randomlize the user profile, this func modify userProfile
def randomProfile(pro):
    ### Random Month Spend
    pro['MonthSpend'] = getInt(profiles.monthRange['min'], profiles.monthRange['max'])
    ### Random percent
    remain = 100
    totalCate = len(profiles.categories)
    cateRemain = totalCate
    while cateRemain > 0:
        pickCate = getInt(0, totalCate-1) # careful index
        c = profiles.categories[pickCate]
        if c not in pro['SpendPercent']:
            perc = getInt(0, remain) 
            pro['SpendPercent'][c] = perc
            remain -= perc
            cateRemain -= 1
    pro['SpendPercent']['Transportation'] += remain # not so careful because in most case there are no remain

#randomProfile(userProfile)
#print(userProfile['SpendPercent'])

