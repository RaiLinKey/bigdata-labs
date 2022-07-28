#!/bin/bash

hdfs dfs -rm -r lab3/mrReq1/

yarn jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
-D mapreduce.job.name="DB request 1 part 2" \
-files `pwd`/mapperReq12.py,`pwd`/reducerReq12.py \
-input lab3/mrReq1mid/ input/office/ \
-output lab3/mrReq1/ \
-mapper `pwd`/mapperReq12.py \
-reducer `pwd`/reducerReq12.py

hdfs dfs -cat lab3/mrReq1/part-00000
