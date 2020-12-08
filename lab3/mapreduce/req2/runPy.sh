#!/bin/bash

hdfs dfs -rm -r lab3/mrReq2/

yarn jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
-D mapreduce.job.name="DB request 2" \
-files `pwd`/mapperReq2.py,`pwd`/reducerReq2.py \
-input input/office/ input/work_place/ \
-output lab3/mrReq2/ \
-mapper `pwd`/mapperReq2.py \
-combiner `pwd`/combinerReq2.py \
-reducer `pwd`/reducerReq2.py

hdfs dfs -cat lab3/mrReq2/part-00000
