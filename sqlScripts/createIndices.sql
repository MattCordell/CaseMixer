
CREATE INDEX idx1 ON AgeDistribution(AgeGroup);
CREATE INDEX idx2 ON AgeDistribution(proportion);

CREATE INDEX idx1 ON ProportionOfMalesForAge(AgeGroup);
CREATE INDEX idx2 ON ProportionOfMalesForAge(proportion);

CREATE INDEX Idx1 ON CandidateProblemList(disorderSCTID);

CREATE INDEX Idx1 ON DisorderFilters(disorderSCTID, filter);
CREATE INDEX idx2 ON DisorderFilters(filter, disorderSCTID);

