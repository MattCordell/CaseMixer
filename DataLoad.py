__author__ = 'Doug'

import sqlite3
import random

print('start')



#Load database creation scripts
file = open('sqlScripts\createTables.sql','rU')
createScript = file.read()
file.close()
file = open('sqlScripts\createIndices.sql','rU')
indexScript = file.read()
file.close()

# files containing seed data
candidateProblemList = 'data\CandidateProblemList.txt'
disorderFilters = 'data\DisorderFilters.txt'
ageDistribution = 'data\AgeDistribution.txt'
proportionOfMalesForAge = 'data\ProportionOfMalesForAge.txt'


#initialise the database
db = sqlite3.connect('CaseMixer.db')
cursor = db.cursor()
cursor.executescript(createScript)
db.commit()

#import the Base set of disorders
file = open(candidateProblemList,'rU')
for line in file:
    cursor.execute("insert into CandidateProblemList values (?)",(line,))
file.close()
db.commit()

#import the variousFilters
file = open(disorderFilters,'rU')
for line in file:
    cursor.execute("insert into DisorderFilters values (?,?)",(line.split('\t')))
file.close()
db.commit()

#import population Age distribution. And calculate cummulative values
#cummulative values allow proportional random selection.
file = open(ageDistribution,'rU')
cummulativeProportion = 0
for line in file:
    ageGroup,proportion = line.split('\t')
    cummulativeProportion = cummulativeProportion + float(proportion)
    print(cummulativeProportion)
    cursor.execute("insert into AgeDistribution values (?,?)",(ageGroup,cummulativeProportion))
file.close()
db.commit()

# import proportionOfMalesForAge.
# this file shows the likelihood somebody of a given age is male.
#cummulative calculation not required, since value is considered boolean.
file = open(proportionOfMalesForAge,'rU')
cummulativeProportion = 0
for line in file:
    ageGroup,proportion = line.split('\t')
    cursor.execute("insert into ProportionOfMalesForAge values (?,?)",(ageGroup,float(proportion)))
file.close()
db.commit()

db.close()

print('end')

