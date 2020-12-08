records = LOAD '/pigInput1' USING PigStorage(',') AS (id:int, name:chararray, position:chararray, country:chararray );

count_test = FOREACH (GROUP records ALL) GENERATE COUNT(records);

same_country = FILTER records BY country == 'New York';

max_test = ORDER records BY id DESC;
max_test1 = LIMIT max_test 1;

%declare DT `date +%y%m%dT%H%M`
STORE count_test INTO '/pigresult/$DT/count_test';
STORE same_country INTO '/pigresult/$DT/same_country';
STORE max_test1 INTO '/pigresult/$DT/max_test1';


