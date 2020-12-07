from pyspark.sql import SparkSession, SQLContext
from pyspark.sql.functions import col
from operator import add
import sys

word = sys.argv[1]
k = sys.argv[2]
input_1 = sys.argv[3]
input_2 = sys.argv[4]

spark = SparkSession.builder.appName("Task2").getOrCreate()
shape_stat = spark.read.csv(input_1, mode = "DROPMALFORMED", inferSchema = True, header = True)
shape = spark.read.csv(input_2, mode = "DROPMALFORMED", inferSchema = True, header = True)
df = shape.join(shape_stat, ["key_id", "word"], how="inner")

results = df.where(col("word") == word)\
            .filter("recognized = False")\
            .where(col("Total_Strokes") < k)\
            .groupBy("countrycode")\
            .count().sort(col("countrycode")).rdd.collect()

for row in results:
    print("%s,%s"%(row[0], row[1]))

#df.show(n=10)