#!/bin/bash

hdfs dfs -rm -r lab3/mrReq5/

yarn jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
-D mapreduce.job.name="DB request 5" \
-files `pwd`/mapperReq5.py,`pwd`/reducerReq5.py \
-input input/workers/ \
-output lab3/mrReq5/ \
-mapper `pwd`/mapperReq5.py \
-combiner `pwd`/reducerReq5.py \
-reducer `pwd`/reducerReq5.py

hdfs dfs -cat lab3/mrReq5/part-00000
