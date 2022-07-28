from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession


def cleaner(s):
    list = s.split('","')
    return list[0:30]


spark = SparkSession(sc)
text = sc.textFile('hdfs:///user/kali/tweets/input/tweets.csv')
text1 = text.filter(lambda row: row.find('"tweetid"') != 0)
text2 = text1.map(cleaner)
newDF = spark.createDataFrame(text2)
newDF.createOrReplaceTempView("tweets")
df = spark.sql("""\
    CREATE TEMP VIEW tweets_foreign AS
    SELECT _2, _13, _11
    FROM tweets WHERE _11 = 'ru'
 """)
fl_text = spark.sql("""\
    SELECT * FROM tweets_foreign
    WHERE _13 LIKE '%Путин%' OR _13 LIKE '%Мишустин%' OR _13 LIKE '%Медведев%'
    OR _13 LIKE '%Вайно%' OR _13 LIKE '%Шойгу%' OR _13 LIKE '%Лавров%'
    OR _13 LIKE'%Патрушев%' OR _13 LIKE '%Собянин%' OR _13 LIKE '%Кириенко%'
    OR _13 LIKE '%Набиуллина%' OR _13 LIKE '%Бортников%' OR _13 LIKE '%Володин%'
    OR _13 LIKE '%Сечин%' OR _13 LIKE '%Громов%' OR _13 LIKE '%Миллер%'
    OR _13 LIKE '%Песков%' OR _13 LIKE '%Силуанов%' OR _13 LIKE '%Бастрыкин%'
    OR _13 LIKE '%Белоусов%' OR _13 LIKE '%Греф%'
""")
fl_text.show()
cnt = fl_text.groupBy("_2").count()
cnt.show()
cnt.createGlobalTempView("max")
spark.sql("SELECT * FROM global_temp.max").show()
spark.sql("""\
    SELECT _2, count FROM global_temp.max
    WHERE count = (
    SELECT MAX(count)
    FROM global_temp.max)
    LIMIT 1
""").show()
# spark.sql("SELECT * FROM tweets WHERE _2 LIKE 2570574680").show()
