
CREATE INDEX idx1 ON AgeDistribution(AgeGroup);
CREATE INDEX idx2 ON AgeDistribution(proportion);

CREATE INDEX idx3 ON ProportionOfMalesForAge(AgeGroup);
CREATE INDEX idx4 ON ProportionOfMalesForAge(proportion);

CREATE INDEX idx5 ON CandidateProblemList(disorderSCTID);

CREATE INDEX idx6 ON DisorderFilters(disorderSCTID, filter);
CREATE INDEX idx7 ON DisorderFilters(filter, disorderSCTID);

