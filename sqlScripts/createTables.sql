
DROP TABLE IF EXISTS AgeDistribution; CREATE TABLE AgeDistribution(AgeGroup TEXT,  proportion REAL);
DROP TABLE IF EXISTS ProportionOfMalesForAge; CREATE TABLE ProportionOfMalesForAge(AgeGroup TEXT,  proportion REAL);
DROP TABLE IF EXISTS CandidateProblemList; CREATE TABLE CandidateProblemList(disorderSCTID INTEGER);
DROP TABLE IF EXISTS DisorderFilters; CREATE TABLE DisorderFilters(disorderSCTID INTEGER, filter TEXT);


-- Neonates <1/12
drop view if exists NeonateProblems;
create view NeonateProblems AS
select * from CandidateProblemList
where disorderSCTID not in
	(select disorderSCTID from DisorderFilters where filter like 'Neonates%'
	 UNION
	 select disorderSCTID from DisorderFilters where filter like 'Fertility%'
	 UNION
	 select disorderSCTID from DisorderFilters where filter like 'MiddleAgedAdults%'
	 UNION
	 select disorderSCTID from DisorderFilters where filter like 'Seniors%'
	);

-- Infants <2
drop view if exists InfantProblems;
create view InfantProblems AS
select * from CandidateProblemList
where disorderSCTID not in
	(select disorderSCTID from DisorderFilters where filter like 'Neonates%'
	 UNION
	 select disorderSCTID from DisorderFilters where filter like 'Fertility%'
	 UNION
	 select disorderSCTID from DisorderFilters where filter like 'MiddleAgedAdults%'
	 UNION
	 select disorderSCTID from DisorderFilters where filter like 'Seniors%'

	);

-- Children < 11
drop view if exists ChildrenProblems;
create view ChildrenProblems AS
select * from CandidateProblemList
where disorderSCTID not in
	(select disorderSCTID from DisorderFilters where filter like 'Neonates%'
	 UNION
	 select disorderSCTID from DisorderFilters where filter like 'Children%'
	 UNION
	 select disorderSCTID from DisorderFilters where filter like 'Fertility%'
	 UNION
	 select disorderSCTID from DisorderFilters where filter like 'MiddleAgedAdults%'
	 UNION
	 select disorderSCTID from DisorderFilters where filter like 'Seniors%'
	);

-- Youth <24
drop view if exists YouthProblems;
create view YouthProblems AS
select * from CandidateProblemList
where disorderSCTID not in
	(select disorderSCTID from DisorderFilters where filter like 'Neonates%'
	 UNION
	 select disorderSCTID from DisorderFilters where filter like 'Children%'
	 UNION
	 select disorderSCTID from DisorderFilters where filter like 'MiddleAgedAdults%'
	 UNION
	 select disorderSCTID from DisorderFilters where filter like 'Seniors%'
	);

-- MiddleAged < 65
drop view if exists MiddleAgedProblems;
create view MiddleAgedProblems AS
select * from CandidateProblemList
where disorderSCTID not in
	(select disorderSCTID from DisorderFilters where filter like 'Neonates%'
	 UNION
	 select disorderSCTID from DisorderFilters where filter like 'Children%'
	 UNION
	 select disorderSCTID from DisorderFilters where filter like 'Seniors%'
	);

-- Seniors >= 65
drop view if exists SeniorsProblems;
create view SeniorsProblems AS
select * from CandidateProblemList
where disorderSCTID not in
	(select disorderSCTID from DisorderFilters where filter like 'Neonates%'
	 UNION
	 select disorderSCTID from DisorderFilters where filter like 'Children%'
	 UNION
	 select disorderSCTID from DisorderFilters where filter like 'Fertility%'
	 UNION
	 select disorderSCTID from DisorderFilters where filter like 'MiddleAgedAdults%'
	);

