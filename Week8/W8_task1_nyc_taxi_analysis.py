
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.appName("NYC Taxi Analysis").getOrCreate()

# Load NYC taxi data
df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("dbfs:/rahuldbfs/files/nyc_taxi_data.csv")
df.createOrReplaceTempView("taxi_data")

# Query 1: Add Revenue column
df = df.withColumn("Revenue", 
    col("Fare_amount") + col("Extra") + col("MTA_tax") + 
    col("Improvement_surcharge") + col("Tip_amount") + 
    col("Tolls_amount") + col("Total_amount")
)

# Query 2: Increasing passenger count by area
zone_df = spark.read.csv("dbfs:/rahuldbfs/files/taxi_zone_lookup.csv", header=True, inferSchema=True)
joined_df = df.join(zone_df, df["PULocationID"] == zone_df["LocationID"])
passenger_by_area = joined_df.groupBy("Borough").sum("passenger_count")

# Query 3: Real-time avg fare/revenue by vendors
vendor_avg = df.groupBy("VendorID").agg(
    avg("Fare_amount").alias("Avg_Fare"),
    avg("total_amount").alias("Avg_Total_Earnings")
)

# Query 4: Moving count of payments by payment mode
windowSpec = Window.partitionBy("payment_type").orderBy("tpep_pickup_datetime").rowsBetween(Window.unboundedPreceding, 0)
df = df.withColumn("moving_payment_count", count("payment_type").over(windowSpec))

# Query 5: Top 2 earning vendors on specific date
specific_date = "2018-01-01"
top_vendors = df.filter(to_date("tpep_pickup_datetime") == specific_date) \
    .groupBy("VendorID") \
    .agg(
        sum("total_amount").alias("total_earning"),
        sum("passenger_count").alias("total_passengers"),
        sum("trip_distance").alias("total_distance")
    ).orderBy(col("total_earning").desc()).limit(2)

# Query 6: Route with most passengers
popular_routes = df.groupBy("PULocationID", "DOLocationID") \
    .sum("passenger_count") \
    .orderBy("sum(passenger_count)", ascending=False).limit(1)

# Query 7: Top pickup locations in last 10 seconds (simulated real-time)
recent_df = df.filter(col("tpep_pickup_datetime") >= (current_timestamp() - expr("INTERVAL 10 seconds")))
top_pickups = recent_df.groupBy("PULocationID").sum("passenger_count").orderBy("sum(passenger_count)", ascending=False)

# Show results (for debugging or development)
df.show(5)
passenger_by_area.show()
vendor_avg.show()
df.select("payment_type", "moving_payment_count").show()
top_vendors.show()
popular_routes.show()
top_pickups.show()
