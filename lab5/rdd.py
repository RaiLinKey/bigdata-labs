from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession

# file_path = 'file:///home/kali/mysources/lab5/tweets.csv'
spark = SparkSession(sc)
file_path = 'hdfs:///user/kali/tweets/input/tweets.csv'
# Чтение данных и разбиение на колонки.
tweets = sc.textFile(file_path).map(lambda line: line[1:-1].split('","'))
# Запись выборочных колонок.
tweets1 = tweets.map(lambda row: (row[1], row[10], row[12]))
# Фильтрация только российских пользователей
tweets2 = tweets1.filter(lambda row: row[1] == 'ru')
tweets2.take(10)
# Фильтрация на содержание в твитах фамилей российских полит. деятелей
fl = tweets2.filter(lambda x: any(e in x[2] for e in [
    'Путин', 'Мишустин', 'Медведев', 'Вайно', 'Шойгу', 'Лавров', 'Патрушев', 'Собянин',
    'Кириенко', 'Набиуллина', 'Бортников', 'Володин', 'Сечин', 'Громов', 'Миллер', 'Песков',
    'Силуанов', 'Бастрыкин', 'Белоусов', 'Греф'
]))

tw = fl.map(lambda row: row[0])
t = tw.map(lambda x: (x, 1))
k = t.reduceByKey(lambda row, n: row + n)
usid = k.sortBy(lambda row: row[1], ascending=False)
# usid.collect()
usid.first()

# spark-submit --class org.apache.spark.examples.SparkPi --master yarn --deploy-mode client $SPARK_HOME/examples/jars/spark-examples_2.12-3.2.1.jar 10
