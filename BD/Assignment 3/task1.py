from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import sys

word = sys.argv[1]
input_1 = sys.argv[2]
input_2 = sys.argv[3]


spark = SparkSession.builder.appName("Task1").getOrCreate()
lines = spark.read.csv(input_2, mode = "DROPMALFORMED", inferSchema = True, header = True)
if "Total_Strokes" in lines.columns:
    #print("...................", lines.columns)
    word = lines.where(col("word") == word).select(col("Total_Strokes"))

else:
    lines = spark.read.csv(input_1, mode = "DROPMALFORMED", inferSchema = True, header = True)
    word = lines.where(col("word") == word).select(col("Total_Strokes"))

recognized = word.where(col("recognized") == "True")
recognized_sum = recognized.groupBy().sum().collect()[0][0]
recognized_count = recognized.count()

unrecognized = word.where(col("recognized") == "False")
unrecognized_sum = unrecognized.groupBy().sum().collect()[0][0]
unrecognized_count = unrecognized.count()


try:
    print("%.5f"%(round(recognized_sum / recognized_count, 5)))
except:
    print("0.00000")
try:
    print("%.5f"%(round(unrecognized_sum / unrecognized_count, 5)))
except:
    print("0.00000")



'''
from pyspark.sql import SparkSession
import sys

word = sys.argv[1]

def recognizedLine(line, recognized):
    out = line.split(",")
    global word
    if recognized == 1:
        if out[0] == word and out[2] == "True":
            return out[4]
    if recognized == 0:
        if out[0] == word and out[2] == "False":
            return out[4]
    return 0

def countWord(line, recognized):
    out = line.split(",")
    global word
    if recognized == 1:
        if out[0] == word and out[2] == "True":
            return 1
    if recognized == 0:
        if out[0] == word and out[2] == "False":
            return 1
    return 0

spark = SparkSession.builder.appName("Task1").getOrCreate()
lines = spark.read.text("/home/hadoop/Downloads/BD3/shape_stat.csv").rdd.map(lambda r: r[0])
recognized_sum = lines.map(lambda stroke: recognizedLine(stroke, 1)).reduce(lambda x,y: int(x)+int(y))
unrecognized_sum = lines.map(lambda stroke: recognizedLine(stroke, 0)).reduce(lambda x,y: int(x)+int(y))
recognized_count = lines.map(lambda line: countWord(line, 1)).reduce(lambda x,y: int(x)+int(y))
unrecognized_count = lines.map(lambda line: countWord(line, 0)).reduce(lambda x,y: int(x)+int(y))

print("%.5f"%(recognized_sum / recognized_count))
print("%.5f"%(unrecognized_sum / unrecognized_count))

'''