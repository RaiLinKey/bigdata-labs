#!/bin/bash

hdfs dfs -rm -r lab3/mrReq4/

yarn jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
-D mapreduce.job.name="DB request 4" \
-files `pwd`/mapperReq4.py,`pwd`/reducerReq4.py \
-input input/workers/ \
-output lab3/mrReq4/ \
-mapper `pwd`/mapperReq4.py \
-combiner `pwd`/reducerReq4.py \
-reducer `pwd`/reducerReq4.py

hdfs dfs -cat lab3/mrReq4/part-00000
