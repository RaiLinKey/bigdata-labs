#!/bin/bash

hdfs dfs -rm -r lab3/mrReq1mid/

yarn jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
-D mapreduce.job.name="DB request 1 part 1" \
-files `pwd`/mapperReq1.py,`pwd`/reducerReq1.py \
-input input/workers/ input/work_place/ \
-output lab3/mrReq1mid/ \
-mapper `pwd`/mapperReq1.py \
-reducer `pwd`/reducerReq1.py

bash `pwd`/runPy2.sh
