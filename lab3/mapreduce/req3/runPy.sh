#!/bin/bash

hdfs dfs -rm -r lab3/mrReq3/

yarn jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
-D mapreduce.job.name="DB request 3" \
-files `pwd`/mapperReq3.py,`pwd`/reducerReq3.py \
-input input/workers/ input/work_place/ \
-output lab3/mrReq3/ \
-mapper `pwd`/mapperReq3.py \
-combiner `pwd`/combinerReq3.py \
-reducer `pwd`/reducerReq3.py

hdfs dfs -cat lab3/mrReq3/part-00000
