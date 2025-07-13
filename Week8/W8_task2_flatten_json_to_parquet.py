
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode

spark = SparkSession.builder.appName("Flatten JSON to Parquet").getOrCreate()

# Step 1: Load JSON dataset
input_path = "dbfs:/rahuldbfs/customer.json"  # Make sure to upload the file to DBFS via UI
df = spark.read.option("multiline", "true").json(input_path)

# Step 2: Flatten the JSON fields
df_flat = df.select(
    col("id"),
    col("name"),
    col("address.city").alias("city"),
    col("address.zip").alias("zip"),
    explode("contacts").alias("contact")
).select(
    "id", "name", "city", "zip",
    col("contact.type").alias("contact_type"),
    col("contact.value").alias("contact_value")
)

# Step 3: Write as external Parquet table
output_path = "dbfs:/rahuldbfs/external_tables/flattened_json_parquet"
df_flat.write.mode("overwrite").parquet(output_path)

# Register as external table
spark.sql(f"""
    CREATE TABLE IF NOT EXISTS flattened_json_table
    USING PARQUET
    LOCATION '{output_path}'
""")

# Optional: View the flattened data
df_flat.show()
