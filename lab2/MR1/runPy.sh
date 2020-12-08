#!/bin/bash

hdfs dfs -rm -r lab2/outputCCP

yarn jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
-D mapreduce.job.name="MapReduce CCP Job via Streaming" \
-files `pwd`/mapperCCP.py,`pwd`/reduceCCP.py \
-input lab2/input/ \
-output lab2/outputCCP/ \
-mapper `pwd`/mapperCCP.py \
-combiner `pwd`/reduceCCP.py \
-reducer `pwd`/reduceCCP.py

hdfs dfs -cat lab2/outputCCP/part-00000
