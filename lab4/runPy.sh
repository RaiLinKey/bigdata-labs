#!/bin/bash
pip3 install pyhdfs
itr_count=3
for ((itr=1; itr <= $itr_count; itr++)); do
    echo "Doing iteration $itr of $itr_count..."
    echo "MapRed1"
#    hdfs dfs -rm -r PBFS/itr_$((itr+1))
    yarn jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
        -D mapreduce.job.name="HITS 1" \
        -files $(pwd)/map1.py,$(pwd)/red1.py \
        -input PBFS/itr_$((itr))/ \
        -output PBFS/itr_$((itr))/mapred1 \
        -mapper $(pwd)/map1.py \
        -reducer $(pwd)/red1.py

    hdfs dfs -rm -r lab4/HITS/auth/
    echo "Doing iteration $itr of $itr_count..."
    echo "MapRed1_1"
#    hdfs dfs -rm -r PBFS/itr_$((itr))
    yarn jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
        -D mapreduce.job.name="HITS 1" \
        -files $(pwd)/map1_1.py,$(pwd)/red1_1.py \
        -input PBFS/itr_$((itr))/mapred1 \
        -output lab4/HITS/auth/ \
        -mapper $(pwd)/map1_1.py \
        -reducer $(pwd)/red1_1.py

    echo "Doing iteration $itr of $itr_count..."
    echo "MapRed1_2"
#    hdfs dfs -rm -r PBFS/itr_$((itr))
    yarn jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
        -D mapreduce.job.name="HITS 1" \
        -files $(pwd)/map1_2.py \
        -input PBFS/itr_$((itr))/mapred1 \
        -output PBFS/itr_$((itr))/mapred3 \
        -mapper $(pwd)/map1_2.py

    echo "Doing iteration $itr of $itr_count..."
    echo "MapRed2"
#    hdfs dfs -rm -r PBFS/itr_$((itr))
    yarn jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
        -D mapreduce.job.name="HITS 1" \
        -files $(pwd)/map2.py,$(pwd)/red2.py \
        -input PBFS/itr_$((itr))/mapred3 \
        -output PBFS/itr_$((itr))/mapred4 \
        -mapper $(pwd)/map2.py \
        -reducer $(pwd)/red2.py

    echo "Doing iteration $itr of $itr_count..."
    echo "MapRed2_1"
    hdfs dfs -rm -r lab4/HITS/hub
    yarn jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
        -D mapreduce.job.name="HITS 1" \
        -files $(pwd)/map2_1.py,$(pwd)/red2_1.py \
        -input PBFS/itr_$((itr))/mapred4 \
        -output lab4/HITS/hub/  \
        -mapper $(pwd)/map2_1.py \
        -reducer $(pwd)/red2_1.py

    echo "Doing iteration $itr of $itr_count..."
    echo "MapRed2_2"
#    hdfs dfs -rm -r PBFS/itr_$((itr))
    yarn jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
        -D mapreduce.job.name="HITS 1" \
        -files $(pwd)/map2_2.py \
        -input PBFS/itr_$((itr))/mapred4 \
        -output PBFS/itr_$((itr+1))/ \
        -mapper $(pwd)/map2_2.py
done
hdfs dfs -cat PBFS/itr_$((itr_count+1))/part-00000
