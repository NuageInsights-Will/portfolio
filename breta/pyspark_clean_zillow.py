from pyspark.conf import SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *


app = "demo"
conf = (SparkConf().setAppName(app)
                    .setMaster("local[1]")
                    .set('spark.driver.maxResultSize', '1g')
                    .set('spark.logConf', 'true'))

# Create a new Spark Session to work with Data Frames
spark = SparkSession.builder.appName(app).config(conf=conf).getOrCreate()


df = spark.read.csv("zillow.csv", header=True)

def is_large_space(living_space: int):
    if living_space > 2000:
        return True
    else:
        return False

udf_is_large_space = udf(is_large_space, BooleanType())

columns = ["Index", "Living_Space_sq_ft", "Beds", "Baths", "Zip", "Year", "List_Price"]
df = df.toDF(*columns)
df = df.select(*(col(c).cast(IntegerType()).alias(c) for c in df.columns))
df = df.withColumn("List_Price", df.List_Price.cast(FloatType()))
df = df.withColumn("LivingSpaceGreaterThan2000", udf_is_large_space("Living_Space_sq_ft"))
df = df.withColumn("Total_Rooms", df.Beds + df.Baths)
df = df.withColumn("List_Price_Incl_Tax", df.List_Price * 1.13)
df = df.withColumn("List_Price_Incl_Tax", df.List_Price_Incl_Tax.cast(FloatType()))
df = df.withColumn("EstMortgageFees", df.List_Price * 0.05)
df = df.drop("Zip")
df = df.filter(~ (df["Year"] < 1980))
df = df.filter(~ (df["List_Price_Incl_Tax"] < 130000))

df.write \
  .option("header", True) \
  .option("delimiter", "\t") \
  .mode("overwrite") \
  .csv("zillow_cleaned.csv")