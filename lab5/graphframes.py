# pyspark --packages graphframes:graphframes:0.8.2-spark3.2-s_2.12
from graphframes import GraphFrame


df = spark.read.format("csv").\
    options(header="true", inferSchema="true").load('hdfs:///user/kali/tweets/input/tweets.csv')
v = df.select('tweetid', 'userid').toDF('id', 'userid')
e = df.select('in_reply_to_tweetid', 'tweetid').toDF('src', 'dst')
e = e.filter(e.src != 'null')
g = GraphFrame(v, e)
sc.setCheckpointDir('hdfs:///user/kali/tweets/')
result = g.connectedComponents()
res = result.select("userid").groupBy('userid').count().orderBy('count', ascending=False)
res.show(1)
rs = res
dff = rs.limit(10)
dff.sort('count', ascending=False).first()
