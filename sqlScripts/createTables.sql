
DROP TABLE IF EXISTS AgeDistribution; CREATE TABLE AgeDistribution(AgeGroup TEXT,  proportion REAL);
DROP TABLE IF EXISTS ProportionOfMalesForAge; CREATE TABLE ProportionOfMalesForAge(AgeGroup TEXT,  proportion REAL);
DROP TABLE IF EXISTS CandidateProblemList; CREATE TABLE CandidateProblemList(disorderSCTID INTEGER);
DROP TABLE IF EXISTS DisorderFilters; CREATE TABLE DisorderFilters(disorderSCTID INTEGER, filter TEXT);

