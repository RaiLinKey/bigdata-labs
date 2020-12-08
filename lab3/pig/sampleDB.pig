recs_office = LOAD '/user/kali/input/office' USING PigStorage('\t') AS (id:int, name:chararray, place:chararray );
recs_wp = LOAD '/user/kali/input/work_place' USING PigStorage('\t') AS (id:int, type:chararray, id_office:int );
recs_workers = LOAD '/user/kali/input/workers' USING PigStorage('\t') AS (id:int, surname:chararray, name:chararray, otchestvo:chararray, position:chararray, salary:int, id_wp:int );

req1_1 = JOIN recs_workers BY id_wp, recs_wp BY id;
req1_2 = JOIN req1_1 BY id_office, recs_office BY id;
req2 = JOIN recs_wp BY id_office, recs_office BY id;
req3 = JOIN recs_workers BY id_wp, recs_wp BY id;
req4 = FILTER recs_workers BY salary >= 150000;
req5 = FILTER recs_workers BY position == 'Programmer';

STORE req1_2 INTO '/pigresult/req1';
STORE req2 INTO '/pigresult/req2';
STORE req3 INTO '/pigresult/req3';
STORE req4 INTO '/pigresult/req4';
STORE req5 INTO '/pigresult/req5';
