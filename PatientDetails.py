__author__ = 'Doug'
import math
import random
import sqlite3
import uuid
import datetime
import time

#risk determines likelihood of an age specific disorder.
#peak is used to alter risk by age... kinda
neonateRisk = 0.85
#No infantRisk
childRisk = 0.5
youthRisk = 0.27
youthPeak = 21
middleAgedRisk = 0.6
agedRisk = 0.34
agedPeak = 83
MostRecentEpisodeDate = datetime.datetime.now() #current date

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
        return round(x/12/4,2)
    if group == "Infant":
        x = random.randint(1, 23)
        return round(x/24,2)
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

#generate a random date between MostRecentEpisodeDate and 100years prior.
#provides a random date for the episode. Which may/maynot be useful
def get_episodeDate():
    epochYear = MostRecentEpisodeDate.year-100
    epochDate = datetime.date(epochYear,MostRecentEpisodeDate.month,MostRecentEpisodeDate.day)

    randomDate = ptime = epochDate + random.random() * (MostRecentEpisodeDate.date() - epochDate)

    return randomDate

def get_Problem(age,sex):
    notSex = 'X'
    if sex == 'M':
        notSex = 'Females%'
    else:
        notSex = 'Males%'

    db = sqlite3.connect('CaseMixer.db')
    cursor = db.cursor()

    EpisodeRiskValue = random.random()


    #determine age level. First attempt an AgeRisk, else set NotFilter variable for default query.
    if age < 1/12:
        if EpisodeRiskValue < neonateRisk:
            q = '''select disorderSCTID from DisorderFilters
            where disorderSCTID not in (select disorderSCTID from DisorderFilters where filter like ?)
            and filter like 'Neonates%'
            order by RANDOM() LIMIT 1;'''
            cursor.execute(q,(notSex,))
            return cursor.fetchone()[0]
        NotFilter = 'NotNeonateProblems'
    elif age < 2:
        NotFilter = 'NotInfantProblems'
    elif age < 11:
        if EpisodeRiskValue < childRisk:
            q = '''select disorderSCTID from DisorderFilters
            where disorderSCTID not in (select disorderSCTID from DisorderFilters where filter like ?)
            and filter like 'Children%'
            order by RANDOM() LIMIT 1;'''
            cursor.execute(q,(notSex,))
            return cursor.fetchone()[0]
        NotFilter = 'NotChildrenProblems'
    elif age < 24:
        if EpisodeRiskValue < ageRelatedRisk(age,youthRisk,youthPeak):
            q = '''select disorderSCTID from DisorderFilters
            where disorderSCTID not in (select disorderSCTID from DisorderFilters where filter like ?)
            and filter like 'YouthRisks%'
            order by RANDOM() LIMIT 1;'''
            cursor.execute(q,(notSex,))
            return cursor.fetchone()[0]
        NotFilter = 'NotYouthProblems'
    elif age < 65:
        if EpisodeRiskValue < middleAgedRisk:
            q = '''select disorderSCTID from DisorderFilters
            where disorderSCTID not in (select disorderSCTID from DisorderFilters where filter like ?)
            and filter like 'MiddleAgedAdults%'
            order by RANDOM() LIMIT 1;'''
            cursor.execute(q,(notSex,))
            return cursor.fetchone()[0]
        NotFilter = 'NotMiddleAgedProblems'
    else:
        if EpisodeRiskValue < ageRelatedRisk(age,agedRisk,agedPeak):
            q = '''select disorderSCTID from DisorderFilters
            where disorderSCTID not in (select disorderSCTID from DisorderFilters where filter like ?)
            and filter like 'Seniors%'
            order by RANDOM() LIMIT 1;'''
            cursor.execute(q,(notSex,))
            return cursor.fetchone()[0]
        NotFilter = 'NotSeniorsProblems'

    q = '''select rowid from CandidateProblemList
        where disorderSCTID not in (select * from '''+ NotFilter + ''')
        and disorderSCTID not in (select disorderSCTID from DisorderFilters where filter like ?)
        and rowid >= (abs(random()) % (SELECT max(rowid) FROM CandidateProblemList))
        LIMIT 1; '''

    cursor.execute(q,(notSex,))
    return cursor.fetchone()[0]


print('start')
s = datetime.datetime.now()
f = open('TestDataSet.txt', 'a')

    #look at some sort of progress bar
    #print("Writing " + str(x+1) +"/"+str(5))

for x in range(0, 10):
    ageGroup = get_ageGroup()
    age = get_age(ageGroup)
    sex = get_sex(ageGroup)
    problem = get_Problem(age,sex)
    episodeDate = get_episodeDate()

    x = episodeDate.strftime('%Y-%m-%d')+'\t'+sex+'\t'+str(age)+'\t'+str(problem)+'\n'
    f.writelines(x)
    #print(x)


f.close()
    #an episode with a UUID. Not used by default for case consideration.
    #print(uuid.uuid4(),sex,age,problem,episodeDate)

f = datetime.datetime.now()

timeTaken = f-s
print(timeTaken)
print('finish')

#initial run 7.5 seconds for 100 records. 250k in about 6 hours.
#1h7m n= 40000
#100 run baseline
#a=9.743,10.535,10.929  w=10.468,10.383,10.612805
#just calculating. No writing
#10.53,10.75,10.533
#just writing
#0.096,0.1360.106
#1000 run, just writing 0.174
#10,000 = 0.87
#50,000 = 3.58
#100,000 = 6.625
#1,000,000 = 1m14s
#100,000 1Mb buff 6.9s
#100k 15Mb buff