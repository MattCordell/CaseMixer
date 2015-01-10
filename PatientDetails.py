__author__ = 'Doug'
import math
import random
import sqlite3
import uuid
import datetime

youthRisk = 0.27
youthPeak = 21
agedRisk = 0.3
agedPeak = 65


#modify the generic risk rate relative to age
def ageRelatedRisk(age,riskFactor,peakRiskAge):
    #for ages greater than the peak risk, start tapering off - and somewhat random rate.
    if age > peakRiskAge:
        age = (age + (peakRiskAge - age)*math.sqrt(math.sqrt(age)))*(random.randint(6, 9)/10)
    risk = (age/(peakRiskAge+3))/2+riskFactor
    return risk

#get a random age for a patient. Based on ABS stats from 2013
def get_ageGroup():
    db = sqlite3.connect('CaseMixer.db')
    cursor = db.cursor()
    a = random.random()

    q = '''select AgeGroup from AgeDistribution
            where proportion >= ?
            order by proportion asc
            limit 1'''

    cursor.execute(q,(a,))
    return cursor.fetchone()[0]

#get a patient age.
#age group is based on ABS stats. Within the group, ages are divided evenly.
def get_age(group):

    if group == 'Neonate':
        x = random.randint(0, 3)
        return x/12/4
    if group == "Infant":
        x = random.randint(1, 23)
        return x/24
    if group == "2-4":
        return random.randint(2, 4)
    elif group == '5-9':
        return random.randint(5, 9)
    elif group == '10-14':
        return random.randint(10, 14)
    elif group == '15-19':
        return random.randint(15, 19)
    elif group == '20-24':
        return random.randint(20, 24)
    elif group == '25-29':
        return random.randint(25, 29)
    elif group == '30-34':
        return random.randint(30, 34)
    elif group == '35-39':
        return random.randint(35, 39)
    elif group == '40-44':
        return random.randint(40, 44)
    elif group == '45-49':
        return random.randint(45, 49)
    elif group == '50-54':
        return random.randint(50, 54)
    elif group == '55-59':
        return random.randint(55, 59)
    elif group == '60-64':
        return random.randint(60, 64)
    elif group == '65-69':
        return random.randint(65, 69)
    elif group == '70-74':
        return random.randint(70, 74)
    elif group == '75-79':
        return random.randint(75, 79)
    elif group == '80-84':
        return random.randint(80, 84)
    elif group == '85+':
        return random.randint(85, 105)

#determine the sex of a patient at a given range.
def get_sex(ageGroup):
    db = sqlite3.connect('CaseMixer.db')
    cursor = db.cursor()

    a = random.random()

    q = '''select proportion from ProportionOfMalesForAge
           where AgeGroup = ?'''

    cursor.execute(q,(ageGroup,))
    maleRateForAge = cursor.fetchone()[0]
    if a < maleRateForAge:
        return 'M'
    else: return 'F'

def get_episodeDate():
    lastYear = datetime.now-1
    epochYear = lastYear-100
    print('start',epochYear)
    print('end',lastYear)


for x in range(0, 5):
    ageGroup = get_ageGroup()
    age = get_age(ageGroup)
    sex = get_sex(ageGroup)
    get_episodeDate()

    print(uuid.uuid4(),sex,age)


