#!/bin/bash

hdfs dfs -rm -r lab2/outputCCS

yarn jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
-D mapreduce.job.name="MapReduce CCS Job via Streaming" \
-files `pwd`/mapperCCS.py,`pwd`/reducerCCS.py \
-input lab2/input/ \
-output lab2/outputCCS/ \
-mapper `pwd`/mapperCCS.py \
-combiner `pwd`/reducerCCS.py \
-reducer `pwd`/reducerCCS.py

hdfs dfs -cat lab2/outputCCS/part-00000
